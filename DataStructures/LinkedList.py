class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next        # pointer to the next element


class LinkedList:
    def __init__(self):
        self.head = None        # points to head of linked list

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        itr = self.head
        llstr = ''
        # traversing the list
        while itr:
            llstr += str(itr.data)+'->'
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_begining(self, data):
        # data is already present in list for new element head is next
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        # when list is empty
        if self.head is None:
            # last element points to null
            self.head = Node(data, None)
            return

        itr = self.head
        # traversing to the list reaching to the end
        while itr.next:
            itr = itr.next     # at last itr.next is null in end breaking loop
        # adding new data at the end
        itr.next = Node(data, None)

    def insert_values(self, data_list, newlist=False):
        if newlist:
            self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, data, index):
        if 0 <= index <= self.get_length():
            if index == 0:
                self.insert_at_begining(data)
                return
            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    # pointing to new element and new element points to next in list
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1
        else:
            raise Exception("Index out of Bound")

    def remove_at(self, index):
        if 0 <= index <= self.get_length():         # inside list
            if index == 0:                          # change head
                self.head = self.head.next
            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    itr.next = itr.next.next        # pointing to next to next element
                    break
                itr = itr.next
                count += 1
        else:
            raise Exception("Index is out of bound")

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_end(34)
    # ll.insert_at_begining(56)
    ll.insert_values(['Thor', 'Black Widow', 'Ironman', 'Loki'], True)
    ll.insert_after_value('Captain', 'Hawkeye')
    # ll.insert_at_begining(45)
    # ll.insert_at_begining(67)
    # ll.insert_at_end(999)
    # ll.insert_values(['Hawkeye'])
    # print('Length of the list : ', ll.get_length())
    # ll.print()
    # ll.remove_at(0)
    # ll.print()
    # ll.insert_at('Spiderman', 0)
    # ll.insert_at(96432, 6)
    # ll.insert_at('Falcon', ll.get_length())
    ll.print()

