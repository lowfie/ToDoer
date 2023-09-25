FROM python:3.11.2

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

COPY pyproject.toml /app/

RUN apt-get update && pip install --upgrade pip && pip install "poetry==1.4.2" && \
    poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . /app/

EXPOSE 8000
