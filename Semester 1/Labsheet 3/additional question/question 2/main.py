def recursiveMaximum(arr, size):
    if size == 1:
        return arr[0]
    else:
        large = recursiveMaximum(arr, size-1)
        if arr[size-1] > large:
            large = arr[size-1]
        return large

arr = [-8,-2,-15,-4]
size = len(arr)

print(recursiveMaximum(arr,size))
print(size)

