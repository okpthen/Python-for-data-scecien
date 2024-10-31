import sys
import string


def count(str):
    upper = 0
    lower = 0
    puncuation = 0
    spaces = 0
    digit = 0
    for c in str:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c in string.punctuation:
            puncuation += 1
        elif c.isspace():
            spaces += 1
        elif c.isdigit():
            digit += 1
    print(f"The text containers {len(str)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{puncuation} puncuation marks")
    print(f"{spaces} spaces")
    print(f"{digit} dijits")


def main():
    if len(sys.argv) == 1:
        str = input("What is the text to count?\n")
        str += "\n"
    elif len(sys.argv) == 2:
        str = sys.argv[1]
    else:
        print("AssertionError: more than one argument is provided")
        exit()
    count(str)


if __name__ == "__main__":
    main()
