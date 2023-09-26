# syntax=docker/dockerfile:1

FROM python:3.10.4

WORKDIR /sm-webui-flask-docker

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]