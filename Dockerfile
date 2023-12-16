FROM python:3.8-slim-buster

WORKDIR /app

COPY ./provider-service/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./provider-service .

CMD ["uvicorn", "main:app", "--host", "*", "--port", "666"]

EXPOSE 666