# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:14:29 2020

@author: Palash
"""

class Deque(object):
    """ Represents a  Deque ADT"""
    def __init__(self):
        """
        Constructor to initialize the deque
        """
        self.deque = []
        
    def add_first(self, data):
        """
        Adds an element to the front of the deque
        """
        self.deque.insert(0, data)
        
    def add_last(self, data):
        """
        Adds an element at the end of the deque
        """
        self.deque.append(data)
        
    def delete_first(self):
        """
        Deletes the first element in the deque
        """
        self.deque.pop(0)
        
    def delete_last(self):
        """
        Deletes the last element in the deque
        """
        self.deque.pop()
        
    def first(self):
        """
        Returns the first element in the deque
        """
        return self.deque[0]
        
    def last(self):
        """
        Returns the last element in the deque
        """
        return self.deque[-1]
    
    def is_empty(self):
        """
        Returns True if deque is empty, False otherwise
        """
        return len(self.deque) == 0
    
    def __len__(self):
        """
        Returns the length of (number of elements in) the deque
        """
        return len(self.deque)
    
    def __str__(self):
        """
        Returns the deque in the form of a string
        For example: [1,2,3] is returned as '[1,2,3]'
        """
        return str(self.deque)
    
if __name__ == '__main__':
    deque_obj = Deque()
    deque_obj.add_first(1)
    deque_obj.add_first(234)
    deque_obj.add_first(123)
    deque_obj.add_last(456)
    print(deque_obj)
    deque_obj.delete_first()
    deque_obj.delete_last()
    print(deque_obj.first())
    print(deque_obj.is_empty())
    print(deque_obj.last())
    print(deque_obj)
