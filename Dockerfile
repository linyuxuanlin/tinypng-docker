FROM python:3.8-slim-buster

RUN pip install tinify watchdog

WORKDIR /app

COPY . /app

ENV TINYPNG_API_KEY=<your_tinypng_api_key>
ENV INPUT_DIR=/app/input
ENV OUTPUT_DIR=/app/output

CMD ["python", "main.py"]
