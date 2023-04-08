FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY . .

RUN pip install confluent-kafka

CMD ["python", "/app/main.py"]