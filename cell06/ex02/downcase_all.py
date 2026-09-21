import sys

def downcase_it(text: str) -> str:
    return text.lower()

def main():
    if len(sys.argv) == 1:
        print("none")
        return

    Parameter = sys.argv[1:]

    for i in Parameter:
        print(downcase_it(i))

main()