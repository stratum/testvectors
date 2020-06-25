from target import target_pb2

def get_new_target(address, target_id, credentials=None, timeout=None):
	tg = target_pb2.Target()
	tg.address = address
	tg.target_id = target_id
	if credentials is not None:
		tg.credentials = credentials
	if timeout is not None:
		tg.timeout = timeout
	return tg