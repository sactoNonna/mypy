"""
split and interactively page string ("") data
"""

def moretext(textbuf, numlines=50, numcols=80, file=""):
    if textbuf == '-h':
        print("\n\tUsage\t: moretext(textbuf, numlines, numcols, file)")
        print("\n\ttextbuf\t\t= text buffer name")
        print("\tnumlines\t= number of lines per display, default = 20")
        print("\tnumcols\t\t= number of columns per line, default = 60")
        print("\tfile\t\t= output file name to store the output")
        print("\n\tExample\t: moretext(open('test.txt').read(), 30, 50, file='out.txt')\n")
        return

    
    if (file != ""):
        try:
            fd = open(file, 'w')
            fd.write(textbuf)
            fd.close()
        except:
            print("File Write Error!\n")
            return 1
    else:
        lines = textbuf.splitlines()           # like split('\n') but no '' at end
        while lines:
            chunk = lines[:numlines]
            lines = lines[numlines:]
            for line in chunk:
                linecount = 0
                while line:
                    chars = line[:numcols]
                    line = line[numcols:]
                    print(chars)
                    linecount += 1
                    if line and (linecount == numlines):
                        linecount = 0
                        iforcol = input("Enter 'q' to quit: ".rjust(70))
                        if iforcol.lower() == 'q': return 'q'
            if lines:
                iforline = input("Enter 'q' to quit: ".rjust(70))
                if iforline.lower() == 'q': break
"""
split and interactively page list([]) data
"""

def morelist(listname, numlines=50, numcols=80, file="", newline=True):
    if listname == '-h':
        print("\n\tUsage\t: morelist(listname, numlines, numcols, file, newline)")
        print("\n\tlistname\t= list buffer name")
        print("\tnumlines\t= number of lines per display, default = 20")
        print("\tnumcols\t\t= number of columns per line, default = 60")
        print("\tfile\t\t= output file name to store the output")
        print("\tnewline\t= False if newline should not be added")
        print("\n\tExample\t: morelist(dir(str), 30, 50, file='out.txt', newline=False)\n")
        return

    #import os, sys
    #sys.path.insert(0, os.getcwd())
    from mymores import moretext
    
    s = ""
    for l in listname:
        s = s + str(l)
        if newline == True: s += '\n'

    if (file != ""):
        try:
            fd = open(file, 'w')
            fd.write(s)
            fd.close()
        except:
            print("File Write Error!\n")
            return 1
    else:    
        if moretext(s, numlines, numcols) == 'q': return 'q'
        return 0
"""
split and interactively page a file data
"""

def morefile(filename, numlines=50, numcols=80):
    if filename == "-h":
        print("\n\tUsage\t: morefile(filename, numlines, numcols)")
        print("\n\tfilename\t= name of the file (must be quoted) to be read")
        print("\tnumlines\t= number of lines per display, default = 20")
        print("\tnumcols\t\t= number of columns per line, default = 60")
        print("\n\tExample\t: morefile(('mymores.py'), 30, 50)\n")
        return

    #import os, sys
    #sys.path.insert(0, os.getcwd())
    from mymores import moretext
    moretext(open(str(filename)).read(), numlines, numcols)
        
"""
split and interactively page keys and values in a dictionary data
"""

def moredict(dictname, numlines=50, numcols=80, key=True, value=True):
    if dictname == "-h":
        print("\n\tUsage\t: moredict(dictname, numlines, numcols, key=True, value=True)")
        print("\n\tdictname\t= dictionary variable to be read")
        print("\tnumlines\t= number of lines per display, default = 20")
        print("\tnumcols\t\t= number of columns per line, default = 60")
        print("\tkey\t\t= True to display dict_keys(), False otherwise")
        print("\tvalue\t\t= True to display dict_values(), False otherwise")
        print("\n\tExample\t: moredict(sys.modules, 30, 50, key=False, value=True)\n")
        return

    lkeys = list(dictname.keys())
    lvalues = list(dictname.values())

    #import os, sys
    #sys.path.insert(0, os.getcwd())    
    from mymores import morelist
    if key == False and value == False: return
    elif key == True and value == True:
        lkeysvalues = []
        while lkeys:
            lkeysvalues.append(lkeys[0] + '\n\t' + lvalues[0])
            lkeys = lkeys[1:]
            lvalues = lvalues[1:]
        morelist(lkeysvalues, numlines, numcols)
    elif value == True: morelist(lvalues, numlines, numcols)
    else: morelist(lkeys, numlines, numcols)


if __name__ == '__main__':
    pass
