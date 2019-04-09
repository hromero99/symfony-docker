FROM php:7.2.3-fpm
WORKDIR /var/www/html/
RUN curl -L https://github.com/composer/composer/releases/download/1.8.3/composer.phar -o /usr/local/bin/composer
RUN chmod 755 /usr/local/bin/composer
COPY php.ini /etc/php/7.2.3/php.ini
COPY php-fpm-pool.conf /etc/php/7.2.3/pool.d/www.conf
RUN groupadd dev -g 999
RUN useradd dev -g dev -d /home/dev -m
EXPOSE 9000
CMD ["php-fpm"]
