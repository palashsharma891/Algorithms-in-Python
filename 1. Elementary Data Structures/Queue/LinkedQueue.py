# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 11:23:01 2020

@author: Palash
"""

class Node(object):
    """ Represents a node in the linked list"""
    def __init__(self, data):
        """
        Constructor to initialize the node
        """
        self.data = data
        self.next = None
        
class LinkedQueue(object):
    """Represents the Queue ADT, implemented using a linked list"""
    def __init__(self):
        """
        Constructor to initalize the queue
        """
        self.head = None
        self.tail = None
        self.size = 0
        
    def __len__(self):
        """
        Getter for the size of the queue
        Returns the length of (number of elements in) the queue
        """
        return self.size
    
    def is_empty(self):
        """
        Returns True if the queue is empty, False otherwise
        """
        return self.size == 0
    
    def enqueue(self, data):
        """
        Adds an element at the end of the queue
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
            
    def get_head(self):
        """
        Returns the front element in the queue
        """
        if self.is_empty():
            raise ValueError('Queue is empty')
        else:
            return self.head.data
        
    def get_tail(self):
        """
        Returns the last element in the queue
        """
        if self.is_empty():
            raise ValueError('Queue is empty')
        else:
            return self.tail.data
        
    def dequeue(self):
        """
        Removes(unlinks) and returns the last element in the queue
        """
        if self.is_empty():
            raise ValueError('Queue is empty')
        else:
            removed = self.head
            self.head = self.head.next # unlinks the current head of the list
            self.size -= 1
            return removed
        
    def printQueue(self):
        """
        Returns the elements in the queue in the form of a list
        """
        temp = self.head
        queue = []
        while temp:
            queue += [temp.data]
            temp = temp.next
        return queue
            
    
if __name__ == '__main__':
    queue_obj = LinkedQueue()
    queue_obj.enqueue(5)
    queue_obj.enqueue(234)
    print(queue_obj.is_empty())
    print(queue_obj.printQueue())
    print(queue_obj.get_head())
    print(queue_obj.get_tail())
    queue_obj.enqueue(546)
    queue_obj.enqueue(7)
    print(queue_obj.printQueue())
    print(queue_obj.get_head())
    print(queue_obj.get_tail())
    queue_obj.dequeue()
    print(queue_obj.printQueue())
    print(len(queue_obj))
