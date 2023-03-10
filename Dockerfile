FROM python:3.10

WORKDIR /usr/src/app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

EXPOSE 2000

