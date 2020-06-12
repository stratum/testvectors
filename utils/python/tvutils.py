# Copyright 2019-present Open Networking Foundation
# SPDX-License-Identifier: Apache-2.0

from testvector import tv_pb2


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
	expectation.control_plane_expectation.read_operation.p4_read_request.CopyFrom(req)

def add_traffic_stimulus(testcase, port, pkt):
	action_group=testcase.action_groups.add()
	action=action_group.sequential_action_group.actions.add()
	packet = action.data_plane_stimulus.traffic_stimulus.packets.add()
	packet.payload = str(pkt)
	action.data_plane_stimulus.traffic_stimulus.port=port

def add_traffic_expectation(testcase, ports, pkt):
	expectation = testcase.expectations.add()
	packet = expectation.data_plane_expectation.traffic_expectation.packets.add()
	packet.payload = str(pkt)
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
