# pull the python image
FROM python:3.9
# switch working directory
WORKDIR /app
# copy the requirements file into the image 
COPY requirements.txt /app
# install the dependencies and packages in the requirements file
RUN pip3 install --upgrade pip -r requirements.txt
# copy every content from the local file to the image
COPY . /app
# configure the container to run in an executed manner
ENTRYPOINT ["python"]
CMD ["app.py"]