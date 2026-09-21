import sys
import re

def main():

    if len(sys.argv) != 2:
        print("none")
        return

    Parameter = sys.argv[1]

    if (not(re.findall("z",Parameter))):
        print("none")
        return

    for i in Parameter:
        if i == 'z':
            print(i, end="")


main()
