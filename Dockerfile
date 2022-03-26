FROM python:3-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD requirements.txt /code/requirements.txt

RUN apk add libpq-dev gcc

# install dependencies
RUN apk add -u zlib-dev jpeg-dev gcc musl-dev
RUN python3 -m pip install --upgrade pip

RUN set -ex \ 
    && apk add --virtual .build-deps build-base \ 
    && python -m venv .venv \
    && /.venv/bin/pip install --upgrade pip \
    && /.venv/bin/pip install  -r /code/requirements.txt \
    && apk del .build-deps

ENV VIRTUAL_ENV /.venv
ENV PATH /.venv/bin:$PATH

WORKDIR /code

