transactions = [
    ('food', 50),
    ('transport', 20),
    ('food', 30),
    ('entertainment', 40),
    ('transport', 15),
    ('food', 25)
]

total = {}

for category, value in transactions:
    if category in total:
        total[category] += value
    else:
        total[category] = value

print(total)