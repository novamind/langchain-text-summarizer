FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]