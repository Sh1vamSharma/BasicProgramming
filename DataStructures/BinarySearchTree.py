class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # if data is already present can't have duplicates
        if data == self.data:
            return
        # adding data to left subtree:
        if data < self.data:
            if self.left:       # when left node is not a leaf
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        # adding data to right subtree:
        else:
            if self.right:      # when right node is not a leaf
                self.right.add_child(data)
            else :
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data)
        # visit reght tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        # visit base node
        elements = [self.data]
        # visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()
        # visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.post_order_traversal()
        # visit right tree
        if self.right:
            elements += self.right.post_order_traversal()
        # visit base node
        elements.append(self.data)

        return elements

    def search(self, value):
        if self.data == value:
            return True
        elif value < self.data:
            # value might be in left subtree
            if self.left:
                return self.left.search(value)
        else:
            # value might be in right subtree
            if self.right:
                return self.right.search(value)

        return False

    def find_min(self):
        return self.data if self.left is None else self.left.find_min()

    def find_max(self):
        # reaching to the right most item
        return self.data if self.right is None else self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + self.right + self.left

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # case 1 : when node to be deleted is a leaf
            if self.left is None and self.right is None:
                return None
            # case 2 : when node to be deleted has right subtree
            if self.left is None:
                return self.right
            # case 3 : when node to be deleted has left subtree
            if self.right is None:
                return self.left
            # case 4 when node to be deleted has oth subtrees
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)
        return self

    def delete2(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # case 1 : when node to be deleted is a leaf
            if self.left is None and self.right is None:
                return None
            # case 2 : when node to be deleted has right subtree
            if self.left is None:
                return self.right
            # case 3 : when node to be deleted has left subtree
            if self.right is None:
                return self.left
            # case 4 when node to be deleted has oth subtrees
            max_value = self.left.find_max()
            self.data = max_value
            self.left = self.left.delete(max_value)
        return self



def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    # numbers = [18, 7, 65, 3, 24, 16, 9, 45, 65, 18, 7, 94, 52]
    # names = ['thor', 'loki', 'venom', 'thor', 'spiderman','ironman', 'antman']
    # nums = [15, 12, 27, 7, 14, 20, 88, 23]
    nums = [17, 4, 1, 20, 9, 23, 18, 34]
    # tree = build_tree(numbers)
    my_tree = build_tree(nums)
    # print(tree.in_order_traversal())
    # name_tree = build_tree(names)
    # print(name_tree.in_order_traversal())
    # print(name_tree.search("Robin"))
    # print(name_tree.search("venom"))
    # print(tree.find_max())
    # print(tree.find_min())
    # print(tree.calculate_sum())
    print("Tree before deleting Node", my_tree.in_order_traversal())
    my_tree.delete2(17)
    print("Tree after deleting Node", my_tree.in_order_traversal())
    # print(my_tree.find_max())
    # print(my_tree.find_min())
    # print(my_tree.in_order_traversal())
    # print(my_tree.pre_order_traversal())
    # print(my_tree.post_order_traversal())






