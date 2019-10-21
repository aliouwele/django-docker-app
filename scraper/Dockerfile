FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /scraper
WORKDIR /scraper
COPY requirements.txt /scraper/
RUN pip install -r requirements.txt
COPY . /scraper/