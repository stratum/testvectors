# Start from golang v1.12.7 base image
FROM golang:1.12.7

RUN apt-get update && \
    apt-get install unzip

RUN curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v3.9.1/protoc-3.9.1-linux-x86_64.zip && \
    unzip -o protoc-3.9.1-linux-x86_64.zip -d /usr/local bin/protoc && \
    unzip -o protoc-3.9.1-linux-x86_64.zip -d /usr/local include/* && \
    rm -rf protoc-3.9.1-linux-x86_64.zip

RUN go get -u github.com/golang/protobuf/protoc-gen-go

RUN git clone --branch master https://github.com/googleapis/googleapis /go/src/github.com/googleapis/googleapis
RUN git clone --branch master https://github.com/openconfig/gnmi /go/src/github.com/openconfig/gnmi
RUN git clone --branch master https://github.com/abhilashendurthi/p4runtime /go/src/github.com/abhilashendurthi/p4runtime

WORKDIR /root

ENTRYPOINT [ "/bin/bash" ]