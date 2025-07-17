# AI-chatBot
# **Smart Chatbot Interface** :robot:

## **Project Overview**

The **Smart Chatbot Interface** is a conversational AI built using **Natural Language Processing (NLP)** and **Streamlit**. The project integrates a machine learning-based chatbot for predefined intents and also integrates **ChatGPT** to handle broader knowledge-based queries. The chatbot offers an interactive, personalized experience and keeps track of conversations.

### **Features:**
- **NLP-based Chatbot**: Uses machine learning classifiers and vectorizers to process and respond to user input.
- **ChatGPT Integration**: Provides broader responses beyond predefined intents using OpenAI's GPT.
- **Conversation History**: Tracks and displays past conversations, stored in a CSV file.
- **Personalized Interaction**: Allows users to enter their names for a personalized experience with the chatbot.

---

## **Technologies Used**

- **Streamlit**: For building the interactive web interface.
- **Scikit-learn**: For machine learning-based intent classification.
- **OpenAI API (ChatGPT)**: For generating responses to broader queries.
- **Pandas/CSV**: For storing and managing conversation logs.
- **Joblib**: For loading pre-trained models.

---

## **Installation Instructions**

To run this project locally, follow the steps below.

### 1. **Clone the Repository**

First, clone this repository to your local machine using the following command:

```bash
git clone https://github.com/om-prakash416/AI-chatBot.git
cd AI-chatBot

pip install -r requirements.txt

----------- Or ----------------

pip install streamlit
pip install scikit-learn
pip install openai
pip install joblib
pip install pandas
pip install python-dotenv


## **Make .env file on your directly**
openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your actual OpenAI API key

python -m venv venv

.\venv\Scripts\Activate

streamlit run app.py

Local URL:  http://localhost:8501

### **Preview**
![Chatbot Screenshot](https://raw.githubusercontent.com/om-prakash416/AI-chatBot/main/image.png)
