def isPalindrome(name):
    name = name.lower()
    if len(name) == 1:
        return True
    else:
        if name[0] == name[len(name)-1]:
            return isPalindrome(name[1:len(name)-1])
        else:
            return False

name = "Level"
palindrome = isPalindrome(name)

if palindrome:
    print(f"This name: {name}, is a palindrome")
else:
    print(f"This name: {name}, is not a palindrome")