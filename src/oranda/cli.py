# MIT License
#
# Copyright (c) 2023 Clivern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import click
import logging, json, sys
from oranda import __version__

main = click.Group(help="🐺 A Lightweight and Flexible Ansible Command Line Tool")

@main.command("key", help="Get key from JSON object")
@click.option("-i", "--input", "infile", type=click.File(), default=sys.stdin, help="Input file name")
@click.option("-o", "--output", "outfile", type=click.File("w"), default=sys.stdout, help="Output file name")
@click.option("-k", "--key", required=True, help="Sorting key")
def main_get_key(infile, outfile, key):
    data = json.load(infile)
    data = data[key]
    json.dump(data, outfile)

@main.command("list-key", help="Get key from JSON list objects")
@click.option("-i", "--input", "infile", type=click.File(), default=sys.stdin, help="Input file name")
@click.option("-o", "--output", "outfile", type=click.File("w"), default=sys.stdout, help="Output file name")
@click.option("-k", "--key", required=True, help="Sorting key")
def main_get_list_key(infile, outfile, key):
    data = json.load(infile)
    data = [obj[key] for obj in data if key in obj]
    json.dump(data, outfile)


if __name__ == "__main__":
    exit(main())
