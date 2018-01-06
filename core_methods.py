# Import syllable comparisons
# from file of {phonetic A}\tab{phonetic B}
def get_syllable_array(file_name):
	with open(file_name) as f:
		content = f.readlines()
	return [x.strip() for x in content]