# TO-DO: Complete the selection_sort() function below

list1 = [10, 25, 13, 8, 34, 23, 19, 45, 9, 7, 16, 36, 27, 23, 56]

# O(n^2)
def selection_sort(arr):
    # Loop through length of the list. 
    for i in range(0, len(arr) - 1):
        # Current index in the list passed in. 
        cur_index = i
        # print('line 11', arr[cur_index])
        # sets the current index to the smallest index. 
        smallest_index = cur_index
        # print('Line 14', arr[smallest_index])
        # TO-DO: find next smallest element
        # add 1 to current index to loop one step in the array. 
        for j in range(cur_index + 1, len(arr)):
            # Checks current index against the smallest index
            if arr[j] < arr[smallest_index]:
                #sets the smallest index to j. 
                smallest_index = j

        # print('Smallest index:', arr[smallest_index], 'Current Index:', arr[cur_index])
        # Reassigns the elements of the list according to their size. 
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr

# print(selection_sort(list1))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # for i in range(0, len(arr) - 1):
    #     curr_index = i
    #     next_index = i + 1
    #     print('Current:', arr[curr_index], 'Next:', arr[next_index])

    #     if arr[curr_index] > arr[next_index]:
    #         arr[curr_index], arr[next_index] = arr[next_index], arr[curr_index]
    #         i += 1
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
    return arr

print(bubble_sort(list1))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
