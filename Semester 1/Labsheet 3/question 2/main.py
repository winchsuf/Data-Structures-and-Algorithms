def recursivePower(num, power):
    if power == 0:
        return 1
    elif power == 1:
        return num
    else:
        return num * recursivePower(num, power -1 )

num = int(input("Enter value for num: "))
power = int(input("Enter the power: "))

print(f"{num} to the power of {power} gives result {recursivePower(num, power)}")