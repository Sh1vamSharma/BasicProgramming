from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, data):
        self.buffer.appendleft(data)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.buffer.pop()
    def front(self):
        # if self.is_empty():
        #     print("Queue is empty")
        #     return
        return self.buffer[-1]
    def size(self):
        return  len(self.buffer)
    def is_empty(self):
        return len(self.buffer) == 0


def place_order(orders):
    for order in orders:
        print("Placing the order of : ", order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while not food_order_queue.is_empty():
        order = food_order_queue.dequeue()
        print("serving the order : ", order)
        time.sleep(2)

def produce_binary_number(num):
    number_queue = Queue()
    number_queue.enqueue('1')

    for i in range(num):
        front = number_queue.front()
        print("  "+front)
        number_queue.enqueue(front+"0")
        number_queue.enqueue(front+"1")
        number_queue.dequeue()

def decimal_to_binary(num):
    if num >= 1:
        decimal_to_binary(num//2)
        print(num%2, end='')


if __name__=='__main__':
    # q = Queue()
    # q.enqueue('Hello')
    # q.enqueue('My')
    # q.enqueue('name')
    # q.enqueue('is')
    # q.enqueue('Nash')
    # print(q.buffer)
    # q.dequeue()
    # print(q.buffer)
    # food_order_queue = Queue()
    # orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    # t1 = threading.Thread(target=place_order, args=(orders,))
    # t2 = threading.Thread(target=serve_order)
    # t1.start()
    # t2.start()
    # t1.join()
    # start = time.time()
    # produce_binary_number(1000000)
    # print("Execution time process 1 : ", time.time()-start)
    start2 = time.time()
    for i in range(1,1000001):
        decimal_to_binary(i)
        print()
    print("Execution time process 1 : ", time.time()-start2)
