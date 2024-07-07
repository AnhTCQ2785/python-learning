employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
#practice1
for employee in employees:
    name, hours, rate = employee
    payment= hours* rate
    print(f"{name} is due to be paid ${payment:.2f}")
#practice2
total_wage = 0
num_employees = len(employees)

for _, _, rate in employees:
    total_wage += rate

average_wage = total_wage / num_employees

print("\nEmployees earning above average hourly wage:")
for name, _, rate in employees:
    if rate > average_wage:
        print(name)