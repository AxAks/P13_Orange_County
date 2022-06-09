FROM python:3.9
ENV VIRTUAL_ENV=/venv
RUN python3.9 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN  pip3 install -r requirements.txt
COPY . /code/
