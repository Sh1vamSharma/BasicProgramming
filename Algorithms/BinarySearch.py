from util import time_it

@time_it
def linear_search(num_list, num_to_find):
    idx = []
    for index, element in enumerate(num_list):
        if element == num_to_find:
            idx.append(index)
    if idx != []:
        return idx
    return -1

@time_it
def binary_search(num_list, num_to_find):
    left = 0
    right = len(num_list) - 1
    while left <= right:
        mid_idx = (left + right) // 2
        mid = num_list[mid_idx]
        if mid == num_to_find:
            return mid_idx
        elif mid < num_to_find:
            left = mid_idx+1
        else:
          right = mid_idx -1

    return -1

def binary_search_recursive(num_list, num_to_find, left, right):
    if left > right:
        return -1
    mid_idx = (left + right) // 2
    mid = num_list[mid_idx]
    if mid == num_to_find:
        return mid_idx
    elif mid < num_to_find:
        left = mid_idx + 1
    else:
        right = mid_idx - 1

    return binary_search_recursive(num_list, num_to_find, left, right)

def find_all_occurances(num_list, num_to_find):
    index = binary_search(num_list, num_to_find)

    indices = [index]

    i = index-1
    while i >= 0:
        if num_list[i] == num_to_find:
            indices.append(i)
        else:
            break
        i-=1

    i = index+1
    while i < len(num_list):
        if num_list[i] == num_to_find:
            indices.append(i)
        else:
            break
        i+=1

    return sorted(indices)


if __name__ =='__main__':
    # num_list = [12, 15, 35, 56, 67, 78, 89, 90, 112, 233, 456]
    # num_list = [i for i in range(1000001)]
    # num_list = [1, 4, 6, 9, 10, 5, 7] # not work on unsorted list
    num_list = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    num_to_find = 15

    index = linear_search(num_list, num_to_find)
    print("Number {} found at index : {} using linear search".format(num_to_find, index))

    index = binary_search(num_list, num_to_find)
    print("Number {} found at index : {} using Binary search".format(num_to_find, index))

    index = binary_search_recursive(num_list, num_to_find, 0, len(num_list)-1)
    print("Number {} found at index : {} using Recursive Binary search".format(num_to_find, index))

    indeces = find_all_occurances(num_list, num_to_find)
    print("Using binary search indices of occurances of {} are {}".format(num_to_find, indeces))

