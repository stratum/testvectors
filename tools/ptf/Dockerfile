#
# Copyright 2020-present Open Networking Foundation
#
# SPDX-License-Identifier: Apache-2.0
#
# Docker image to run PTF-based tests

ARG GRPC_VER=1.26
ARG PROTOBUF_VER=3.12

FROM python:2.7.13 as proto-deps

ARG GRPC_VER

ENV BUILD_DEPS \
    autoconf \
    automake \
    ca-certificates \
    curl \
    g++ \
    net-tools
RUN apt-get update
RUN apt-get install -y $BUILD_DEPS
RUN pip install grpcio-tools==$GRPC_VER

RUN mkdir -p /output
RUN echo "Building gnmi proto"
RUN git clone https://github.com/openconfig/gnmi.git /tmp/github.com/openconfig/gnmi
WORKDIR /tmp/github.com/openconfig/gnmi/proto
RUN sed -i "s|github.com/openconfig/gnmi/proto/gnmi_ext|gnmi_ext|g" /tmp/github.com/openconfig/gnmi/proto/gnmi/gnmi.proto

RUN python -m grpc_tools.protoc -I=/tmp/github.com/openconfig/gnmi/proto --python_out=/output gnmi_ext/gnmi_ext.proto
RUN python -m grpc_tools.protoc -I=/tmp/github.com/openconfig/gnmi/proto --python_out=/output --grpc_python_out=/output gnmi/gnmi.proto

RUN echo "Building p4runtime proto"
RUN git clone https://github.com/p4lang/p4runtime.git /tmp/github.com/p4lang/p4runtime
RUN git clone https://github.com/googleapis/googleapis /tmp/github.com/googleapis/googleapis
WORKDIR /tmp/github.com/p4lang/p4runtime/proto
ENV PROTOS="\
/tmp/github.com/p4lang/p4runtime/proto/p4/v1/p4data.proto \
/tmp/github.com/p4lang/p4runtime/proto/p4/v1/p4runtime.proto \
/tmp/github.com/p4lang/p4runtime/proto/p4/config/v1/p4info.proto \
/tmp/github.com/p4lang/p4runtime/proto/p4/config/v1/p4types.proto \
/tmp/github.com/googleapis/googleapis/google/rpc/status.proto \
/tmp/github.com/googleapis/googleapis/google/rpc/code.proto"
RUN python -m grpc_tools.protoc -I=/tmp/github.com/p4lang/p4runtime/proto:/tmp/github.com/googleapis/googleapis --python_out=/output --grpc_python_out=/output $PROTOS

RUN echo "Building testvector proto"
RUN git clone https://github.com/stratum/testvectors /tmp/github.com/stratum/testvectors
WORKDIR /tmp/github.com/stratum/testvectors/proto
RUN git pull
RUN python -m grpc_tools.protoc -I=.:/tmp/github.com/openconfig/gnmi/proto:/tmp/github.com/p4lang/p4runtime/proto:/tmp/github.com/googleapis/googleapis --python_out=/output testvector/tv.proto
RUN python -m grpc_tools.protoc -I=. --python_out=/output target/target.proto
RUN python -m grpc_tools.protoc -I=. --python_out=/output portmap/portmap.proto
RUN cp /tmp/github.com/stratum/testvectors/utils/python/tvutils.py /output/testvector/tvutils.py
RUN cp /tmp/github.com/stratum/testvectors/utils/python/pmutils.py /output/portmap/pmutils.py
RUN cp /tmp/github.com/stratum/testvectors/utils/python/targetutils.py /output/target/targetutils.py

RUN touch /output/gnmi_ext/__init__.py
RUN touch /output/gnmi/__init__.py
RUN touch /output/google/__init__.py
RUN touch /output/google/rpc/__init__.py
RUN touch /output/__init__.py
RUN touch /output/p4/__init__.py
RUN touch /output/p4/config/__init__.py
RUN touch /output/p4/config/v1/__init__.py
RUN touch /output/p4/v1/__init__.py
RUN touch /output/testvector/__init__.py
RUN touch /output/target/__init__.py
RUN touch /output/portmap/__init__.py

FROM bitnami/minideb:stretch as ptf-deps

ARG GRPC_VER
ARG PROTOBUF_VER

ENV RUNTIME_DEPS \
	python \
	python-pip \
	python-setuptools \
    git

ENV PIP_DEPS \
    git+https://github.com/p4lang/scapy-vxlan \
    git+https://github.com/p4lang/ptf \
    protobuf==$PROTOBUF_VER \
    grpcio==$GRPC_VER

RUN install_packages $RUNTIME_DEPS
RUN pip install --no-cache-dir --root /python_output $PIP_DEPS


FROM bitnami/minideb:stretch

#FIXME: Remove tcpdump, netbase after removing ptf
ENV RUNTIME_DEPS \
    make \
    net-tools \
    python \
    python-setuptools \
    iproute2 \
    tcpdump \
    netbase

RUN install_packages $RUNTIME_DEPS

COPY --from=proto-deps /output /usr/lib/python2.7/dist-packages
COPY --from=ptf-deps /python_output /
RUN ldconfig

ENTRYPOINT []
