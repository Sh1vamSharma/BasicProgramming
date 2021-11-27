def bubble_sort(my_list,key=None):
    swapped = False
    list_lenght = len(my_list)
    if list_lenght == 0:
        return
    for i in range(list_lenght-1):
        for j in range(list_lenght-1-i):
            if key != None:
                a = my_list[j][key]
                b = my_list[j+1][key]
            else:
                a = my_list[j]
                b = my_list[j+1]
            if a > b:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
                swapped = True
        if not swapped:
            break


    return my_list

if __name__ == "__main__":
    my_list = [6, 9, 4, 3, 5, 8, 2, 1,7]

    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]
    print(bubble_sort(elements, key = 'transaction_amount'))
    bubble_sort(my_list)
    print(my_list)
