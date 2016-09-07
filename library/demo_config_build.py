#!/usr/bin/env python

from jinja2 import Template
from jinja2 import Environment, PackageLoader
import yaml
from sys import argv

if __name__ == "__main__":
	
	length = len(argv)
	template, template_vars = False, False
	if length == 3:

		for each in argv[1:]:
			if '.yml' in each:
				template_vars = each
			elif '.j2' in each:
				template = each
			else:
				print 'Incorrect file extension.  Use .yml and .j2'	

		if template and template_vars:
			imported_vars = yaml.load(open(template_vars).read())
			config_template = Template(open(template).read())
			print config_template.render(imported_vars)
	
	else:
		print 'Input requires two arguments.'
		print '    (1) YAML File (.yml)'
		print '    (2) Template File (.j2)'
		print 'Fix & Re-run'

