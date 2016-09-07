#!/usr/bin/env python

import sys
import json
from cli import *

if __name__ == "__main__":

	length = len(sys.argv)

	if length == 1:
		print '\n Input Requires an option. \n\n Available Options: '
		print ' - crc\n - runts\n - coll\n'
	else:
		args = sys.argv
		stats = json.loads(clid('show interface'))

		if args[1] == 'help':
			print '\n Available Options: ' + '\n - crc ' + '\n - runts\n - coll\n'
		else:
			if not (args[1] == 'crc' or args[1] == 'runts' or args[1] == 'coll'):
				print '\nInvalid Option'
				print 'Input Requres a Valid Option'
				print '\n Available Options: ' + '\n - crc ' + '\n - runts\n - coll\n'
			else:
				for each in stats['TABLE_interface']['ROW_interface']:
					if each['interface'].startswith('Eth'):
						delta = 15 - len(each['interface'])
						spaces = delta * ' '
						if length == 2:
							occurences = 0
						elif length == 3:
							occurences = args[2]
						if args[1] == 'crc' and each['eth_crc'] >= occurences:
							print each['interface'] + ': ' + spaces + 'CRC errors: ' + each['eth_crc']
						elif args[1] == 'runts' and each['eth_runts'] >= occurences:
							print each['interface'] + ': ' + spaces + 'runts: ' + each['eth_runts']
						elif args[1] == 'coll' and each['eth_coll'] >= occurences:
							print each['interface'] + ': ' + spaces + 'collisions: ' + each['eth_coll']
