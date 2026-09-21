array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = set()
for i in array:
    if(i+2) > 5:
        new_array.add(i+2)

print(list(new_array))