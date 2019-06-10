FROM repo.xxx.com/base/elastalert-base:latest

COPY . /opt/elastalert/

USER elastalert

WORKDIR /opt/elastalert

CMD ["sh", "-c", "python -m elastalert.elastalert --verbose"]
