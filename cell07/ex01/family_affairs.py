def find_the_redheads(family: dict) -> list:
    """Return Red Hair As List"""

    Output = list()

    for i in family:
        if family[i] == "red":
            Output.append(i)

    return Output

def main():
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
        }
    print(find_the_redheads(dupont_family))
main()
