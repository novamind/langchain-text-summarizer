FROM python:3.9-slim
COPY requirements.txt /app/
WORKDIR /app
RUN pip3 install --upgrade pip -r requirements.txt
COPY app.py /app/
COPY summarizer.py /app/
ENTRYPOINT ["python"]
CMD ["app.py"]