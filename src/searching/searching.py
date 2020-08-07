list = [4, 3, 5, 19, 50, 34, 26, 73, 10, 30, 36, 28, 50, 24, 18, 14, 89, 109]


# def linear_search(arr, target): O(n)
#     # Your code here
def linear_search(arr, target):
            for i in range(0, len(arr)):
                if arr[i] == target:
                    return i
        return -1 # not found


#     return -1   # not found


# Write an iterative implementation of Binary Search
# def binary_search(arr, target): # O(log n)

    # Your code here
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    print(high)
    middle = (high + low) // 2
    print(middle)
    while low <= high:
        if target < arr[middle]:
            high = middle -1 # eliminate RHS
        elif target > arr[middle]:
            low = middle + 1 # eliminate LHS
        else:
            return middle

    return -1

result = binary_search(list, 50)

print(result)


