listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

listThree = []

for l1 in listOne:
    if (listOne.index(l1) % 2):
        listThree.append(l1)

for l2 in listTwo:
    if not (listTwo.index(l2) % 2):
        listThree.append(l2)

print listThree


listA = [1, 3, 46, 1, 3, 9]
k = 47

# listA = [6, 6, 3, 9, 3, 5, 1]
# k = 12

output_result = 0

for a in listA:
    if listA.index(a) == (len(listA) - 1):
        break

    if (a + listA[(listA.index(a) + 1)]) == k:
        output_result += 1

    del listA[listA.index(a)]


print output_result


"""
Write a Python program to push three items into a heap and return
the smallest item from the heap. Also Pop and return
the smallest item from the heap.
"""

import heapq

heap = []
heapq.heappush(heap, ('V', 3))
heapq.heappush(heap, ('V', 2))
heapq.heappush(heap, ('V', 1))

print('Items in a heap')
for a in heap:
    print(a)

print('Smallest Item in a heap')
print(heap[0])

print('Pop Smallest Item from the heap')
heapq.heappop(heap)
for a in heap:
    print(a)

print('Push Item into the heap')
heapq.heappush(heap, ('V', 4))
for a in heap:
    print(a)
print('------------------------------')


"""
Python Data Structure
Write a Python program to get the two largest and three smallest items from a dataset.
"""

import heapq
h = [10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]
print('Two largest number of above dataset')
print(heapq.nlargest(2, h))
print('Two smallest number of above dataset')
print(heapq.nsmallest(2, h))
print('------------------------------')

# Second Alternative way to get the largest and smallest values from list
largest_numbers = []
largest_numbers.append(max(h))
h.remove(max(h))
largest_numbers.append(max(h))
print('Two Largest numbers')
print(largest_numbers)

smallest_numbers = []
smallest_numbers.append(min(h))
h.remove(min(h))
smallest_numbers.append(min(h))
print('Two smallest numbers')
print(smallest_numbers)
print('----------------------------')


"""
Python Data Structure
Write a Python program to locate the left insertion point for a specified
value in sorted order.
"""

import bisect
def index(a, x):
   i =  bisect.bisect_left(a, x)
   return i

a_list = [1, 2, 4, 5]
print(index(a_list, 6))
print(index(a_list, 3))
print("-------------------------")

# Second Alternative way to find out with simple python code
c = 0

for a in a_list:
    if a_list.index(a) == (len(a_list) - 1):
        a_list.append(c)
        break

    if (a_list[a_list.index(a)]) > c:
        a_list.insert(a_list.index(a), c)
        break

print a_list
print a_list.index(c)
print("---------------------------")


"""
Python Data Structure
Write a Python program to locate the right insertion point for a
specified value in sorted order.
"""

a_list = [1, 2, 4, 7]
c = 3

for a in reversed(a_list):
    if a_list.index(a) == 0:
        a_list.insert(0, c)
    if a_list[a_list.index(a)] < c:
        a_list.insert(a_list.index(a) + 1, c)
        break

print('Search by Reverse Order')
print(a_list)
print(a_list.index(c))
print('------------------------------')


"""
Python Data Structure
Use bubble sort to sort the list
"""

array = [2, 1, 5, 4, 3]


def bubble_sort_ascending(array):
    length_of_array = len(array) - 1  # length_of_array = 4

    for i in range(length_of_array):
        for j in range(length_of_array - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


print("Sort The list by using bubble sorting in Ascending Order")
print bubble_sort_ascending(array)
print('------------------------')


array = [2, 1, 5, 4, 3]


def bubble_sort_descending(array):
    length_of_array = len(array) - 1
    for i in range(length_of_array):
        for j in range(length_of_array - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


print("Sort The list by using bubble sorting in Descending Order")
print bubble_sort_descending(array)
print('------------------------')



"""
Data Structure
Linear Search in List
"""

a_list = [1, 2, 5, 6, 18, 48, 19, 7, 20, 9, 88, 67]
x = 9

print "Linear Search in List"
for a in range(len(a_list)):
    if a_list[a] == x:
        print "Search of %s found at postion: %s" % (x, a)
        break

print "--------------------------"


"""
Data Structure
Binary Search in List
"""


a_list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 222, 333]
x = 222


def binary_search_list(a_list, x):

    a_min = 0
    a_max = len(a_list) - 1
    avg = (a_max - a_min)/2

    while (a_min < a_max):
        if a_list[avg] == x:
            return avg
        elif a_list[avg] < x:
            return avg + 1 + binary_search_list(a_list[avg+1:], x)
        elif a_list[avg] > x:
            return binary_search_list(a_list[:avg+1], x)


print(binary_search_list(a_list, x))
print("--------------------------")
