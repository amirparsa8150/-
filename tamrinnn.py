def decimal_to_binary(n):
    steps = []
    while n > 0:
        steps.append(n)
        n //= 2  

    binary_representation = bin(steps[0])[2:] if steps else "0"

    print("binary: ", binary_representation)

num = int(input("enter a number: "))
decimal_to_binary(num)