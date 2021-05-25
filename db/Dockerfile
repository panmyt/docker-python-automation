FROM mysql
EXPOSE 3306
WORKDIR /application
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3.7 -y
RUN apt-get install python3-pip -y
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install marshmallow-sqlalchemy
COPY . .
CMD ["python3","initdb.py"]



