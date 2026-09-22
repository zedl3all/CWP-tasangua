def array_of_names(persons: dict) -> list:

    Output = list()

    for i in persons:
        temp = i.capitalize() + " " + persons[i].capitalize()
        Output.append(temp)

    return Output

def main():
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
        }

    print(array_of_names(persons))

main()