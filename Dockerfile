FROM python:3.7-slim

COPY . /app
WORKDIR /app

RUN apt update && apt install -y gcc
RUN pip install psutil

ENTRYPOINT ["python", "mon.py"]
CMD ["mem","cpu"]