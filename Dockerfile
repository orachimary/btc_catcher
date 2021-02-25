FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/app/src/
WORKDIR /usr/app/src/
COPY requirements.txt /usr/app/src/
RUN pip install  -r requirements.txt
COPY  ./src  /usr/app/src/
