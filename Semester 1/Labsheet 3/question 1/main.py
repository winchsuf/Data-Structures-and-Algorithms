def recursiveSum(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num + recursiveSum(num - 1)

num = int(input("Enter a number: "))

print(f"The sum of the first {num} is {recursiveSum(num)}")