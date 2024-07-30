A Proof of Concept (PoC) that demonstrates the potential of local data processing using the LangChain framework with LLMs.

## Features

- Local Inference Server: Utilizes Ollama running any supported LLM (customizable) on an NVIDIA GPU
- LangChain: Employs WebBaseLoader and off-the-shelf chains for effective data handling and processing
- Multi-Agent System: Includes agents for summarization and question answering
- Streamlit Interface: Provides a user-friendly UI for interactions
- Microservice Architecture: Uses Docker for containerized deployment

![image](https://github.com/user-attachments/assets/0c66177e-ed04-4c9c-ade8-e88919ce7d2e)

## Quick Start

Follow these steps to clone the repository and start the service using Docker Compose.

1. Clone the repository:

```bash
git clone https://github.com/novamind/langchain-text-summarizer.git
cd langchain-text-summarizer
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

![image](https://github.com/user-attachments/assets/82085a48-7b61-4a83-9c22-2e6c67e6ce4c)


## Configuration

Use the .env file to change the model settings.
