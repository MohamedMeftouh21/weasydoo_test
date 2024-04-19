FROM odoo:16.0
USER root
RUN apt-get update || true
# RUN apt -y install python-pandas || true
RUN chmod 777 -R /home/