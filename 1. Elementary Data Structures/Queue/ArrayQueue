# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 12:15:43 2020

@author: Palash
"""

class ArrayQueue(object):
    """Represents a Queue ADT"""
    def __init__(self):
        """
        Constructor to initialize th queue
        """
        self.queue = []
        
    def __len__(self):
        """
        Returns the length of (the number of elements in) the queue
        """
        return len(self.queue)
    
    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise
        """
        return len(self.queue) == 0
    
    def first(self):
        """
        Returns the first element in the queue
        """
        return self.queue[0]
    
    def enqueue(self, data):
        """
        Adds an element to the end of the queue
        """
        self.queue.append(data)
        
    def dequeue(self):
        """
        Removes the first element from the front of the queue
        """
        return self.queue.pop(0)
        
    def __str__(self):
        """
        Returns the queue in the from of a string
        For example: [1,2,3] will be returned as '[1,2,3]'
        """
        return str(self.queue)
    

if __name__ == '__main__':
    queue_obj = ArrayQueue()
    queue_obj.enqueue(3456)
    queue_obj.enqueue(12)
    queue_obj.enqueue(3346)
    queue_obj.dequeue()
    print(queue_obj)
    queue_obj.first()
    queue_obj.is_empty
    print(queue_obj)
