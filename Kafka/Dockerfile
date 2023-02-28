FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY . .

#RUN pip install -r requirements.txt
RUN pip install uuid pytz confluent-kafka

CMD ["python", "/app/main.py"]