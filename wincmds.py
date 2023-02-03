"""
    Implement Windows internal commands my way for IDLE
"""

import os
from mymores import moretext, morelist

#cd
def wcd(cdarg='-h', numlines=50, numcols=80):
    if cdarg == "-h":
        print("\n\tUsage  \t: wcd(cdarg)")
        print("\n\tExample\t: wcd('c:\\\\users')\n")
    elif cdarg == "":
        print(os.getcwd())
    else:
        os.chdir(cdarg)
        print(os.getcwd())
        
#diff - Since this is not a DOS internal command, won't rename it as wdiff
# Compare two files and store the difference in "diff.txt" file
def diff(file1, file2):
    import difflib
    f_out = open("diff.txt", "w")
    for line in difflib.unified_diff(open(file1).readlines(), open(file2).readlines(), fromfile=file1, tofile=file2, lineterm=''):
        print(line, file=f_out, end='')

#differ - Since this is not a DOS intenal command, won't rename it as wdiffer
# Use Python's differ module to compare two files and store the difference in "differ.txt" file
def differ(file1, file2):
    from difflib import Differ
    differ = Differ()
    f_out = open("differ.txt", "w")
    for line in differ.compare(open(file1).readlines(), open(file2).readlines()):
        print(line, file=f_out, end='')
        
# dir
def wdir(dirarg='-h', numlines=50, numcols=80):
    if dirarg == "-h":
        print("\n  Usage: wdir(dirarg, numlines, numcols)")
        print("\n  dirarg\t= path to display (must be quoted)")
        print("  numlines\t= number of lines per display, default = 50")
        print("  numcols\t= number of columns per line, default = 80")
        print("  Example\t: wdir('\\\\windows', 500, 80)")
        print("  For a path with spaces, use the following format:")
        print("    wdir(\r'\"C:\\Program Files (x86)\Microsoft Visual Studio\\shared\"\')")
    else:
        dircmd = 'dir' + ' ' + str(dirarg)
        moretext(os.popen(dircmd).read(), numlines, numcols)
        
#del
def wdel(delarg='-h', numlines=50, numcols=80):
    if delarg == "-h":
        print("\n\tUsage\t: wdel(delarg)")
        print("\n\tExample\t: wdel('sample.txt')\n")
        return
    
    delcmd = 'del' + ' ' + str(delarg)
    os.system(delcmd)
    return

#find
def wfind(option='', findstr='-h', rootpath='.', ftype='.py', numlines=50, numcols=80):
    if findstr == "-h":
        print("\n  Usage  : wfind('', 'findstr', 'filename', numlines, numcols), or")
        print("           wfind('-r', 'findstr', 'rootpath', 'filetype', (int)numlines, (int)numcols)")
        print("  Example: wfind('', '\"dir-str\" *.txt')")
        print("  Example: wfind('-r', 'Template', '.', '.py')")
        return

    if option=='':
        findcmd = 'find' + ' \"' + str(findstr) + '\" ' + str(rootpath)
        moretext(os.popen(findcmd).read(), numlines, numcols)
        return
    else:    # add recursive search
        matches = []
        for (dirname, dirshere, fileshere) in os.walk(rootpath):
            for filename in fileshere:
                if filename.endswith(ftype):
                    pathname = os.path.join(dirname, filename)
                    if findstr in open(pathname).read():
                        matches.append(pathname)
        morelist(matches, numlines, numcols)
        
# ren
def wren(cmdstring='-h'):
    if cmdstring == "-h":
        print("\n\tUsage\t: wren(cmdstring)")
        print("\n\tExample\t: wren('test.txt testtest.txt')\n")
        return

    rencmd = 'ren' + ' ' + str(cmdstring)
    os.system(rencmd)
    return
        
#   type -
def wtype(cmdstring='-h', numlines=50, numcols=80):
    if cmdstring == "-h":
        print("\n\tUsage\t: wtype(cmdstring, numlines, numcols)")
        print("\n\tcmdstring\t= params for DOS 'ren' cmd(must be quoted)")
        print("\tnumlines\t= number of lines per display, default = 50")
        print("\tnumcols\t\t= number of columns per line, default = 80")
        print("\n\tExample\t: wtype('test.txt', 500, 80)\n")
        return
    
    typecmd = 'type' + ' ' + str(cmdstring)
    moretext(os.popen(typecmd).read(), numlines, numcols)
    return

if __name__ == '__main__':
    import wincmds
    from mymores import moretext

    l = list(wincmds.__dict__)
    b = dir(__builtins__)
    s = ""
    for key in l:
        if ((key == 'os') or \
           (key =='sys') or \
           (key in b) or    \
           key.startswith('__')): pass
        else:
           s += key + ', '
    print("\nEmulatd DOS command list:\n\t", end='')
    moretext(s[:-2])
