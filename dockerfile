FROM python:3.10-slim-bullseye

WORKDIR /usr/app/givetime

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY givetime .

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]