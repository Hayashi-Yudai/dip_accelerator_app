FROM python:3.7.6-slim

RUN mkdir /app
WORKDIR /app

ADD assets/model_brief.sav /app
ADD requirements.txt /app

RUN pip install -r requirements.txt
