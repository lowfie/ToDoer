FROM python:3.11.2

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

RUN apt-get update
RUN pip install --upgrade pip

RUN pip install "poetry==1.4.2"
COPY pyproject.toml /app/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . /app/

EXPOSE 8000
