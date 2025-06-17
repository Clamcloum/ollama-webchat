from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral-fr"  # Change ici si tu utilises un autre modèle

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")

    payload = {
        "model": MODEL,
        "prompt": user_input,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    if response.status_code == 200:
        data = response.json()
        return jsonify({"response": data["response"]})
    else:
        return jsonify({"error": "Erreur Ollama"}), 500

if __name__ == "__main__":
    app.run(debug=True)
