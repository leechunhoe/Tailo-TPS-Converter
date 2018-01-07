import sys
from stailo_hongim_converter import StailoHongimConverter

if len(sys.argv) == 2:
	filename = sys.argv[-1]
	StailoHongimConverter().convert_file_full(filename)
else:
	print "Please provide one input file name!"