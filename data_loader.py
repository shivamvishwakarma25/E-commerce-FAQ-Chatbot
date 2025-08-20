from datasets import load_dataset
import pandas as pd

def load_faq_data():
    dataset = load_dataset("bitext/Bitext-customer-support-llm-chatbot-training-dataset", split="train")
    df = pd.DataFrame(dataset)[["instruction", "response"]]
    return df.rename(columns={"instruction": "query", "response": "response"}).to_dict(orient="records")
