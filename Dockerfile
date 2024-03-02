FROM python:3


ENV PYTHONUNBUFFERED=1
RUN mkdir /Django_Backend
WORKDIR /Django_Backend
COPY . /Django_Backend/
RUN pip install -r requirements.txt