#!/bin/sh

proto_imports=".:${GOPATH}/src/github.com/googleapis/googleapis:${GOPATH}/src/github.com/openconfig/gnmi/proto:${GOPATH}/src/github.com/p4lang/p4runtime/proto/:${GOPATH}/src"

protoc -I=$proto_imports --go_out=plugins=grpc:. testvector/*.proto
protoc -I=$proto_imports --go_out=plugins=grpc:. target/*.proto
protoc -I=$proto_imports --go_out=plugins=grpc:. portmap/*.proto
