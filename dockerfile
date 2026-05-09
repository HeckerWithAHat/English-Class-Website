FROM python:3.13

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask

EXPOSE 5000

ENV FLASK_APP=main.py

CMD ["python", "main.py"]
