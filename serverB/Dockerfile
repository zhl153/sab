FROM python:3.6-slim

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends build-essential \
    && apt-get clean \
    && apt-get install -y dnsutils python-dev python-pip\
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install -r requirements.txt

CMD ["python", "serverB_client.py"]

