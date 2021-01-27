FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Santiago

RUN apt-get update -y && \
    apt-get -y install build-essential python3-dev python3-pip python3-setuptools python3-wheel && \
    apt-get -y install python3-cffi

COPY . /app
WORKDIR /app
RUN python3 -m pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "app:app"]
