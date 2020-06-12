#!/bin/sh

proto_imports=".:${GOPATH}/src/github.com/googleapis/googleapis:${GOPATH}/src/github.com/openconfig/gnmi/proto:${GOPATH}/src/github.com/p4lang/p4runtime/proto/:${GOPATH}/src"

protoc -I=$proto_imports --go_out=plugins=grpc:. --go_opt=paths=source_relative testvector/*.proto
protoc -I=$proto_imports --go_out=plugins=grpc:. --go_opt=paths=source_relative target/*.proto
protoc -I=$proto_imports --go_out=plugins=grpc:. --go_opt=paths=source_relative portmap/*.proto
