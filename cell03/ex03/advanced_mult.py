import sys

def main():

    if len(sys.argv) != 1:
        print("none")
        return

    for i in range(11):
        print("Table de", str(i) + ": ", end="")
        for j in range(11):
            print(i*j, end=" ")
        print()

main()