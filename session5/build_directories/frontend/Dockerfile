FROM registry.access.redhat.com/ubi9/httpd-24:latest
USER 0
RUN dnf install -y python3 python3-pip && \
  pip3 install --upgrade pip && \
  pip3 install mysql-connector-python
COPY files/app.py /var/www/cgi-bin/
COPY files/cgi.conf /etc/httpd/conf.d/
RUN chmod a+x /var/www/cgi-bin/app.py
USER 1001:0
