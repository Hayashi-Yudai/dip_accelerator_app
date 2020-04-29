FROM python:3.7.6-slim

RUN mkdir /app
WORKDIR /app

ADD analyzer/ /app/analyzer/
ADD app/ /app/app
ADD assets/ /app/assets
ADD media/ /app/media
ADD manage.py /app/
ADD requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD gunicorn app.wsgi -b 0.0.00:$PORT
