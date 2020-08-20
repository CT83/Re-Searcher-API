FROM python:3.8-buster

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install libpq-dev gcc python3-dev musl-dev python3-pip -y

WORKDIR /app

COPY requirements/base.txt /app/requirements/base.txt
RUN pip3 install -r /app/requirements/base.txt

COPY . /app

RUN chmod +X start_flask.sh

ENV FLASK_APP main_app.py
ENV FLASK_ENV development
ENV PYTHONUNBUFFERED 1

CMD ["/bin/sh","./start_flask.sh"]