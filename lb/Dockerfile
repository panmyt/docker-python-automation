FROM nginx
WORKDIR /application
RUN apt-get update && apt-get upgrade -y
COPY nginx.conf /etc/nginx/
EXPOSE 80
COPY . .
#RUN chmod +x wrapper.sh
#CMD ["./wrapper.sh"]

