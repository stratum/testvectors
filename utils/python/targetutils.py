from target import target_pb2
import os, errno
import google.protobuf.text_format

def get_new_target(address, target_id, credentials=None, timeout=None):
	tg = target_pb2.Target()
	tg.address = address
	tg.target_id = target_id
	if credentials is not None:
		tg.credentials = credentials
	if timeout is not None:
		tg.timeout = timeout
	return tg

# Writes target to <directory>/testvectors/target.pb.txt file
# If file_name is given then writes target to <directory>/testvectors/<file_name>
# If create_tv_sub_dir=false then writes target to <directory>
def write_to_file(target, directory, file_name=None, create_tv_sub_dir=True):
	if create_tv_sub_dir:
		directory = os.path.join(directory,"testvectors")
	if file_name is None:
		file_name = "target.pb.txt"
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
		f.write(google.protobuf.text_format.MessageToString(target))