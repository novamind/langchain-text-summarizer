A Proof of Concept (PoC) that demonstrates the potential of local data processing using the LangChain framework with the LLAMA2 model.

## Features

- Local Inference Server: Utilizes Ollama running the LLAMA2 model on an NVIDIA GPU
- Post Endpoint: Accepts URLs as input and returns a summarized content of the web pages
- LangChain: Employs WebBaseLoader and a summarization chain for effective data handling and processing
- Microservice Architecture: Uses Docker for containerized deployment

## Prerequisites

- [Download](https://ollama.com/download/windows) and install Ollama
- Fetch the `llama2` model:
```bash
ollama pull llama2
```

## Quick Start

Clone the repository and use the `docker-compose` commands to build and start the service.

```bash
git clone https://github.com/novamind/text_summarization.git
cd text_summarization
docker-compose up
```

## Usage

The endpoint accepts a JSON payload containing the URLs to be summarized as following:
```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"urls":["https://example.com/"]}' http://localhost:5000/summarize
```
## Example Response
```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"urls":["https://habr.com/en/articles/818317/"]}' http://localhost:5000/summarize
```

This returned the following summary on my machine. You can get a different response.

![image](https://github.com/novamind/text_summarization/assets/26347574/a1e8e28e-42a1-4c40-9285-dfc79b0733c8)
