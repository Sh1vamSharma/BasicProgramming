import math
import copy

def insertion_sort(elements):
    for i in range(1 , len(elements)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor
    
    return elements

def running_median(elements):
    running_median = []
    i = 1
    
    while i < len(elements):
        my_arr = insertion_sort(elements[:i])
        arr_len = len(my_arr)
        if arr_len == 1 :
            running_median.append(elements[0])
        elif arr_len%2 == 0:
            mid_left = int(arr_len/2)
            mid_right = int(mid_left-1)
            running_median.append((my_arr[mid_left]+my_arr[mid_right])/2)
        else:
            mid = math.floor(arr_len/2)
            running_median.append(elements[mid])
        i +=1
        
    return running_median
    
    

if __name__ =='__main__':
    numbers = [12,4,5,23,5,34,2,3,56,31,29]
    numbers_copy = copy.deepcopy(numbers)
    insertion_sort(numbers)
    sorted = insertion_sort(numbers)
    print("Sorted list : ", sorted)
    print("Copied List : ", numbers_copy)
    running_med = running_median(numbers_copy)
    print("running median : ", running_med)
    