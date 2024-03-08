# StrawberryPieServer

To run server:
gunicorn -c gunicorn_config.py run:app

To install & update DUC:  (https://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client)

- login as root (sudo su -)
- run the following commands to install:
  - cd /usr/local/src
  - wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
  - tar xzf noip-duc-linux.tar.gz
  - cd noip-2.1.9-1
  - make
  - make install
- to configure:
  - /usr/local/bin/noip2 -C
  - /usr/local/bin/noip2

To get SSL certificate: sudo certbot renew --nginx

Expiration dates:
HTTPS Certificate: Jun 6 2024
DDNS: Jun 5 2024
