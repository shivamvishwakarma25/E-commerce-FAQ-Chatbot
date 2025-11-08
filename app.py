import streamlit as st
from chatbot import retrieve_answer

st.set_page_config(page_title="E-commerce FAQ Chatbot")
st.title("E-commerce FAQ Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# FAQ suggestions
if len(st.session_state.messages) == 0:
    st.markdown("### 💡 Try asking:")
    col1, col2, col3 = st.columns(3)
    
    faq_questions = [
        "📦 Shipping policy",
        "💳 Payment methods", 
        "🔄 Return process"
    ]
    
    for col, question in zip([col1, col2, col3], faq_questions):
        with col:
            if st.button(question):
                user_input = question
                st.session_state.messages.append({"role": "user", "content": user_input})
                response = retrieve_answer(user_input)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()

user_input = st.chat_input("Ask your question here...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = retrieve_answer(user_input)
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
