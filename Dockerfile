FROM python:3.10-alpine

RUN mkdir -p /roulette

WORKDIR /roulette

COPY src/ .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONPATH=src/

CMD ["python3", "-m", "roulette"]
