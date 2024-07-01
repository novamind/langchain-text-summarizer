# Text Summarization

Python project employing the LLaMA model to generate a concise summary of given web pages

## Installation

Clone the repository and use the docker-compose commands to build and start the service.

```bash
docker-compose build
docker-compose up
```
Make sure you run this command from the project's root folder where the docker-compose.yml is located.

## Usage

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"urls":["https://example.com/"]}' http://localhost:5000/summarize
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
