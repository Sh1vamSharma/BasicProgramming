class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count +=1
            itr = itr.next
        return count

    def print(self, backward=False):
        if self.head is None:
            print("Linked List is Empty")
            return
        dllist = ''
        if backward:
            # traversing the list backward
            itr = self.get_last_node()
            while itr:
                dllist += str(itr.data)+"<->"
                itr = itr.prev
        else:
            # traversing the list forward
            itr = self.head
            while itr:
                dllist += str(itr.data)+'<->'
                itr = itr.next
        print(dllist)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        # data is already present in list for new element head is next
        else:
            # creating a head node with null previous link
            node = Node(data, self.head, None)
            # linking at the begining
            self.head.prev = node
            # making the node as head
            self.head = node

    def insert_at_end(self, data):
        # when list is empty
        if self.head is None:
            # last element points to null
            self.head = Node(data, None, None)
            return

        itr = self.head
        # traversing to the list reaching to the end
        while itr.next:
            itr = itr.next  # at last itr.next is null in end breaking loop
        # adding new data at the end
        itr.next = Node(data, None, itr)

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
                    node = Node(data, itr.next, itr)
                    if node.next:   # not last element in list
                        itr.next.prev = node
                    itr.next = node
                    break
                itr = itr.next
                count += 1
        else:
            raise Exception("Index out of Bound")

    def remove_at(self, index):
        if 0<=index<=self.get_length():
            if index == 0:
                self.head = self.head.next
            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    itr.next = itr.next.next
                    itr.next.prev = itr.next
                itr = itr.next
                count +=1
        else:
            raise Exception("Index out of bound")




if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_end(34)
    dll.insert_at_begining(56)
    dll.insert_at_begining(674)
    dll.insert_values(['Thor', 'Black Widow', 'Ironman', 'Loki'], True)
    dll.insert_at('Spiderman', 0)
    dll.insert_at('Vision', 1)
    dll.remove_at(2)
    dll.print()

