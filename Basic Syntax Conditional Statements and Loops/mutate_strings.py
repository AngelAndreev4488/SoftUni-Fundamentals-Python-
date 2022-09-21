string_1 = input()
string_2 = input()
last_printed_string = string_1

for char in range(len(string_1)):
    left_side = string_2[:char + 1]
    right_side = string_1[char + 1:]
    printed_string = left_side + right_side
    if printed_string == last_printed_string:
        continue
    print(printed_string)
    last_printed_string = printed_string


