# hash table or hash map : underlying data structure for Dictionary
# with collision handling using probing

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, data):
        h = 0
        for char in data:
            h += ord(char)
        return h%self.MAX

    def get_prob_range(self, index):
        # range from index to length of array + range 0 to index
        # print([*range(index, len(self.arr))] + [*range(0, index)])
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            # finding the new index value for hashmap
            if self.arr[prob_index] is None:
                return prob_index
            # if key is same that means value update
            if self.arr[prob_index][0] == key:
                return prob_index

        raise Exception("Hashmap is full")

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, value)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key,value)

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return  # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
        print(self.arr)


if __name__ == '__main__':
    t = HashTable()
    t["march 6"] = 20
    t["march 17"] = 88
    t["march 17"] = 29
    t["nov 1"] = 1
    t["march 33"] = 234
    print(t["dec 1"])
    print(t.arr)
    t["march 33"] = 67
    t['april 1'] = 45
    t['april 2'] = 25
    t['april 3'] = 15
    t['april 4'] = 5
    t['May 22'] = 34
    t['May 7'] = 34
    print(t.arr)
    #t['Jan 1'] = 34
    del t['april 2']
    t['Jan 1'] = 0
    print(t.arr)
    t.get_prob_range(5)