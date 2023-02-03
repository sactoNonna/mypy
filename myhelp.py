"""
Note: 
These two class objects were taken from Programming Python by Mark Lutz.
---
File-like objects that are standard output text in a string and provide
standard input text from a string; redirect runs a passed-in function
with its output and input streams reset to these file-like class objects;
"""

import sys, subprocess

class Output:
    def __init__(self):
        self.text = ''
    def write(self, string):
        self.text += string
    def writeline(self, lines):
        for line in lines: self.write(line)

class Input:
    def __init__(self, input=''):
        self.text = input
    def read(self, size=None):
        if size == None:
            res = self.text
            self.text = ''
        else:
            res = self.text[:size]
            self.text = self.text[size:]
        return res
    def readline(self):
        eoln = self.text.find('\n')
        if eoln == -1:
            res = self.text
            self.text = ''
        else:
            res = self.text[:eoln+1]
            self.text = self.text[eoln+1:]
        return res

def myhelp(harg, numlines=50, numcols=80, file=""):
    if harg == "-h":
        print("\n\tUsage\t: myhelp(helparg, numlines, numcols, file)")
        print("\n\thelparg\t= arg as for help(arg)")
        print("\tnumlines\t= number of lines per display, default = 20")
        print("\tnumcols\t\t= number of columns per line, default = 60")
        print("\tfile\t\t= output file name to store the output")
        print("\n\tExample: myhelp(print, 40, 50, file='print.txt')\n")
        return

    savestreams = sys.stdout
    sys.stdout = Output()
    result = '?'
    output = '$'
    try:
        result = help(harg)
        output = sys.stdout.text
    finally:
        sys.stdout = savestreams
        if (result != None): print('Result Failed: ', result, '\n')
    #return (output)
    from mymores import moretext
    if (file == ""): moretext(output, numlines, numcols)
    else:
        fd = open(file, 'w')
        if (fd.write(output) != len(output)): print('file write error!')
        fd.close()
        
