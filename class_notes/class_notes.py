----------------- iterative complexity ------------------------------

# Big-O
# factorial time complexity N!
# N! = N* N-1*...1
# O(A*B) != O(N^2)
​
# Classifications 
# 1. Constant time -- O(1)
# 2. Logarithmic time -- O(Log N)
    # log (base) N = exponent 
    # log 8 = 3
# 3. linear -- O(N)
# 4. linearithmic/log-linear -- O(N * Log N)
# 5. polynomial  -- O(N^c)
# 6. exponential -- O(c^N)
# 7. factorial -- O(N!) 
​
​
# 2. Logarithmic time -- O(Log N)
    # log (base) N = exponent 
    # log 8 = 3
# 3. linear -- O(N)
​
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
​
def print_animals(animal_list):
    for i in range(len(animal_list)):
        print(animal_list[i])
        counter = 0 
        for n in range(10000):
            counter += 1
# O(10000*N) --> O(N)
print_animals(animals)
​
# 4. linearithmic/log-linear -- O(N * Log N)
# 5. polynomial  -- O(N^c)
# 6. exponential -- O(c^N)
# 7. factorial -- O(N!)


------------------- Searching --------------------------------

import random
import time
# 100,000 ---> 50,000 Log(100,000)
# keywords: unsorted and random
​
my_range = 100
my_size = 10
​
my_random = random.sample(range(my_range), my_size)
print(my_random)
​
searching_for = 3
​
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False 
​
print(linear_search(my_random, searching_for))
​
# binary searach
# keywords: sorted, ordered
​
def find_value_binary(arr, value):
    first = 0
    last = (len(arr) - 1)
​
    found = False
​
    while first <= last and not found: 
        middle = (first + last) // 2
​
        if arr[middle] == value:
            found = True
        else:
            if value < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found
# [1, 2, 3, 4, 5, 6, 7] target = 5
​
​
# linear vs binary search



------------- insertion sort ---------------------
# my_list = [8, 2, 5, 4, 1, 3]
​
# my_list = [8, |  2, 5, 4, 1, 3]
​
# temp = 2
# my_list = [2, 8, |  5, 4, 1, 3]
​
# temp = 5
# my_list = [2, 5, 8, | 4, 1, 3]
​
# temp = 4
# my_list = [2, 5, 8, | 4, 1, 3]
# my_list = [2, 4, 5, | 8, 1, 3]
​
# separate the first element, think of it as sorted
# for all other items, starting at the second (index 1)
    # put current num into temp var
    # look left, until we find correct position
    # as we look left, shift items to right
# when left is smaller than temp or we're at zero index, put at this location
​
def insertion_sort(list_to_sort):
    # separate the first element, think of it as sorted
        # no code--abstract idea
    # for all other items, starting at the second (index 1)
    for i in range(1, len(list_to_sort)):
        # put current num into temp var
        temp = list_to_sort[i]
        # look left, until we find correct position
        j = i 
        while j > 0 and temp < list_to_sort[j - 1]:
            print(j) # for our understanding
            # as we look left, shift items to right
            list_to_sort[j] = list_to_sort[j-1]
            j -= 1
        # when left is smaller than temp or we're at zero index, put at this location
        list_to_sort[j] = temp
​
    return list_to_sort