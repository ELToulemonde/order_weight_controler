FROM python:3.11-slim-bullseye
RUN mkdir /weight-controler
WORKDIR /weight-controler
COPY balance balance
COPY caisse caisse
COPY data data
COPY weight_controler_interface weight_controler_interface
COPY weight_controler_api weight_controler_api
COPY logger.py .
COPY requirements.txt .
COPY run.py .

RUN pip install -r requirements.txt
CMD ["python", "run.py"]

