# Convert lines into array
def get_array_from_file(file_name):
	with open(file_name) as f:
		content = f.readlines()
	return [x.strip() for x in content]