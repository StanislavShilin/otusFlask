FROM python:3.11-slim as build
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get install -y python3-dev build-essential
COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
