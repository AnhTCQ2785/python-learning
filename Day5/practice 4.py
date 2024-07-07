hours_worked = float(input("How many hours has the employee worked this week? "))
hourly_wage = float(input("What is the employee's hourly wage? "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (hourly_wage * 1.1)
    total_pay = (40 * hourly_wage) + overtime_pay
    print(f"The employee worked {overtime_hours} overtime hours. ")
    print(f"The employee is pay extra {overtime_pay:.2f} USD. ")
    print(f"The total salary is {total_pay:2f} USD .")
else:
    total_pay = hours_worked * hourly_wage
    print(" The employee who not have the overtime work.")
    print(" The total salary(total_pay:.2f) USD.")
