import sys
args = sys.argv


def is_int(s):
    if not s:
        return False
    if s[0] in ('+', '-'):
        return s[1:].isdigit()
    return s.isdigit()


if len(args) > 2:
    print("AssertionError: more than one argument is provided")
elif len(args) == 2:
    if is_int(args[1]):
        if int(args[1]) % 2 != 0:
            print("I'm Odd.")
        else:
            print("I'm Even.")
            
    else:
        print("AssertionError: argument is not an integer")
