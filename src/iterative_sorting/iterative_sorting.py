# TO-DO: Complete the selection_sort() function below
list = [4, 10, 3, 20, 5, 14, 19, 16]

# while list:
#     print(list.pop(-1))

i = 0
while i < len(list):
    print(list[i])
    i += 1
print('')
print('')

# def selection_sort(arr):
#     # loop through n-1 elements
#     for i in range(len(arr)):
#         min_ = i
#         for j in range(i + 1, len(arr)):
#             if arr[min_] > arr[j]:
#                 min_ = j

#         temp = arr[i]
#         arr[i] = arr[min_]
#         arr[min_] = temp

# selection_sort(list)

# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    n = len(arr)
    print('N = array length:', n)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sort(list)

i = 0
while i < len(list):
    print(list[i])
    i += 1

    # return arr

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
