FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
#RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf && pip install pipenv && pipenv install --system
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/