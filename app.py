from flask import Flask, render_template, request
from agents import hr_agent, technical_agent, career_agent
from scorer import score_answer
from memory import save_memory, load_memory

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        role = request.form["role"]
        answer = request.form["answer"]

        hr = hr_agent(answer)
        tech = technical_agent(role)
        career = career_agent(role)
        score = score_answer(answer)

        previous = load_memory()

        result = f"""
HR Feedback: {hr}

Technical Question: {tech}

Career Advice: {career}

Interview Score: {score}/10

Previous Role: {previous}
"""

        save_memory(role)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)