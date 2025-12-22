ARG URL_DOCKER_INDEX=index.docker.io
ARG URL_PYPI_INDEX=https://pypi.org/simple
FROM ${URL_DOCKER_INDEX}/library/python:3.13.10-slim-trixie

ARG URL_PYPI_INDEX
ENV URL_PYPI_INDEX=${URL_PYPI_INDEX}

WORKDIR /app
COPY ./main ./
COPY ./requirements.txt ./requirements.txt
RUN pip install --index-url ${URL_PYPI_INDEX} -r requirements.txt