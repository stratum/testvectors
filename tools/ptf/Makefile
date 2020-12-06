#
# Copyright 2020-present Open Networking Foundation
#
# SPDX-License-Identifier: Apache-2.0
#
TV_ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/../../)
IMAGE_NAME ?= stratumproject/testvectors:ptf
all: image

image:
	docker build -t ${IMAGE_NAME} \
		-f ${TV_ROOT}/tools/ptf/Dockerfile \
		${TV_ROOT}
