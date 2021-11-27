from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)

def reverse_string(my_string):
    stack = Stack()
    for char in my_string:
        stack.push(char)
    new_string = ''
    while stack.size() != 0:
        new_string += stack.pop()
    return new_string

def match(ch1, ch2):
    '''
    :param ch1: paranthese closing
    :param ch2: paranthese starting poped out of stack
    :return: true if matches are found for whole string
    '''
    my_dict = {
        ']':'[',
        '}':'{',
        ')':'('
    }
    return my_dict[ch1] == ch2


def is_balanced(my_string):
    '''As going from left to right the last parantheses  started should
    end first i.e. the last bracket goes in should have it's first match'''
    stack = Stack()
    for char in my_string:
        if char == '[' or char == '{' or char == '(':
            stack.push(char)
        if char == ']' or char == '}' or char == ')':
            if stack.size() == 0:
                return False
            if not match(char, stack.pop()):
                return False
    return stack.size()==0


if __name__ == '__main__':
    stk = Stack()
    stk.push('Batman')
    stk.push('Superman')
    stk.push('Robin')
    print(stk.buffer)
    stk.pop()
    print(stk.buffer)
    print(reverse_string("Kids are angle"))
    print(is_balanced("(1/t)*{g-r}*[c+1]"))
    print(is_balanced("[{(tshfghdf)}]"))
    print(is_balanced("{(tshfghdf)}]"))
    print(is_balanced("[{(tshfghdf)]"))
