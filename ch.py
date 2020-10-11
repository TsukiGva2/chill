import sys

args        = ["-f", "--file", "-i", "--interactive"]
keyw        = ["yell", "say"]
ops         = ["num", "str", "/", "%"]
aritm       = ["add", "sub", "is", "mul", "div", "mod", "pow"]
comp        = ["equals", "<", ">", "not"]
code        = ""
reserved    = comp + aritm + ops + keyw
programvars = {}

clargs  = sys.argv

def dothings(thing):
    for line in thing.splitlines():
        for kw in keyw:
            if kw in line:
                if(kw == "say"):
                    if(ops[2] in line[line.index("say") + 4:line.index(";")] and ops[3] in line[line.index("say") + 4:line.index(";")] and line[line.index("/") + 1:line.index("%")] in programvars):
                        var = programvars[line[line.index("/") + 1:line.index("%")]]
                        print line[line.index("say") + 4:line.index("/")] + str(var) + line[line.index("%") + 1:line.index(";")]
                    else:
                        print line[line.index("say") + 4:line.index(";")]
                    for word in reserved:
                        if word in line:
                            line.strip(word)
                elif(kw == "yell"):
                    if(ops[2] in line[line.index("yell") + 5:line.index(";")] and ops[3] in line[line.index("yell") + 5:line.index(";")] and line[line.index("/") + 1:line.index("%")] in programvars):
                        var = programvars[line[line.index("/") + 1:line.index("%")]]
                        print line[line.index("yell") + 5:line.index("/")] + str(var) + line[line.index("%") + 1:line.index(";")].upper()
                    else:
                        print line[line.index("yell") + 5:line.index(";")].upper()
                    for word in reserved:
                        if word in line:
                            line.strip(word)
        for op in ops:
            if op in line:
                if(op == ops[0]):
                    programvars[line[line.index(ops[0]) + 4:line.index(";")]] = int(programvars[line[line.index(ops[0]) + 4:line.index(";")]])
        for at in aritm:
            if at in line:
                if(at == aritm[2]):
                    programvars[line[:line.index("is") - 1]] = line[line.index("is") + 3:line.index(";")]
                elif(at == aritm[0]):
                    try:
                        programvars[line[line.index(aritm[0]) + 4:line.index(",")]] += int(line[line.index(",") + 1:line.index(";")])
                    except TypeError:
                        print "\nError in expression ADD, two arguments must be numbers!\ntry: num <var>; before using that expression\n" # put line number here
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
