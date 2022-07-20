FROM python:3.9

RUN groupadd app && useradd -g app app
RUN mkdir /app
WORKDIR /app

COPY . /app/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

USER app
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000