number = int(input())

string_of_number = str(number)
x = 0


for i in range(len(string_of_number)):

    if int(string_of_number[x]) > 0:
        biggest_string = int(string_of_number[x])
    x += 1
print(biggest_string)

