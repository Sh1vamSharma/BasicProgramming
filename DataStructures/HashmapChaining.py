# hash table or hash map : underlying data structure for Dictionary
# with collision handling using chaining

class HashTable:
    def __init__(self):
        self.MAX = 10       # block of memory allocation
        # empty 2D list (2D array) containing hash functions associated with key
        self.arr = [[] for i in range(self.MAX)]


    def get_hash(self, data):
        '''
        generating hash function using ASCII
        '''
        h = 0
        for char in data:
            h += ord(char)
        return h % self.MAX

    # the following methods will allow to use operators []
    # to set, get and del item with c
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        # if the key is present in the list
        # we should be able to update its value in tuple
        found = False               # flag
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        # if the key is not present in the list
        # updating the key value pair as touple
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

if __name__ == "__main__":
    dict = HashTable()
    dict['Doremon'] = 12
    dict['Nobita'] = 13
    dict['Shizuka'] = 11
    dict['Gian'] = 15
    dict['Sunio'] = 10
    dict['march 6'] = 75
    dict['march 6'] = 62
    dict['march 8'] = 123
    dict['march 9'] = 58
    dict['march 17'] = 94
    # print(dict['march 6'])
    # print("The Hashmap is given below:")
    # for i in range(len(dict.arr)):
    #     if dict.arr[i] != []:
    #         print(dict.arr[i])
    del dict['march 17']
    del dict['march 6']
    print("The Modified Hashmap is given below:")
    for i in range(len(dict.arr)):
        if dict.arr[i] != []:
            print(dict.arr[i])
    print("the deleted value is now: ",dict['march 6'])
    # array = []
    # with open('nyc_weather.csv', "r") as file:
    #     for line in file:
    #         token = line.split(',')
    #         try:
    #             temp = int(token[1])
    #             array.append(temp)
    #         except:
    #             pass
    #             # print('Error')
    # print(array)
    # print(sum(array[0:7])/7)
    # print(max(array[0:10]))

    # dict = {}
    # with open('nyc_weather.csv', "r") as file:
    #     for line in file:
    #         token = line.split(',')
    #         try :
    #             dict[token[0]] = int(token[1])
    #         except:
    #             pass
    # print(dict)
    # word_count = {}
    # with open('poem.txt', 'r') as file:
    #     for line in file:
    #         tokens = line.split(' ')
    #         for token in tokens:
    #             token = token.replace('\n','')
    #             if token in word_count:
    #                 word_count[token] += 1
    #             else:
    #                 word_count[token] = 1
    # print(word_count)



