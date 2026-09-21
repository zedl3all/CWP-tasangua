import sys

def main():

    if len(sys.argv) != 2 :
        print("none")
        return

    print(sys.argv[1].lower())

"""
    # For CommandLine
    for i in sys.argv[1:]:
        if "'" in i:
            print(i.replace("'","").lower(), end=" ")
        else:
            print(i.lower(), end=" ")
"""

main()
