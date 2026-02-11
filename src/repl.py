from pylisp import *

def balanced(x):
    tk = tokenize(x)
    return x.count("(") == x.count(")")

curr = ""
while True:
    try:
        t = input("> " if balanced(curr) else "  ")
    except EOFError:
        break
    curr += t + "\n"
    if balanced(curr):
        try:
            parse(curr, f_Leval_2bprint)
        except Exception as e:
            print("ERROR: %s" % e)
        curr = ""
