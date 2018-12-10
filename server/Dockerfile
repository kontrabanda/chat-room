FROM python:3.7-slim

WORKDIR /app

RUN mkdir server

COPY ./server /app/server
COPY ./config.py /app

CMD ["python3", "-m", "server"]
