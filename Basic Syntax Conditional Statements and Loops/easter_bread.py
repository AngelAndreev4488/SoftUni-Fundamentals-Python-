budget = float(input())
price_for_kg_flour = float(input())

coloured_egg = 0
number_of_bread_loaf = 0

egg_price = 0.75 * price_for_kg_flour
milk_price = 1.25 * price_for_kg_flour
price_for_loaf = price_for_kg_flour + egg_price + (milk_price / 4)

while budget >= price_for_loaf:
    coloured_egg += 3
    number_of_bread_loaf += 1
    if number_of_bread_loaf % 3 == 0:
        coloured_egg -= (number_of_bread_loaf - 2)
    budget -= price_for_loaf

print(f"You made {number_of_bread_loaf} loaves of Easter bread! Now you have {coloured_egg} eggs and {budget:.2f}BGN left.")
