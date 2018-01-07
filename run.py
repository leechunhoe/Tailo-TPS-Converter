import core_methods
from hongim_tailo_converter import HongimTailoConverter
hongim_tailo_converter = HongimTailoConverter()

result = hongim_tailo_converter.convert_file("input.txt")

print "Result:\n" + result

print "Please refer output.txt for result"

with open('output.txt', 'w') as output_file:
	output_file.truncate()
	output_file.write(result)
	output_file.close()