# syntax=docker/dockerfile:experimental
FROM python:3.13.1-bullseye
	
WORKDIR /app

COPY pyproject.toml .
COPY LICENSE .
COPY *.md .
COPY asyncapi.yaml .
COPY src/ src/
RUN pip install -e .

ENV RABBITMQ_HOST=mov-mq
ENV RABBITMQ_PORT=5672.
ENV RABBITMQ_USERNAME=mov.
ENV RABBITMQ_PASSWORD=password
ENV RABBITMQ_MAX_RETRIES=100
ENV RABBITMQ_RETRY_SLEEP=3

ENV LOG_CONSOLE_LEVEL=DEBUG
ENV LOG_FILE_LEVEL=DEBUG
ENV LOG_FILE_MAX_BYTES=1000000
ENV LOG_FILE_BACKUP_COUNT=5

HEALTHCHECK CMD test -s /app/{$LOG_DIR:-logs}/{$COMPONET_ID_FILE_NAME:-component_id.json}

CMD ["python", "src/c2_treatment_autonomy_valuator"] 