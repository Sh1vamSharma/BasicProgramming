class TreeNode:

    def __init__(self, name , alias = None):
        self.name = name
        self.alias = alias
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p :
            level +=1
            p = p.parent
        return level


    def print_tree(self, depth, style='name'):
        level = self.get_level()
        if level > depth:
            return
        spaces = " " * level * 2
        prefix = spaces+"-> "  if self.parent else ""
        if style == 'name':
            print(prefix+self.name)
        elif style == 'alias':
            print(prefix+self.alias)
        elif style == 'both':
            print("{0} {1}({2})".format(prefix,self.name,self.alias))
        if self.children:
            for child in self.children:
                child.print_tree(depth, style)





def built_product_tree():
    # level 0
    root = TreeNode("Electronics")
    # level 1
    # defining the nodes
    tv = TreeNode("Television")
    laptop = TreeNode("Laptop")
    cellphone = TreeNode("Cellphone")
    # adding the nodes to the root
    root.add_child(tv)
    root.add_child(cellphone)
    root.add_child(laptop)
    # level 2 : adding leaves to the nodes
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("Samsung"))
    laptop.add_child(TreeNode("Lenovo"))
    laptop.add_child(TreeNode("Macbook"))
    laptop.add_child(TreeNode("Dell"))
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixer"))
    cellphone.add_child(TreeNode("Vivo"))

    return root

def built_managment_tree():
    # level 0
    root = TreeNode("Nilupul", "CEO")
    # level 1
    N1L1 = TreeNode("Chinmay", "CTO")
    N2L1 = TreeNode("Gels", "HR Head")
    root.add_child(N1L1)
    root.add_child(N2L1)
    # level 2
    N1L2 = TreeNode("Vishwa", "Infrastructure Head")
    N2L2 = TreeNode("Aamir", "Application Head")
    N3L2 = TreeNode("Peter", "Recruitment Manager")
    N4L2 = TreeNode("Waqas", "Policy Manager")
    N1L1.add_child(N1L2)
    N1L1.add_child(N2L2)
    N2L1.add_child(N3L2)
    N2L1.add_child(N4L2)
    # level 3
    N1L3 = TreeNode("Dhawal", "Cloud Manager")
    N2L3 = TreeNode("Abhijeet", "App Manager")
    N1L2.add_child(N1L3)
    N1L2.add_child(N2L3)

    return root

if __name__ == "__main__":
    # root1 = built_product_tree()
    # root1.print_tree()
    root = built_managment_tree()
    root.print_tree(5)
    # print("\n\n\n")
    # root.print_tree('name')
    # print("\n\n\n")
    # root.print_tree('alias')
