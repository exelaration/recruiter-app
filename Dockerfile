FROM python:3.6-alpine

ARG WEB_PORT

RUN apk add --no-cache bash postgresql postgresql-client postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev git

ENV PYTHONUNBUFFERED 1
ENV PROJECT_HOME=/code

RUN mkdir $PROJECT_HOME
WORKDIR $PROJECT_HOME

COPY ./requirements.txt $PROJECT_HOME
RUN pip install -r requirements.txt

COPY . $PROJECT_HOME

EXPOSE $WEB_PORT

ADD ./docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh
CMD ["/docker-entrypoint.sh"]