import sys

def main():

    if len(sys.argv) != 3:
        print("none")
        return

    Start, End = sys.argv[1:]

    Output = list()

    for i in range(int(Start), int(End)+1):
        Output.append(i)

    print(Output)

main()
