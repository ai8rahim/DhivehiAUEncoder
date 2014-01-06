#!/usr/bin/python
"""
This Python script can be used to encode a text file with Dhivehi ASCII content and save as the equivalent Unicode version.

@author: ai8rahim
@contact: mr.ahmedibrahim@gmail.com
@copyright:
@license:
@requires: python version 2.6.6
@since: 20140106 (do not change)
@date: 20140106
@version: 0.1

"""

from os.path import exists

ascii_filename = raw_input("Enter input file: ");
unicode_filename = "unicode_" + ascii_filename

# Check if file exists
if not exists(ascii_filename):
	print "\nFile does not exist."
	exit(1)

# Open file to read
ascii_file = open(ascii_filename, "r")
ascii_content = ascii_file.read()

# Do the conversion
ascii_content = ascii_content.replace('h', u'\u0780')
ascii_content = ascii_content.replace('S', u'\u0781')
ascii_content = ascii_content.replace('n', u'\u0782')
ascii_content = ascii_content.replace('r', u'\u0783')
ascii_content = ascii_content.replace('b', u'\u0784')
ascii_content = ascii_content.replace('L', u'\u0785')
ascii_content = ascii_content.replace('k', u'\u0786')
ascii_content = ascii_content.replace('a', u'\u0787')
ascii_content = ascii_content.replace('v', u'\u0788')
ascii_content = ascii_content.replace('m', u'\u0789')
ascii_content = ascii_content.replace('f', u'\u078A')
ascii_content = ascii_content.replace('d', u'\u078B')
ascii_content = ascii_content.replace('t', u'\u078C')
ascii_content = ascii_content.replace('l', u'\u078D')
ascii_content = ascii_content.replace('g', u'\u078E')
ascii_content = ascii_content.replace('N', u'\u078F')
ascii_content = ascii_content.replace('s', u'\u0790')
ascii_content = ascii_content.replace('D', u'\u0791')
ascii_content = ascii_content.replace('z', u'\u0792')
ascii_content = ascii_content.replace('T', u'\u0793')
ascii_content = ascii_content.replace('y', u'\u0794')
ascii_content = ascii_content.replace('p', u'\u0795')
ascii_content = ascii_content.replace('j', u'\u0796')
ascii_content = ascii_content.replace('C', u'\u0797')
ascii_content = ascii_content.replace('X', u'\u0798')
ascii_content = ascii_content.replace('H', u'\u0799')
ascii_content = ascii_content.replace('K', u'\u079A')
ascii_content = ascii_content.replace('J', u'\u079B')
ascii_content = ascii_content.replace('R', u'\u079C')
ascii_content = ascii_content.replace('x', u'\u079D')
ascii_content = ascii_content.replace('B', u'\u079E')
ascii_content = ascii_content.replace('F', u'\u079F')
ascii_content = ascii_content.replace('Y', u'\u07A0')
ascii_content = ascii_content.replace('Z', u'\u07A1')
ascii_content = ascii_content.replace('A', u'\u07A2')
ascii_content = ascii_content.replace('G', u'\u07A3')
ascii_content = ascii_content.replace('q', u'\u07A4')
ascii_content = ascii_content.replace('V', u'\u07A5')
ascii_content = ascii_content.replace('w', u'\u07A6')
ascii_content = ascii_content.replace('W', u'\u07A7')
ascii_content = ascii_content.replace('i', u'\u07A8')
ascii_content = ascii_content.replace('I', u'\u07A9')
ascii_content = ascii_content.replace('u', u'\u07AA')
ascii_content = ascii_content.replace('U', u'\u07AB')
ascii_content = ascii_content.replace('e', u'\u07AC')
ascii_content = ascii_content.replace('E', u'\u07AD')
ascii_content = ascii_content.replace('o', u'\u07AE')
ascii_content = ascii_content.replace('O', u'\u07AF')
ascii_content = ascii_content.replace('c', u'\u07B0')

# reverse line direction
ascii_lines = ascii_content.split('\n')
unicode_content = ''
for line in ascii_lines:
	unicode_content += line[::-1] + '\n'

# save unicode content with utf-8 encoding
unicode_file = open(unicode_filename, "w")
unicode_file.write(unicode_content.encode('utf-8'))

ascii_file.close()
unicode_file.close()

