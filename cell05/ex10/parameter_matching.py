import sys

def main():

    if len(sys.argv) != 2 :
        print("none")
        return

    Parameter = sys.argv[1]
    Text = input("What was the parameter? ")
    if (Parameter == Text):
        print("Good job!")
    else:
        print("Nope, sorry...")

main()
