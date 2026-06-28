FROM python:3.12-alpine AS builder

WORKDIR /app

ENV PYTHON_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHON_NO_CACHE_DIR=1

RUN python3 -m venv venv

COPY requirements.txt .

RUN /app/venv/bin/pip3 install --upgrade --retries 5 pip && \
    /app/venv/bin/pip3 install --retries 5 -r requirements.txt

FROM python:3.12-alpine AS final

ENTRYPOINT ["/app/docker-entrypoint.sh"]

WORKDIR /app

ENV PATH=/app/venv/bin/:$PATH

RUN adduser --uid 1001 --disabled-password gunicorn --home /app

COPY --chown=gunicorn docker-entrypoint.sh docker-entrypoint.sh

COPY --chown=gunicorn application/ application/
COPY --chown=gunicorn static/ static/
COPY --chown=gunicorn users/ users/
COPY --chown=gunicorn manage.py manage.py

COPY --from=builder --chown=gunicorn /app/venv /app/venv

USER gunicorn