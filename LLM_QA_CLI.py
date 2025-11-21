# LLM_QA_CLI.py
import os
import re
import sys
from google import genai

def preprocess(text):
    # basic preprocessing: lowercase, remove punctuation, simple tokenization
    text = text.lower().strip()
    # remove punctuation (keep simple characters and spaces)
    text = re.sub(r'[^\w\s]', '', text)
    # simple tokenization (split on whitespace)
    tokens = text.split()
    # return processed question as a single string (tokens joined)
    return " ".join(tokens)

def ask_gemini(prompt, model="gemini-2.5-flash"):
    # create client (reads GEMINI_API_KEY from env automatically)
    client = genai.Client()
    # call the generate_content method (per Google quickstart)
    response = client.models.generate_content(model=model, contents=prompt)
    # response.text returns the model output (quickstart shows this field)
    return response.text

def main():
    if len(sys.argv) > 1:
        raw_question = " ".join(sys.argv[1:])
    else:
        raw_question = input("Enter your question: ")

    processed = preprocess(raw_question)
    print("\nProcessed question:", processed)

    # Construct prompt — you can add system/context instructions here
    prompt = f"Question: {processed}\nAnswer concisely:"
    answer = ask_gemini(prompt)

    print("\n--- LLM Answer ---\n")
    print(answer)

if __name__ == "__main__":
    main()
