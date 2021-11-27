import pprint

def merge_sort(elements, key=None, descending=False):
    len_e = len(elements)
    if len_e <= 1:
        return elements
    mid = len_e // 2
    
    left = merge_sort(elements[:mid], key, descending)
    right = merge_sort(elements[mid:], key, descending)
    sorted_list = merge(left, right, key, descending)
    
    return sorted_list
    
def merge(left, right, key, descending):
    merged = []
    if key is None:
        if descending:
            while len(left) > 0 and len(right) > 0:
                if left[0] >= right[0]:
                    merged.append(left.pop(0))
                else:
                    merged.append(right.pop(0))
        else:
            while len(left) > 0 and len(right) > 0:
                if left[0] <= right[0]:
                    merged.append(left.pop(0))
                else:
                    merged.append(right.pop(0))
    else:
        if descending:
            while len(left) > 0 and len(right) > 0:
                if left[0][key] >= right[0][key]:
                    merged.append(left.pop(0))
                else:
                    merged.append(right.pop(0))
        else:
            while len(left) > 0 and len(right) > 0:
                if left[0][key] <= right[0][key]:
                    merged.append(left.pop(0))
                else:
                    merged.append(right.pop(0))
                    
    merged.extend(left)
    merged.extend(right)
        
    return merged

if __name__ =='__main__':
    numbers = [12,4,5,23,5,34,2,3,56,31,29]
    merge_sort(numbers)
    print(numbers)
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]
    for case in test_cases:
        merge_sort(case)
        print(case)
        
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    sorted_list = merge_sort(elements, key='time_hours', descending=True)
    pprint.pprint(sorted_list)
    