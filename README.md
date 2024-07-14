A Proof of Concept (PoC) that demonstrates the potential of local data processing using the LangChain framework with the LLAMA2 model.

## Features

- Local Inference Server: Utilizes Ollama running the LLAMA2 model on an NVIDIA GPU
- LangChain: Employs WebBaseLoader and a summarization chain for effective data handling and processing
- Streamlit Interface: Provides a user-friendly UI for interactions
- Microservice Architecture: Uses Docker for containerized deployment

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
Visit [http://localhost:8501](http://localhost:8501) and provide your link to summarize the content
