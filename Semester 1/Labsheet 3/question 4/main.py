def triangular(term):
    if term == 0:
        return 0
    elif term == 1:
        return 1
    else:
        return term + triangular(term - 1)

term = int(input("Enter the term: "))

print(f"The result for the {term}th term is: {triangular(term)} ")