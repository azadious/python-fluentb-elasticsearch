FROM python:3.9

COPY ./requirements.txt /tmp
RUN pip3 install --upgrade pip
RUN pip3 install -r /tmp/requirements.txt
RUN mkdir /app
WORKDIR /app
