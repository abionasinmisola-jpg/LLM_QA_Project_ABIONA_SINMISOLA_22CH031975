from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini API
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in your environment variables.")
genai.configure(api_key=API_KEY)

@app.route("/", methods=["GET", "POST"])
def home():
    user_question = ""
    api_response = ""
    
    if request.method == "POST":
        user_question = request.form.get("question", "").strip()
        if user_question:
            try:
                model = genai.GenerativeModel("models/gemini-flash-latest")
                response = model.generate_content(user_question)
                api_response = response.text
            except Exception as e:
                api_response = f"Error: {str(e)}"
    
    return render_template(
        "index.html",
        user_question=user_question,
        api_response=api_response
    )

if __name__ == "__main__":
    app.run(debug=True)

