```markdown
# ChatGPT Local

Aplicação web local em Flask que integra com Ollama para criar um ChatGPT privado. Permite digitar perguntas em um formulário e receber respostas geradas pelo modelo Llama2. Dockerizado para fácil deploy e portabilidade, podendo rodar em qualquer máquina com Docker.

---

## Funcionalidades

- Chat local com modelo Llama2 via Ollama.
- Formulário web para enviar perguntas.
- Respostas exibidas na mesma página.
- Dockerizado para fácil execução.

---

## Pré-requisitos

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Pelo menos 6 GB de RAM disponível para rodar o modelo Llama2.

---

## Estrutura do Projeto

```

chatgpt\_local/
│
├─ app.py                 # Código principal Flask
├─ Dockerfile             # Dockerfile da aplicação
├─ docker-compose.yml     # Configuração dos containers
├─ templates/
│   └─ index.html         # Página web com formulário
├─ static/
│   └─ style.css          # Estilo da página

````

---

## Passo a passo

### 1. Clonar o projeto
```bash
git clone https://github.com/josehenriqueprogramador/chatgpt_local.git
cd chatgpt_local
````

### 2. Subir os containers

```bash
docker-compose up -d --build
```

Isso vai iniciar:

* `chatgpt_local`: aplicação Flask na porta `5000`
* `ollama`: servidor Ollama na porta `11434`

### 3. Baixar o modelo Llama2 no container Ollama

```bash
docker exec -it ollama /bin/sh
ollama pull llama2
exit
```

> O modelo precisa ser baixado apenas uma vez.

### 4. Acessar a aplicação

No navegador, abra:

```
http://localhost:5000
```

Digite sua pergunta e receba a resposta do modelo Llama2.

---

## Observações

* Se houver erro de memória, aumente a RAM disponível para Docker.
* A aplicação usa a rede interna do Docker para se comunicar com Ollama (`http://ollama:11434`).
* Para parar a aplicação:

```bash
docker-compose down
```

---

## Docker Hub

Você pode puxar a imagem pronta da aplicação:

```bash
docker pull josehenriquejardim/chatgpt_local:latest
```

---

## Licença

MIT License

```

---
