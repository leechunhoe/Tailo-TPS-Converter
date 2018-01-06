import core_methods
from hongim_tailo_converter import HongimTailoConverter
hongim_tailo_converter = HongimTailoConverter()

result = hongim_tailo_converter.convert_file("input.txt")

print "Output:\n" + result