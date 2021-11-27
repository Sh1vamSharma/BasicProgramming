# Hoare partition

def hoare_partition(elements, start, end):
    pivot_idx = start
    pivot = elements[pivot_idx]

    while start < end:
        while start <len(elements) and elements[start]<= pivot:
            start += 1
        while elements[end] > pivot:
            end -=1

        if start < end:
            elements[start], elements[end] = elements[end], elements[start]

    elements[pivot_idx], elements[end] = elements[end], elements[pivot_idx]

    return end

def lomuto_partition(elements, start, end):
    pivot = elements[end]
    p_idx = start

    for i in range(start, end):
        if elements[i] <= pivot:
            elements[i], elements[p_idx] = elements[p_idx], elements[i]
            p_idx+=1

    elements[p_idx], elements[end] = elements[end], elements[p_idx]


    return p_idx



def quick_sort(elements, start, end):
    if len(elements) == 1:
        return
    if start < end:
        hpi = hoare_partition(elements, start, end)
        #hpi = lomuto_partition(elements, start, end)
        quick_sort(elements, start, hpi-1)   # left partition
        quick_sort(elements, hpi+1, end)    # right partition

if __name__ =="__main__":
    #numbers = [5, 6, 3, 7, 1, 9]
    #elements = [11, 9, 29, 7, 2, 15, 28]
    elements = [5, 6, 3, 7, 1, 9]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)
