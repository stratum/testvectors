from portmap import portmap_pb2
import os, errno
import google.protobuf.text_format

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

# Writes portmap to <directory>/testvectors/portmap.pb.txt file
# If file_name is given then writes portmap to <directory>/testvectors/<file_name>
# If create_tv_sub_dir=false then writes portmap to <directory>
def write_to_file(portmap, directory, file_name=None, create_tv_sub_dir=True):
	if create_tv_sub_dir:
		directory = os.path.join(directory,"testvectors")
	if file_name is None:
		file_name = "portmap.pb.txt"
	elif not file_name.endswith(".pb.txt"):
		file_name = file_name + ".pb.txt"
	if not os.path.exists(directory):
		try:
			os.makedirs(directory)
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise
	abs_file_name = os.path.join(directory, file_name)
	with open(abs_file_name, "w") as f:
		f.write(google.protobuf.text_format.MessageToString(portmap))