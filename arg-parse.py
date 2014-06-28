import argparse
import os
import sys

def parseArgs():
	parser = argparse.ArgumentParser(
		description = 'Rename png files to ordinal squence' 
			      'by last modified time.')
	parser.add_argument('-d', 
			    dest = 'directory')
	parser.add_argument('-p',
			    dest = 'prefix')
	args = parser.parse_args()
	print args
	
	if args.directory and not os.path.exists(args.directory):
		print('Error! directory is not found')
		sys.exit(1)
	return args

def main():
	parseArgs()

if __name__ == '__main__':
	main()
			    
