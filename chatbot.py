import os
from dotenv import load_dotenv
from groq import Groq
from data_loader import load_faq_data

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
faq_data = load_faq_data()

def retrieve_answer(query):
    try:
        # Load FAQ data
        faq_data = load_faq_data()
        
        # Initialize response with a default message
        response = "I'm sorry, I couldn't find a relevant answer. Please try asking differently."
        
        # Search through FAQ data for matching answer
        for item in faq_data:
            if query.lower() in item['query'].lower():  # Changed from user_query to query
                response = item['response']
                break
        
        # If no match found in FAQ, fallback to LLM
        if response == "I'm sorry, I couldn't find a relevant answer. Please try asking differently.":
            llm_response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a helpful customer support chatbot.Do not answer questions that are not related to customer support."},
                    {"role": "user", "content": query}  # Changed from user_query to query
                ]
            )
            return llm_response.choices[0].message.content
            
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"