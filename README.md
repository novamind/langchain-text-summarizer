A Proof of Concept (PoC) that demonstrates the potential of local data processing using the LangChain framework with the LLAMA2 model.

## Features

- Local Inference Server: Utilizes Ollama running the LLAMA2 model on an NVIDIA GPU
- Post Endpoint: Accepts URLs as input and returns a summarized content of the web pages
- LangChain: Employs WebBaseLoader and a summarization chain for effective data handling and processing
- Microservice Architecture: Uses Docker for containerized deployment

## Prerequisites

- [Download](https://ollama.com/download) and install Ollama
- Start `ollama` and pull the `llama2` model:
```bash
ollama serve
ollama pull llama2
```

## Quick Start

Clone the repository and use the `docker-compose` commands to build and start the service.

```bash
git clone https://github.com/novamind/text_summarization.git
cd text_summarization
```
If your machine has an Nvidia GPU:
```bash
docker-compose -f docker-compose-cuda.yml up
```
Otherwise:
```bash
docker-compose -f docker-compose-cpu.yml up
```

## Usage

The endpoint accepts a JSON payload containing the URLs to be summarized as following:

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"urls":["https://en.wikipedia.org/wiki/Activation_function"]}' http://localhost:5000/summarize
```

This returned the following summary on my machine. You can get a different response.

![image](https://github.com/novamind/text_summarization/assets/26347574/03aaef8b-de6c-492d-8a87-f9afcf2a97a3)

