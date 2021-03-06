import sys

keepgoin = True

def add_(operation, line):
    if(line[line.index(operation) + len(operation) + 1:line.index(",")] in programvars):
        if(ops[2] in line[line.index(operation) + len(operation) + 1:line.index(";")] and ops[3] in line[line.index(operation) + len(operation) + 1:line.index(";")]):
            if(line[line.index("/") + 1:line.index("%")] in programvars):
                try:
                    programvars[line[line.index(operation) + len(operation) + 1:line.index(",")]] += programvars[line[line.index("/") + 1:line.index("%")]]
                except TypeError:
                    print "\nError in expression ADD, two variables must have the same type!\nif you want a number use: num <var>;\nif you want a string use: str <var>\nbefore using that expression\n"
            else:
                print "\nI couldn't find that variable you are looking for\n"
        else:
            try:
                programvars[line[line.index(operation) + len(operation) + 1:line.index(",")]] += int(line[line.index(",") + 1:line.index(";")])
            except TypeError:
                print "\nError in expression ADD, two arguments must be numbers!\ntry: num <var>; before using that expression\n" # put line number here

def sub_(operation, line):
    if(line[line.index(operation) + len(operation) + 1:line.index(",")] in programvars):
        if(ops[2] in line[line.index(operation) + len(operation) + 1:line.index(";")] and ops[3] in line[line.index(operation) + len(operation) + 1:line.index(";")]):
            if(line[line.index("/") + 1:line.index("%")] in programvars):
                try:
                    programvars[line[line.index(operation) + len(operation) + 1:line.index(",")]] -= programvars[line[line.index("/") + 1:line.index("%")]]
                except TypeError:
                    print "\nError in expression SUB, two variables must have the same type!\nif you want a number use: num <var>;\nif you want a string use: str <var>\nbefore using that expression\n"
            else:
                print "\nI couldn't find that variable you are looking for\n"
        else:
            try:
                programvars[line[line.index(operation) + len(operation) + 1:line.index(",")]] -= int(line[line.index(",") + 1:line.index(";")])
            except TypeError:
                print "\nError in expression SUB, two arguments must be numbers!\ntry: num <var>; before using that expression\n" # put line number here

def mul_(operation, line):
    if(line[line.index(operation) + len(operation) + 1:line.index(",")] in programvars):
        if(ops[2] in line[line.index(operation) + len(operation) + 1:line.index(";")] and ops[3] in line[line.index(operation) + len(operation) + 1:line.index(";")]):
            if(line[line.index("/") + 1:line.index("%")] in programvars):
                try:
                    programvars[line[line.index(operation) + len(operation) + 1:line.index(",")]] *= programvars[line[line.index("/") + 1:line.index("%")]]
                except TypeError:
                    print "\nError in expression MUL, two variables must have the same type!\nif you want a number use: num <var>;\nif you want a string use: str <var>\nbefore using that expression\n"
            else:
                print "\nI couldn't find that variable you are looking for\n"
        else:
            try:
                programvars[line[line.index(operation) + len(operation) + 1:line.index(",")]] *= int(line[line.index(",") + 1:line.index(";")])
            except TypeError:
                print "\nError in expression MUL, two arguments must be numbers!\ntry: num <var>; before using that expression\n" # put line number here

def div_(operation, line):
    if(line[line.index(operation) + len(operation) + 1:line.index(",")] in programvars):
        if(ops[2] in line[line.index(operation) + len(operation) + 1:line.index(";")] and ops[3] in line[line.index(operation) + len(operation) + 1:line.index(";")]):
            if(line[line.index("/") + 1:line.index("%")] in programvars):
                try:
                    programvars[line[line.index(operation) + len(operation) + 1:line.index(",")]] /= float(programvars[line[line.index("/") + 1:line.index("%")]])
                except TypeError:
                    print "\nError in expression DIV, two variables must have the same type!\nif you want a number use: num <var>;\nif you want a string use: str <var>\nbefore using that expression\n"
            else:
                print "\nI couldn't find that variable you are looking for\n"
        else:
            try:
                programvars[line[line.index(operation) + len(operation) + 1:line.index(",")]] /= float(line[line.index(",") + 1:line.index(";")])
            except TypeError:
                print "\nError in expression DIV, two arguments must be numbers!\ntry: num <var>; before using that expression\n" # put line number here
            except ZeroDivisionError:
                print "\nDont divide by 0...\n"

def mod_(operation, line):
    if(line[line.index(operation) + len(operation) + 1:line.index(",")] in programvars):
        if(ops[2] in line[line.index(operation) + len(operation) + 1:line.index(";")] and ops[3] in line[line.index(operation) + len(operation) + 1:line.index(";")]):
            if(line[line.index("/") + 1:line.index("%")] in programvars):
                try:
                    programvars[line[line.index(operation) + len(operation) + 1:line.index(",")]] %= programvars[line[line.index("/") + 1:line.index("%")]]
                except TypeError:
                    print "\nError in expression MOD, two variables must have the same type!\nif you want a number use: num <var>;\nif you want a string use: str <var>\nbefore using that expression\n"
            else:
                print "\nI couldn't find that variable you are looking for\n"
        else:
            try:
                programvars[line[line.index(operation) + len(operation) + 1:line.index(",")]] %= int(line[line.index(",") + 1:line.index(";")])
            except TypeError:
                print "\nError in expression MOD, two arguments must be numbers!\ntry: num <var>; before using that expression\n" # put line number here

def pow_(operation, line):
    if(line[line.index(operation) + len(operation) + 1:line.index(",")] in programvars):
        if(ops[2] in line[line.index(operation) + len(operation) + 1:line.index(";")] and ops[3] in line[line.index(operation) + len(operation) + 1:line.index(";")]):
            if(line[line.index("/") + 1:line.index("%")] in programvars):
                try:
                    programvars[line[line.index(operation) + len(operation) + 1:line.index(",")]] **= programvars[line[line.index("/") + 1:line.index("%")]]
                except TypeError:
                    print "\nError in expression POW, two variables must have the same type!\nif you want a number use: num <var>;\nif you want a string use: str <var>\nbefore using that expression\n"
            else:
                print "\nI couldn't find that variable you are looking for\n"
        else:
            try:
                programvars[line[line.index(operation) + len(operation) + 1:line.index(",")]] **= int(line[line.index(",") + 1:line.index(";")])
            except TypeError:
                print "\nError in expression POW, two arguments must be numbers!\ntry: num <var>; before using that expression\n" # put line number here

def equ_(op,line):
    global keepgoin
    if line[line.index(keyw[3]) + len(keyw[3]) + 1:line.index(comp[0]) - 1] in programvars:
        if("/" in line and "%" in line and line[line.index("/") + 1:line.index("%")] in programvars):
            if(programvars[line[line.index(keyw[3]) + len(keyw[3]) + 1:line.index(comp[0]) - 1]] == programvars[line[line.index("/") + 1:line.index("%")]]):
                flags["equality"] = True
                flags["non-equality"] = False
            else:
                flags["non-equality"] = True
                flags["equality"] = False
                keepgoin = False
def let_(op,line):
    global keepgoin
    if line[line.index(keyw[3]) + len(keyw[3]) + 1:line.index(comp[1]) - 1] in programvars:
        if("/" in line and "%" in line and line[line.index("/") + 1:line.index("%")] in programvars):
            if(programvars[line[line.index(keyw[3]) + len(keyw[3]) + 1:line.index(comp[1]) - 1]] < programvars[line[line.index("/") + 1:line.index("%")]]):
                flags["equality"] = True
                flags["non-equality"] = False
            else:
                flags["non-equality"] = True
                flags["equality"] = False
                keepgoin = False
def grt_(op,line):
    global keepgoin
    if line[line.index(keyw[3]) + len(keyw[3]) + 1:line.index(comp[2]) - 1] in programvars:
        if("/" in line and "%" in line and line[line.index("/") + 1:line.index("%")] in programvars):
            if(programvars[line[line.index(keyw[3]) + len(keyw[3]) + 1:line.index(comp[2]) - 1]] > programvars[line[line.index("/") + 1:line.index("%")]]):
                flags["equality"] = True
                flags["non-equality"] = False
            else:
                flags["non-equality"] = True
                flags["equality"] = False
                keepgoin = False
def not_(op,line):
    global keepgoin
    if line[line.index(keyw[3]) + len(keyw[3]) + 1:line.index(comp[3]) - 1] in programvars:
        if("/" in line and "%" in line and line[line.index("/") + 1:line.index("%")] in programvars):
            if not programvars[line[line.index(keyw[3]) + len(keyw[3]) + 1:line.index(comp[3]) - 1]] == programvars[line[line.index("/") + 1:line.index("%")]]:
                flags["equality"] = True
                flags["non-equality"] = False
            else:
                flags["non-equality"] = True
                flags["equality"] = False
                keepgoin = False

args        = ["-f", "--file", "-i", "--interactive"]
keyw        = ["yell", "say", "maybe", "assuming","jump"]
ops         = ["num", "str", "/", "%"]
aritm       = ["add", "sub", "is", "mul", "div", "mod", "pow"]
comp        = ["equals", "<", ">", "not"]
flags       = {"equality":False,"non-equality":False}
code        = ""
compmix     = {"equals":equ_,"<":let_,">":grt_,"not":not_}
mathmix     = {"add":add_,"sub":sub_,"mul":mul_,"div":div_,"mod":mod_,"pow":pow_}
reserved    = comp + aritm + ops + keyw
programvars = {}
ignore      = 0

clargs  = sys.argv

def dothings(thing):
    global keepgoin, ignore
    lines = thing.splitlines()
    for linum, line in enumerate(lines):
        if not line.startswith("nop") and keepgoin == True and ignore <= 0:
            try:
                for kw in keyw:
                    if kw in line:
                        if(kw == keyw[1]):
                            if(ops[2] in line[line.index(keyw[1]) + len(keyw[1]) + 1:line.index(";")] and ops[3] in line[line.index(keyw[1]) + len(keyw[1]) + 1:line.index(";")] and line[line.index("/") + 1:line.index("%")] in programvars):
                                var = programvars[line[line.index("/") + 1:line.index("%")]]
                                print line[line.index(keyw[1]) + len(keyw[1]) + 1:line.index("/")] + str(var) + line[line.index("%") + 1:line.index(";")]
                            else:
                                print line[line.index(keyw[1]) + len(keyw[1]) + 1:line.index(";")]
                            for word in reserved:
                                if word in line:
                                    line.strip(word)
                        elif(kw == keyw[0]):
                            if(ops[2] in line[line.index(keyw[0]) + len(keyw[0]) + 1:line.index(";")] and ops[3] in line[line.index(keyw[0]) + len(keyw[0]) + 1:line.index(";")] and line[line.index("/") + 1:line.index("%")] in programvars):
                                var = programvars[line[line.index("/") + 1:line.index("%")]]
                                print line[line.index(keyw[0]) + len(keyw[0]):line.index("/")] + str(var) + line[line.index("%") + 1:line.index(";")].upper()
                            else:
                                print line[line.index(keyw[0]) + len(keyw[0]) + 1:line.index(";")].upper()
                            for word in reserved:
                                if word in line:
                                    line.strip(word)
                        elif(kw == keyw[2]):
                            from random import randint; rnum = randint(1,2)
                            if rnum == 2:
                                keepgoin = True
                            else:
                                keepgoin = False
                        elif(kw == keyw[3]):
                            for cx in comp:
                                if cx in line:
                                    compmix[cx](cx,line)
                        elif(kw == keyw[4]):
                            if "&" in line and "!" in line:
                                if line[line.index("&"):line.index("!")] in thing:
                                    place = lines.index(line[line.index("&"):line.index("!")])
                                    ignore = place - linum
                                else:
                                    print "\n" + str(thing)
                                    print "\nmark not found!\n"
                            else:
                                place = int(line[line.index(keyw[4]) + len(keyw[4]) + 1:line.index(";")])
                                if place <= len(lines):
                                    ignore = place - linum
                for op in ops:
                    if op in line:
                        if(op == ops[0] and line[line.index(ops[0]) + len(ops[0]) + 1:line.index(";")] in programvars):
                            programvars[line[line.index(ops[0]) + len(ops[0]) + 1:line.index(";")]] = int(programvars[line[line.index(ops[0]) + len(ops[0]) + 1:line.index(";")]])
                        elif(op == ops[1] and line[line.index(ops[1]) + len(ops[1]) + 1:line.index(";")] in programvars):
                            programvars[line[line.index(ops[1]) + len(ops[1]) + 1:line.index(";")]] = str(programvars[line[line.index(ops[1]) + len(ops[1]) + 1:line.index(";")]])
                for at in aritm:
                    if at in line:
                        if(at == aritm[2]):
                            if "pltx" in line:
                                programvars[line[line.index("pltx") + 5:line.index(aritm[2]) - 1]] = line[line.index(aritm[2]) + 3:line.index(";")]
                            else:
                                programvars[line[:line.index(aritm[2]) - 1]] = line[line.index(aritm[2]) + 3:line.index(";")]
                        else:
                            mathmix[at](at, line)
            except TypeError:
                print "something went wrong here, remember to put a semicolon(;) in the end of lines"
        else:
            ignore -= 1
            keepgoin = True


if(len(clargs) > 1):
    if(clargs[1] == "--help" or clargs[1] == "-h"):
        print "\n<> -> obrigatory  [] -> optional  \n\n-h --help                  show this help and exit\n-i --interactive           run the language on interactive mode, like python\n-f --file <somefile.chl>   you know... do things with the file and run some commands\n-c --docs                  see some useful things about the language\n-d --debug                 complex debugging shit, alert: its broken i just put it here to help me remember that it exists\n"
    else:
        if(clargs[1] == args[0] or clargs[1] == args[1]):
            if(len(clargs) > 2):
                try:
                    f = open(clargs[2])
                    code = f.read()
                except:
                    print "\nError opening file! check if the file exists and try again\n"
                dothings(code)
            else:
                print "\nWrong number of arguments! usage: -f somefile.chl\n"
        elif(clargs[1] == args[2] or clargs == args[3]):
            pass
