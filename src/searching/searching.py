list1 = ['what', 'when', 5, 10, 6, 'who', 100, 10000]

def linear_search(arr, target):
	for i in range(len(arr) - 1):
		if arr[i] == target:
			return arr[i]

	return -1

print(linear_search(list1, 6))


list2 = [1, 2, 3, 5, 6, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# Write an iterative implementation of Binary Search
def binary_search(arr, target):
	

    return -1  # not found
