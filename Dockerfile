FROM python:3.11.2 as base

RUN apt update && \
    apt upgrade -y && \
    pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

FROM base
EXPOSE $(DOCKER_EXPOSE_PORT)

WORKDIR /usr/src/app

COPY . .

RUN poetry install