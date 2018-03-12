FROM python:3.6-alpine

RUN apk add --no-cache --virtual build-essentials \
    musl-dev \
    gcc \
    postgresql-dev \
    postgresql \
    python3-dev \
    make \
    g++

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["./api/tests.py"]
