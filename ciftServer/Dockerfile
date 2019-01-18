FROM "tensorflow/tensorflow"

RUN pip install requests
RUN pip install flask
RUN pip install flask_restful
RUN pip install redis

EXPOSE 8080

ADD cift_server /notebook/cift_server
WORKDIR /notebook/cift_server
CMD ["/usr/bin/python", "ciftServer.py"]
