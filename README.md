# 🧠 ChatGPT Local com Docker + Ollama

![Docker](https://img.shields.io/badge/Docker-Container-blue) ![Python](https://img.shields.io/badge/Python-3.10-green) ![Flask](https://img.shields.io/badge/Flask-Framework-orange)

Uma aplicação local de **ChatGPT** usando **Flask** e **Ollama**, totalmente containerizada. Faça perguntas na interface web e receba respostas usando o modelo **Llama2**.

---

## ✨ Funcionalidades

* 🖥 Interface web simples para digitar perguntas
* 🤖 Respostas via modelo **Llama2** dentro do container Ollama
* 📦 Totalmente containerizada para fácil execução em qualquer máquina com Docker
* 🔄 Atualização simples dos containers e do modelo

---

## ⚠️ Pré-requisitos

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* Conexão à internet (para baixar Ollama e o modelo Llama2)
* **💾 Pelo menos 6 GB de RAM disponíveis** para o container Ollama

> Sem memória suficiente, o modelo **Llama2** não será carregado e retornará erro.

---

## 🚀 Instalação e Uso

1. **Clonar o repositório**

```bash
git clone https://github.com/josehenriqueprogramador/chatgpt_local.git
cd chatgpt_local
```

2. **Subir os containers**

```bash
docker-compose up -d --build
```

Isso criará dois containers:

* `chatgpt_local` → aplicação Flask
* `ollama` → servidor Ollama

3. **Baixar o modelo Llama2 dentro do container Ollama**

```bash
docker exec -it ollama /bin/sh
ollama pull llama2
exit
```

> Este passo é obrigatório para que o ChatGPT local funcione.

4. **Acessar a aplicação**

Abra no navegador:

```
http://localhost:5000
```

Digite sua pergunta e veja a resposta do ChatGPT.

---

## 🐳 Usando a imagem do Docker Hub

A imagem do ChatGPT local está disponível no Docker Hub:

```bash
docker pull josehenriquejardim/chatgpt_local:latest
docker run -p 5000:5000 josehenriquejardim/chatgpt_local:latest
```

---

## 📂 Estrutura do Projeto

```
chatgpt_local/
│
├─ app.py
├─ Dockerfile
├─ docker-compose.yml
├─ templates/
│   └─ index.html
├─ static/
│   └─ style.css
```

---

## 💡 Dicas e Observações

* Certifique-se de que o container Ollama está rodando e o modelo Llama2 foi baixado.
* Ajuste a variável `OLLAMA_HOST` em `app.py` caso queira conectar a outro host ou porta.
* **Memória mínima de 6 GB é necessária** para rodar Llama2 sem erros.
* Você pode forçar atualização do modelo usando:

```bash
docker exec -it ollama /bin/sh
ollama pull llama2
```

* Para parar os containers:

```bash
docker-compose down
```

---
