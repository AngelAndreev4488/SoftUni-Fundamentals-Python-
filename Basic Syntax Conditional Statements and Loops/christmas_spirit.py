decorations_to_buy = int(input())
days_until_christmas = int(input())

counted_days = 0
budget = 0
spirit = 0
# Decoration	Price/Piece	Points/Shopping
# Ornament Set	   2$	               5
# Tree Skirt	   5$	               3
# Tree Garland     3$	               10
# Tree Lights	   15$	               17

while days_until_christmas >= 1:
    days_until_christmas -= 1
    counted_days += 1
    if counted_days % 11 == 0:
        decorations_to_buy += 2
    if counted_days % 2 == 0:
        budget += 2 * decorations_to_buy
        spirit += 5
    if counted_days % 3 == 0:
        budget += 8 * decorations_to_buy
        spirit += 13
    if counted_days % 5 == 0:
        budget += 15 * decorations_to_buy
        spirit += 17
        if counted_days % 3 == 0 and counted_days % 5 == 0:
            spirit += 30
    if counted_days % 10 == 0:
        spirit -= 20
        budget += 23
        if days_until_christmas < 1:
            spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")







