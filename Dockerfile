FROM python:3.11.2 as base

RUN apt update && \
    apt upgrade -y && \
    pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

FROM base
EXPOSE 8000

WORKDIR /usr/src/app

COPY . .

RUN poetry install

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "8", "src.wsgi:application"]