FROM python:3.7
WORKDIR /application
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3-pip -y
RUN apt-get install redis-server -y
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install marshmallow-sqlalchemy
EXPOSE 5000
EXPOSE 6379
COPY . .
RUN chmod +x wrapper.sh
CMD ["./wrapper.sh"]

