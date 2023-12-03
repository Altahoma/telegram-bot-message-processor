FROM python:3.11.0-slim
LABEL authors="altahoma"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY . .

RUN chmod +x wait-for-it.sh
RUN pip install -r requirements.txt
