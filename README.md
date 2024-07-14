A Proof of Concept (PoC) that demonstrates the potential of local data processing using the LangChain framework with LLMs.

## Features

- Local Inference Server: Utilizes Ollama running any supported LLM (customizable) on an NVIDIA GPU
- LangChain: Employs WebBaseLoader and a summarization chain for effective data handling and processing
- Streamlit Interface: Provides a user-friendly UI for interactions
- Microservice Architecture: Uses Docker for containerized deployment

## Quick Start

Follow these steps to clone the repository and start the service using Docker Compose.

1. Clone the repository:

```bash
git clone https://github.com/novamind/text_summarization.git
cd text_summarization
```

2. Start the service:

- If your machine has an Nvidia GPU:
```bash
docker-compose -f docker-compose-cuda.yml up
```
- Otherwise:
```bash
docker-compose -f docker-compose-cpu.yml up
```

3. Visit [http://localhost:8501](http://localhost:8501) and provide your link to summarize the content

## Configuration

Use the .env file to change the model settings.