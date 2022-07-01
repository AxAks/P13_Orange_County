FROM python:3.9

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /code/
CMD python manage.py runserver 0.0.0.0:8000