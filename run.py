import argparse
import os.path

from stailo_hongim_converter import StailoHongimConverter

parser = argparse.ArgumentParser(description='Convert between Tailo and TPS.')

parser.add_argument('-i', help='Input file')
parser.add_argument('-o', help='Output file, output.txt by default', default='output.txt')
parser.add_argument('--safe', help='Encode safe version of TPS', action='store_true')
parser.add_argument('--hanji', help='Get only hanji', action='store_true')
parser.add_argument('--hongim', help='Get only hongim', action='store_true')
parser.add_argument('--tailo', help='Get only tailo', action='store_true')
parser.add_argument('--no-convert', help='Not converting Tailo to TPS (To be used with --filter-out-hanji flag)', action='store_true')

args = parser.parse_args()

filename = args.i

if not args.i or not os.path.isfile(filename):
	print "Please provide input file name and make sure file exists.\ne.g. `python run.py -i input.txt`"
else:
	if args.hongim:
		result = StailoHongimConverter().convert_save_hongim_without_hanji(args.i, args.safe, args.o)
	elif args.hanji:
		result = StailoHongimConverter().convert_save_hanji(args.i, args.safe, args.o)
	else:
		result = StailoHongimConverter().save_tailo(args.i, args.safe, args.o)

	print "Conversion success!\n"
	print "Result to " + args.o + ":\n" + result + "\n"
