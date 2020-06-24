from portmap import portmap_pb2

def get_new_portmap():
	return portmap_pb2.PortMap()

def add_new_entry(portmap, port_number, interface_name, port_type=None):
	entry = portmap.entries.add()
	entry.port_number = port_number
	entry.interface_name = interface_name
	if port_type is not None:
		entry.port_type = port_type
	else:
		entry.port_type = 0