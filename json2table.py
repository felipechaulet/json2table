#!/usr/bin/env python
import getopt
from json2html import *
import webbrowser
import os

# Before running this script, runÇ pip install json2html

def convert_json(json_object, output_file):
    f = open(json_object, "r")
    content = f.read()
    out = open(output_file, "w+")
    out.write(json2html.convert(json=content))
    out.close()
    return out


def help():
    print("Usage: json2table.py \t-j file.json. -o output.html\n" +
                    "\t\t\t-j, --json [json formatted file]\n" +
                    "\t\t\t-o, --output [outputfile with the HTML table]"
    )
    sys.exit(2)


def main(argv):
    json_file = ''
    out_file = ''
    try:
        opts, args = getopt.getopt(argv, "h:j:o:", ["help=", "json=", "output="])
    except getopt.GetoptError:
        help()
    if not opts:
        help()
    if len(opts) != 2:
        help()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
        elif opt in ("-j", "--json"):
            json_file = arg
        elif opt in ("-o", "--output"):
            out_file = arg

    convert_json(json_file, out_file)
    url = "file://" + os.getcwd() + "/" + out_file
    webbrowser.open(url, new=2)


if _name__ == "__main__":
    main(sys.argv[1:])
