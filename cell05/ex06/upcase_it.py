import sys

def main():

    if len(sys.argv) != 2 :
        print("none")
        return

    print(sys.argv[1].upper())

"""
    # For CommandLine
    for i in sys.argv[1:]:
        if "'" in i:
            print(i.replace("'","").upper(), end=" ")
        else:
            print(i.upper(), end=" ")
"""

main()
