FROM python:latest

RUN mkdir test

WORKDIR /test

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "backend.src.main:app", "--reload"]