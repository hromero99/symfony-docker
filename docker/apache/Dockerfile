FROM debian:stretch

RUN apt-get update && apt-get install -y  apache2 curl
RUN mkdir /var/log/symfony_logs
RUN sed -i '/Global configuration/a \
ServerName localhost \
' /etc/apache2/apache2.conf

RUN a2enmod proxy_fcgi ssl rewrite proxy proxy_balancer proxy_http proxy_ajp

EXPOSE 80 443

CMD apachectl  -D FOREGROUND -e info
