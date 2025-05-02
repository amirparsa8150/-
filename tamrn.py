def square_numbers_before(n):
    for i in range(n):
        print(f"{i}^2 = {i**2}")

num = int(input("input a number: "))
square_numbers_before(num)