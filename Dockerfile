FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y libmariadb-dev \
    && apt-get install -y python3-pip \
    && apt-get install -y build-essential \
    && apt-get install -y libcurl4-openssl-dev \
    && apt-get install -y libssl-dev \
    && pip install --upgrade pip
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]