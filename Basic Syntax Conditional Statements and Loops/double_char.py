command = input()
word = ""

while command != "End":
    if command == "SoftUni":
        continue
    elif command != "SoftUni":
        for char in range(len(command)):
            word += command[char] + command[char]
        print(word)
    command = input()
    word = ""


