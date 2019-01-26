FROM python:3.7-alpine

ADD ./requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt

ADD . /code

CMD ["python", "app.py"]
