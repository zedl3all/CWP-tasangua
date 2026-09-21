import sys

def main():

    if len(sys.argv) == 1:
        print("none")
        return

    Parameter = sys.argv[1:]

    for i in Parameter:
        temp = i[-3:]
        if temp != "ism":
            print(i+"ism")

main()
