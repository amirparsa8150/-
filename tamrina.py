def to_binary(number):
    return bin(number)[2:]

# input
num = int(input("enter a number: "))
binary_representation = to_binary(num)
print(f"binary: {binary_representation}")