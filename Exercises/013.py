# Create an algorithm that reads an employee's salary and shows their
# new salary with a 15% raise.

salary = float(input("Enter the salary: "))
new_salary = float(salary + (salary * 0.15))

print("The salary with a 15% raise is: {:.2f}".format(new_salary))
