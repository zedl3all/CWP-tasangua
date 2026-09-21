import sys

def main():

    if len(sys.argv) == 1 :
        print("none")
        return

    Parameter = sys.argv[1:]

    print("parameters:", len(Parameter))

    for i in Parameter:
        print(f"{i}: {len(i)}")

main()
