import re

# Convert lines into array
def get_array_from_file(file_name):
	with open(file_name) as f:
		content = f.readlines()
	return [x.strip() for x in content]

def write_to_output(content, file_name):
	with open(file_name, 'w') as output_file:
		output_file.truncate()
		output_file.write(content)
		output_file.close()

def get_hanji_from_file(file_name):
	input_text_array = get_array_from_file(file_name)
	result = ""
	for sentence in input_text_array:
		encoded_sentence = unicode(sentence, encoding="utf-8")
		if len(re.findall(ur'[\u4e00-\u9fff]+', encoded_sentence)) > 0:
			result += sentence + "\n"
	result = result.rstrip('\n')
	return result

def get_non_hanji_from_file(file_name):
	input_text_array = get_array_from_file(file_name)
	result = ""
	for sentence in input_text_array:
		encoded_sentence = unicode(sentence, encoding="utf-8")
		has_hanji = len(re.findall(ur'[\u4e00-\u9fff]+', encoded_sentence)) > 0
		if ~has_hanji and len(encoded_sentence) > 0:
			result += sentence + "\n"
	result = result.rstrip('\n')
	return result

def get_hongim_from_file(file_name):
	input_text_array = get_array_from_file(file_name)
	result = ""
	for sentence in input_text_array:
		encoded_sentence = unicode(sentence, encoding="utf-8")
		if len(re.findall(ur'[\u3100-\u31bf]+', encoded_sentence)) > 0:
			result += sentence + "\n"
	result = result.rstrip('\n')
	return result