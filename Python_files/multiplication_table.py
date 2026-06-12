# Multiplication Table Generator

num = int(input("Enter a number: "))

print("\nMultiplication Table:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")