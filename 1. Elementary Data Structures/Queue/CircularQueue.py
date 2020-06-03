# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:46:32 2020

@author: Palash
"""

class Node(object):
    """Represents an element in the queue"""
    def __init__(self, data):
        """
        Constructor to intialize the node
        """
        self.data = data
        self.next = None
        
class CircularQueue(object):
    """Represents a circular queue ADT"""
    def __init__(self):
        """
        Constructor to initialize the circular queue object
        """
        self.head = None
        self.tail = None
        self.size = 0
        
    def __len__(self):
        """
        Returns the length of (number of elements in) the queue
        """
        return self.size
        
    def is_empty(self):
        """
        Return True if the queue is empty, False otherwise
        """
        return self.size == 0
    
    def get_head(self):
        """
        Returns the first element in the queue
        """
        return self.head.data
    
    def get_tail(self):
        """
        Returns the last element in the queue
        """
        return self.tail.data
    
    def enqueue(self, data):
        """
        Adds an element at the end of the queue
        """
        new_node = Node(data);
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        
    def dequeue(self):
        """
        Removes and returns the first element in the queue
        """
        if self.is_empty():
            raise ValueError('Queue is empty')
        else:
            temp =self.head
            self.head = self.head.next
            self.size -= 1
            return temp
        
    def rotate(self):
        """
        Puts the first element(head) of the queue at the end(tail)
        """
        if self.size > 0:
            temp = self.head
            self.head = self.head.next
            self.tail.next = temp
            self.tail = temp
            self.tail.next = None
        
    def printQueue(self):
        """
        Returns the circular queue in the form of a list
        """
        temp = self.head
        queue = []
        while temp:
            queue += [temp.data]
            temp = temp.next
        return queue
        
    
if __name__ == '__main__':
    queue_obj = CircularQueue()
    queue_obj.enqueue(5)
    queue_obj.enqueue(234)
    print(queue_obj.is_empty())
    print(queue_obj.printQueue())
    print(queue_obj.get_head())
    print(queue_obj.get_tail())
    queue_obj.rotate()
    print(queue_obj.printQueue())
    print(queue_obj.get_head())
    print(queue_obj.get_tail())
    queue_obj.enqueue(546)
    queue_obj.enqueue(7)
    print(queue_obj.printQueue())
    print(queue_obj.get_head())
    print(queue_obj.get_tail())
    queue_obj.rotate()
    print(queue_obj.printQueue())
    queue_obj.dequeue()
    print(queue_obj.printQueue())
    print(len(queue_obj))
