FROM python:3-alpine
MAINTAINER Simon ROBERT <simon.robert24@gmail.com>
#ubuntu:20.04 FROM node:12.16-alpine
RUN apk add --no-cache bash

# RUN apt-get update
# RUN apt install -y python3-pip

WORKDIR /src

COPY . .



RUN pip install -r requirements.txt --no-cache-dir

CMD ["gunicorn","--timeout","600","-b",":9091","-w","4","base_gui:app"]