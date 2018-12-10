FROM python:3.7-slim

WORKDIR /app

RUN mkdir client
RUN apt-get update
RUN apt-get -y install python3-pip
RUN pip3 install blessings

COPY ./client /app/client
COPY ./config.py /app

CMD ["python3", "-m", "client"]
