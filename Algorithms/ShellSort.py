
def shell_sort(elements, del_duplicate = False):
    size = len(elements)
    div = 2
    gap = size // div
    
    while gap > 0:
        index_to_del = []
        for i in range(gap, size):
            anchor = elements[i]
            j = i
            while j >= gap and elements[j - gap] >= anchor:
                if (elements[j-gap] == anchor) and del_duplicate:
                    index_to_del.append(j)
                elements[j] = elements[j - gap]
                j -= gap
            elements[j] = anchor
        if index_to_del and del_duplicate :
            index_to_del = list(set(index_to_del))
            index_to_del.sort()
            for i in index_to_del[-1::-1]:
                del elements[i]
        div *= 2
        size = len(elements)
        gap = size // div


if __name__ =='__main__':
    numbers = [12, 4, 5, 23, 5, 34, 2, 3, 56, 31, 29]
    shell_sort(numbers, True)
    print(numbers)
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5],
        [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    ]
    for case in test_cases:
        shell_sort(case, True)
        print(case)