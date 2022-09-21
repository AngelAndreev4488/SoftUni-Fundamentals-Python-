number = int(input())

for _ in range(number):
    n = int(input())
    if n % 2 == 1:
        print(f"{n} is odd!")
        break
else:
    print("All numbers are even.")


