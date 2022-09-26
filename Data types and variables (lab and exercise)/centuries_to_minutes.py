centuries_input = int(input())

years = centuries_input * 100
days = years * 365.2422
days1 = int(days)
hours = days1 * 24
minutes = hours * 60


print(f"{centuries_input} centuries = {years} years = {int(days1)} days = {int(hours)} hours = {int(minutes)} minutes")
