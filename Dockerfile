FROM python:3.8

WORKDIR /app
# 
COPY csaf_validator.py /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD [ "python", "./csaf_validator.py", "--input", "cisco.json" ]
