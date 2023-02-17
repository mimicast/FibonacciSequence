print("Hello! This code will write the first 20 numbers in the Fibonacci Sequence.")

num1 = 0
num2 = 1
count = 0

while count < 20:
    print(num1)
    result = num1 + num2
    num1 = num2
    num2 = result
    count += 1