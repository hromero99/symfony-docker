FROM debian:stretch

RUN apt-get update && apt-get install -y  apache2 curl
RUN mkdir /var/log/symfony_logs
RUN sed -i '/Global configuration/a \
ServerName localhost \
' /etc/apache2/apache2.conf

EXPOSE 80 443

CMD apachectl  -D FOREGROUND -e info
