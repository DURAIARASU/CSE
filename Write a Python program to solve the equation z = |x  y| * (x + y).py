def solve_equation(x, y):
    z = abs(x-y) * (x + y)
    return z
x =int(input("Enter the number :"))
y =int(input("Enter the number :"))
result = solve_equation(x, y)
print("The solution to the equation is:", result)
