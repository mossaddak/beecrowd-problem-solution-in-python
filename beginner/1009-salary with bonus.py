name = input()
fixed_salary = float(input())
monthly_sold = float(input())
total = fixed_salary + (15 / 100 * monthly_sold)
print(f"TOTAL = R$ {total:.2f}")