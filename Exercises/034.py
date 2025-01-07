# Write a program that asks for an employee's salary and calculates the value of their raise.
# For salaries above R$1,250.00, calculate a 10% raise.
# For salaries below or equal to that amount, the raise is 15%.

salary = float(input("Enter your salary: "))

# Calculate raise based on salary amount
if salary > 1250:
    salary += salary * 0.1  # 10% raise for salaries above 1250
else:
    salary += salary * 0.15  # 15% raise for salaries less than or equal to 1250

print(f"Your new salary is R${salary:.2f}")
