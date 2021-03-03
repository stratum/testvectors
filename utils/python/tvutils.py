# Copyright 2019-present Open Networking Foundation
# SPDX-License-Identifier: Apache-2.0

from testvector import tv_pb2
import os, errno
import google.protobuf.text_format
from ptf.mask import Mask


def get_new_testvector():
	return tv_pb2.TestVector()

def get_new_testcase(testvector, tc_name=None):
	tc = testvector.test_cases.add()
	if tc_name is not None:
		tc.test_case_id = tc_name
	return tc

def add_write_operation(testcase, req,resp=None):
	action_group=testcase.action_groups.add()
	action=action_group.sequential_action_group.actions.add()
	action.control_plane_operation.write_operation.p4_write_request.CopyFrom(req)
	if resp is not None:
		action.control_plane_operation.write_operation.p4_write_response.CopyFrom(resp)

def add_read_expectation(testcase, req, resp=None):
	expectation = testcase.expectations.add()
	expectation.control_plane_expectation.read_expectation.p4_read_request.CopyFrom(req)
	if resp is not None:
		for r in resp:
			expectation.control_plane_expectation.read_expectation.p4_read_responses.add().CopyFrom(r)

def add_traffic_stimulus(testcase, port, pkt):
	action_group=testcase.action_groups.add()
	action=action_group.sequential_action_group.actions.add()
	packet = action.data_plane_stimulus.traffic_stimulus.packets.add()
	if isinstance(pkt, Mask):
		packet.payload = bytes(pkt.exp_pkt)
	else:
		packet.payload = bytes(pkt)
	action.data_plane_stimulus.traffic_stimulus.port=port

def add_traffic_expectation(testcase, ports, pkt):
	expectation = testcase.expectations.add()
	packet = expectation.data_plane_expectation.traffic_expectation.packets.add()
	if isinstance(pkt, Mask):
		packet.payload = bytes(pkt.exp_pkt)
	else:
		packet.payload = bytes(pkt)
	for port in ports:
		expectation.data_plane_expectation.traffic_expectation.ports.append(port)

def add_packet_out_operation(testcase, packet, count=1):
	action_group=testcase.action_groups.add()
	action=action_group.sequential_action_group.actions.add()
	action.control_plane_operation.packet_out_operation.p4_packet_out.CopyFrom(packet)
	action.control_plane_operation.packet_out_operation.num_of_packets = count

def add_packet_in_expectation(testcase, packet):
	expectation = testcase.expectations.add()
	expectation.control_plane_expectation.packet_in_expectation.p4_packet_in.CopyFrom(packet)

def add_pipeline_config_operation(testcase, req, resp=None):
	action_group=testcase.action_groups.add()
	action=action_group.sequential_action_group.actions.add()
	action.control_plane_operation.pipeline_config_operation.p4_set_pipeline_config_request.CopyFrom(req)
	if resp is not None:
		action.control_plane_operation.pipeline_config_operation.p4_set_pipeline_config_response.CopyFrom(resp)

# Writes given testvector to file under <directory>/testvectors directory
# If create_tv_sub_dir=False, then file is created under <directory> directory
def write_to_file(tv, directory, file_name, create_tv_sub_dir=True):
	if create_tv_sub_dir:
		directory = os.path.join(directory,"testvectors")
	if not file_name.endswith(".pb.txt"):
		file_name = file_name + ".pb.txt"
	if not os.path.exists(directory):
		try:
			os.makedirs(directory)
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise
	abs_file_name = os.path.join(directory, file_name)
	with open(abs_file_name, "w") as f:
		f.write(google.protobuf.text_format.MessageToString(tv))

# Writes given list of testvectors to files under <base_dir>/testvectors/<base_file_name> directory
# If create_tv_sub_dir=False, then file is created under <base_dir>/<base_file_name> directory
def write_tv_list_to_files(tv_list, base_dir, base_file_name, create_tv_sub_dir=True):
	if create_tv_sub_dir:
		directory = os.path.join(base_dir,"testvectors")
	directory = os.path.join(directory,base_file_name)
	for i in range(len(tv_list)):
		file_name = base_file_name + str(i)
		write_to_file(tv_list[i], directory, file_name, create_tv_sub_dir=False)
