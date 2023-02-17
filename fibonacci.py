print("Hello! This code will write the first 20 numbers in the Fibonacci Sequence.")
#print("As an added challenge, it can also start at whatever number you give and print the 20 numbers in the sequence.")

num1 = 0
num2 = 1
count = 0

while count < 20:
    print(num1)
    result = num1 + num2
    num1 = num2
    num2 = result
    count += 1