import sys

def shrink(text: str) -> str:
    return(text[slice(8)])

def enlarge(text: str) -> str:
    return text + "Z"*(8 - len(text))

def main():
    if len(sys.argv) == 1:
        print("none")
        return

    Parameter = sys.argv[1:]

    for i in Parameter:
        print(enlarge(shrink(i)))

main()