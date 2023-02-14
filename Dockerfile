FROM python:3.8

ENV PATH=/app/bin:$PATH

WORKDIR /app

COPY . /app/

RUN set -e; \
    python3 -m venv /app; \
    . /app/bin/activate; \
    python3 -m pip install --upgrade pip setuptools; \
    pip3 install -e /app;

CMD [ "csaf-validator", "/app/examples/cisco_example.json" ]
