import sys

def main():

    if len(sys.argv) < 3 :
        print("none")
        return

    for i in range(len(sys.argv)-1, 0, -1):
        print(sys.argv[i])

main()
