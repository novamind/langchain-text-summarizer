FROM python:3.12-slim
COPY requirements.txt /app/
WORKDIR /app
RUN pip3 install --upgrade pip -r requirements.txt
COPY app.py /app/
COPY summarizer.py /app/
COPY streamlit_app.py /app/
ENTRYPOINT ["streamlit"]
CMD ["run", "streamlit_app.py"]