
# Copyright (c) 2007-2009 PediaPress GmbH
# See README.rst for additional licensing information.

"""main programs - installed via setuptools' entry_points"""

import optparse
import os

def buildcdb():
    parser = optparse.OptionParser(usage="%prog --input XMLDUMP --output OUTPUT [--ignore-redirects]")
    parser.add_option("-i", "--input", help="input file")
    parser.add_option("-o", "--output", help="write output to OUTPUT")
    parser.add_option("-r", "--ignore-redirects", help="skip redirect pages in input file", action="store_true", dest="redirects")
    options, args = parser.parse_args()
    
    if args:
        parser.error("too many arguments.")

    
    input = options.input
    output = options.output
    redirects = options.redirects

    if not (input and output):
        parser.error("missing argument.")
        
    from mwlib.cdb import cdbwiki

    cdbwiki.BuildWiki(input, output, ignore_redirects=redirects)()
    open(os.path.join(output, "wikiconf.txt"), "w").write("""
[wiki]
type = nucdb
path = %s
lang = en
""" % (os.path.abspath(output),))
