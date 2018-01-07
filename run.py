import core_methods
from hongim_tailo_converter import HongimTailoConverter
hongim_tailo_converter = HongimTailoConverter()

result = hongim_tailo_converter.convert_file("input.txt")

hanji_result = core_methods.get_hanji_from_file("input.txt")
tailo_result = core_methods.get_non_hanji_from_file("input.txt")

print "Please refer:"
print "output.txt for main result"
print "output_hanji.txt for hanji"
print "output_hongim.txt for hongim"
print "output_tailo.txt for tailo"

core_methods.write_to_output(result, "output.txt")
hongim_result = core_methods.get_hongim_from_file("output.txt")
core_methods.write_to_output(tailo_result, 'output_tailo.txt')
core_methods.write_to_output(hanji_result, 'output_hanji.txt')
core_methods.write_to_output(hongim_result, 'output_hongim.txt')