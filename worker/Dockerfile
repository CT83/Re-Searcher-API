FROM ubuntu:19.10

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install libpq-dev gcc python3-dev musl-dev python3-pip -y

WORKDIR /app

COPY ./api/requirements/base.txt /app/requirements/base.txt
RUN pip3 install -r /app/requirements/base.txt

COPY ./api/ /app

ENV FLASK_APP main_app.py
ENV FLASK_ENV production
ENV PYTHONUNBUFFERED 1
ENV DONT_RUN_SCHEDULAR True

# Fixing utc, timezone
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends tzdata  && rm -rf /var/lib/apt/lists/*
RUN ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  && dpkg-reconfigure --frontend noninteractive tzdata

CMD celery worker -A main_app.client --loglevel=info