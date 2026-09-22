def famous_births(peoples: dict):

    sorted_data = dict(sorted(peoples.items(), key=get_value))

    for i in sorted_data:
        print(f"{sorted_data[i]["name"]} is a great scientist born in {sorted_data[i]["date_of_birth"]}.")

def get_value(item):
    return item[1]["date_of_birth"]

def main():
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
        }

    famous_births(women_scientists)

main()