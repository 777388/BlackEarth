import sys
print("usage: CTE.py encryption, file, output")
types = []
charred = []
checks = []
i = 0
class typer:
    pass
#x = lambda b: print(c = type(b))
with open(sys.argv[1], "r") as encryption:
    with open(sys.argv[2], "r") as basefile:
        with open(sys.argv[3], "w") as output:
            encryptions = encryption.readlines()
            for line in encryptions:
                types.append(line)
            for chars in basefile:
                charred.append(chars)
            for a, c in zip(types, charred):
                if a in checks:
                    i += 1
                else:
                    checks.append(a)
                    
                output.write("class "+str(a.strip())+str(i)+":\r\t attr = '"+c.strip()+"'\r")
                output.write("print("+str(a.strip())+str(i)+".attr)\r")
encryption.close()
basefile.close()
output.close()