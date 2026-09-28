from flask import Flask, url_for, render_template, request
import os
from dotenv import load_dotenv
from openai import OpenAI


app=Flask(__name__)
load_dotenv()
api_key=os.getenv("openai_api_key")
client=OpenAI(api_key=api_key)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    ques=request.form.get("question")
    response=self.client.responses.create(
            model="gpt-5",
            input=[
                {"role":"system","content":"act like a math teacher"},
                {"role":"user","content":ques}
            ],
            temperature=0.7,
            max_output_tokens=512
        )
    answer=response.output_text.strip()
    return jsonify({"response":answer}),200

@app.route("/summarize", methods=["POST"])
def summarize():
    email=request.form.get("email")
    prompt=f"summarize the following email in 2-3 sentences:{email}"
    response=client.responses.create(
        model="gpt-5",
        input=[
            {"role":"system","content":"act as expert email assistant "},
            {"role":"user","content":prompt}
        ],
        temperature=0.7,
        max_output_tokens=512
    )
    summary=response.output_text.strip()
    return jsonify({"response":summary}),200


if __name__=="__main__":
    app.run(debug=True)