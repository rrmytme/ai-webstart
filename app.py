from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Configure your OpenAI API key
openai.api_key = os.getenv("openai.api_key")


# Function to generate website content using AI
def generate_content(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    # Get user input
    company_name = request.form["company_name"]
    services = request.form["services"]
    target_audience = request.form["target_audience"]

    # Generate content
    prompt = f"Create a professional website for an IT service company named {company_name} that offers {services}. The target audience is {target_audience}. Provide a homepage layout with headings, sections, and content."
    generated_content = generate_content(prompt)

    return render_template("result.html", content=generated_content)


if __name__ == "__main__":
    app.run(debug=True)
