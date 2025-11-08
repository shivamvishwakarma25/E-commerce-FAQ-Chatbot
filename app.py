import streamlit as st
from chatbot import retrieve_answer

# Hide developer menu
st.set_page_config(page_title="E-commerce FAQ Chatbot")

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("E-commerce FAQ Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# FAQ buttons positioned above chat input
st.markdown("---")
st.markdown("#### Frequently Asked Questions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("What's your shipping policy?", use_container_width=True):
        user_input = "What's your shipping policy?"
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = retrieve_answer(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
    
    if st.button("How do I return an item?", use_container_width=True):
        user_input = "How do I return an item?"
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = retrieve_answer(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

with col2:
    if st.button("What payment methods do you accept?", use_container_width=True):
        user_input = "What payment methods do you accept?"
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = retrieve_answer(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
    
    if st.button("How do I track my order?", use_container_width=True):
        user_input = "How do I track my order?"
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = retrieve_answer(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

with col3:
    if st.button("What's your delivery time?", use_container_width=True):
        user_input = "What's your delivery time?"
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = retrieve_answer(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
    
    if st.button("How do I cancel my order?", use_container_width=True):
        user_input = "How do I cancel my order?"
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = retrieve_answer(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

st.markdown("---")

# Chat input
user_input = st.chat_input("Ask your question here...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = retrieve_answer(user_input)
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
