FROM python:3.5.9-alpine3.10

RUN mkdir /code
COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY blabla.py /code/blabla.py

CMD python /code/blabla.py

