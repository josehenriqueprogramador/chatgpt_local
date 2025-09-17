from flask import Flask, request, render_template
import os
import requests

app = Flask(__name__)

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama:11434")

@app.route("/", methods=["GET", "POST"])
def home():
    resposta = None
    if request.method == "POST":
        pergunta = request.form.get("pergunta")
        try:
            response = requests.post(f"{OLLAMA_HOST}/v1/chat/completions", json={
                "model": "llama2",
                "messages": [{"role": "user", "content": pergunta}]
            })
            resposta = response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            resposta = f"Erro ao acessar Ollama: {e}"
    return render_template("index.html", resposta=resposta)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
