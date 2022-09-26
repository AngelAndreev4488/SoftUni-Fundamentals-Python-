new_year = int(input())

new_year_condition = False

while not new_year_condition:
    new_year += 1
    new_year_set = set()
    for i in range(len(str(new_year))):
        new_year_set.add(str(new_year)[i])

    new_year_condition = len(new_year_set) == len(str(new_year))

print(new_year)