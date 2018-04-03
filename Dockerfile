FROM ubuntu:latest

MAINTAINER Burak Tahtaci <tahtaciburak@gmail.com>

RUN apt-get update

RUN apt-get install python3

CMD ["mkdir","/home/pinger/"]

ADD ["./main.py","/home/pinger"]

ADD ["./config.json","/home/pinger"]

ENTRYPOINT python3 /home/pinger/main.py
