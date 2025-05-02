import math


def solve_quadratic(a, b, c):
     discriminant = b**2 - 4*a*c  # delta
     if discriminant > 0:
          root1 = (-b + math.sqrt(discriminant)) / (2*a)
          root2 = (-b - math.sqrt(discriminant)) / (2*a)
          return f"two real roots: {root1} و {root2}"
     elif discriminant == 0:
          root = -b / (2*a)
          return "a real root: {root}"
     else:
           return "ریشه‌های مختلط هستند و در مجموعه اعداد حقیقی قرار ندارند."


a = float(input("amount a: "))
b = float(input("amount b: "))
c = float(input("amount c: "))
result = solve_quadratic(a, b, c)
print(result)