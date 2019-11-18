FROM ubuntu

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN apt-get update -qq \
    && apt-get install -y python \
    && apt-get install -y --no-install-recommends build-essential \
    && apt-get clean \
    && apt-get install -y dnsutils python-dev python-pip\
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install -r requirements.txt

EXPOSE 50001

CMD ["python", "middle.py"]

