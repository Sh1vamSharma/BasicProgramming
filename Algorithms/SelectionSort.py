import pprint

def selection_sort(arr, key_list=None):
    arr_len = len(arr)
    if key_list is None:
        for i in range(arr_len-1):
            min_idx = i
            for j in range(min_idx+1, arr_len):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if i != min_idx:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
    else:
        for key in key_list[-1::-1]:
            for i in range(arr_len):
                min_idx = i
                for j in range(i, arr_len):
                    if arr[j][key] < arr[min_idx][key]:
                        min_idx = j
                if i != min_idx:
                    arr[i], arr[min_idx] = arr[min_idx], arr[i]



if __name__ == '__main__':
    # numbers = [12, 4, 5, 23, 5, 34, 2, 3, 56, 31, 29]
    # selection_sort(numbers)
    # print(numbers)
    # test_cases = [
    #     [10, 3, 15, 7, 8, 23, 98, 29],
    #     [],
    #     [3],
    #     [9, 8, 7, 2],
    #     [1, 2, 3, 4, 5],
    #     [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    # ]
    # for case in test_cases:
    #     selection_sort(case)
    #     print(case)
    #
    # elements = [
    #     {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    #     {'name': 'rajab', 'age': 12, 'time_hours': 3},
    #     {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
    #     {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    # ]
    elements = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]
    #
    # selection_sort(elements, key_list=['First Name', 'Last Name'])
    # pprint.pprint(elements)
    
    a = sorted(elements, key= lambda d : (d['First Name'], d['Last Name']))
    pprint.pprint(a)
        