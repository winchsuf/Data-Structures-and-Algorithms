def findLength(arg):
    if arg == "":
        return 0
    else:
        return 1 + findLength(arg[1:]) #Start at index 1 and go until the end.

arg = input("Enter a word or sentence: ")

print(f"The length of the string {arg} is: {findLength(arg)}")