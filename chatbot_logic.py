import os
import json
import random
import openai
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def init_nlp_chatbot():
    with open("intents.json", "r") as file:
        intents = json.load(file)
    vectorizer = TfidfVectorizer()
    clf = LogisticRegression(random_state=0, max_iter=10000)
    patterns, tags = [], []
    for intent in intents:
        for pattern in intent["patterns"]:
            patterns.append(pattern)
            tags.append(intent["tag"])
    x = vectorizer.fit_transform(patterns)
    clf.fit(x, tags)
    return clf, vectorizer, intents

def process_input(input_text, clf, vectorizer, intents):
    x_input = vectorizer.transform([input_text])
    tag = clf.predict(x_input)[0]
    for intent in intents:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "Sorry, I didn't understand that."

def generate_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
          messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)
        print(response['choices'][0]['message']['content'])
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return str(e)
