import re
import sys

def main():

    if len(sys.argv) < 3 :
        print("none")
        return

    FindText = sys.argv[1]
    Text = sys.argv[2]
    print(len(re.findall(FindText,Text)))

main()
