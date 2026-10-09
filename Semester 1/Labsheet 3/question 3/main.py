def multiply(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    else:
        return num1 + multiply(num1, num2 - 1)

num1 = int(input("Enter value for number 1: "))
num2 = int(input("Enter value for number 2: "))

print(f"The multiplication for num1 {num1} and num2 {num2} is {multiply(num1, num2)}")
