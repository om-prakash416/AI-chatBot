import os
import json
import datetime
import csv
import streamlit as st
import random
from chatbot_logic import init_nlp_chatbot, process_input, generate_gpt_response


clf, vectorizer, intents = init_nlp_chatbot()


if not os.path.exists('chat_log.csv'):
    with open('chat_log.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['User Input', 'Chatbot Response', 'Timestamp'])


with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    st.markdown("**Developed by: Om Prakash**")

def main():
    st.title("Smart Chatbot Interface")
    st.sidebar.header("Navigation")
    menu = ["Home", "Conversation History", "About", "ChatGPT"]
    choice = st.sidebar.radio("Menu", menu)

    if "user_name" not in st.session_state:
        st.session_state["user_name"] = None

   
    if not st.session_state["user_name"]:
        st.session_state["user_name"] = st.text_input("What's your name?", placeholder="Enter your name here")
        if st.session_state["user_name"]:
            st.success(f"Hello, {st.session_state['user_name']}! How can I assist you today?")
        return

    if choice == "Home":
        st.header(f"Welcome, {st.session_state['user_name']}!")
        user_input = st.text_input("You:", placeholder="Ask me anything...")
        if user_input:
            response = process_input(user_input, clf, vectorizer, intents)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input, response, timestamp])
            st.text_area("Chatbot:", response, height=120)

    elif choice == "Conversation History":
        st.header("Conversation History")
        with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                st.text(f"User: {row[0]}")
                st.text(f"Chatbot: {row[1]}")
                st.text(f"Timestamp: {row[2]}")
                st.markdown("---")

    elif choice == "About":
        st.header("About")
        st.write("This chatbot is built using NLP, Logistic Regression, and Streamlit. It also integrates ChatGPT for broader knowledge.functionalities of chat gpt also.Develop by OM Prakash")

    elif choice == "ChatGPT":
        st.header("ChatGPT Assistant")
        user_input = st.text_input("You:", placeholder="Ask me anything powered by GPT...")
        if user_input:
            gpt_response = generate_gpt_response(user_input)
            st.text_area("ChatGPT:", gpt_response, height=120)

if __name__ == '__main__':
    main()
