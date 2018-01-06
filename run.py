import core_methods
from hongim_tailo_converter import HongimTailoConverter

# Get samples
sample_text = open("sample", "r").read()
sample_simple_text = open("sample_simple", "r").read()

hongim_tailo_converter = HongimTailoConverter()

hongim = hongim_tailo_converter.convert(sample_simple_text)

print "hongim: " + hongim