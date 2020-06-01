# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:15:34 2020

@author: Palash
"""

class ArrayStack(object):
    """Represents a Stack ADT"""
    def __init__(self):
        """
        Constructor to initialize a stack
        """
        self.stack = []
        
    def __len__(self):
        """
        Returns the length of (number of elements in) the stack
        """
        return len(self.stack)
    
    def is_empty(self):
        """
        Returns True if stack is empty, False otherwise
        """
        return len(self.stack) == 0
    
    def push(self, data):
        """
        Pushes an element on top of the stack
        """
        self.stack.append(data)
        
    def top(self):
        """
        Returns the element on top of the stack without mutating the stack
        """
        if self.is_empty():
            raise EmptyError('Stack is empty')
        else:
            return self.stack[-1]
        
    def pop(self):
        """
        Removes the top element of the stack and returns the element
        """
        if self.is_empty():
            raise EmptyError('Stack is empty')
        else:
            return self.stack.pop()
        
    def __str__(self):
        """
        Returns the stack in the form of a string
        For example: [1,2,3] will be returned as '[1,2,3]'
        """
        return str(self.stack)
        
    
if __name__ == '__main__':
    stack_obj = ArrayStack()
    stack_obj.push(5)
    stack_obj.push(57)
    stack_obj.push(46)
    stack_obj.push(5327)
    stack_obj.push(5778)
    stack_obj.is_empty()
    stack_obj.top()
    stack_obj.pop()
    print(stack_obj)
    # to checck if str modifies the stack and converts it inot a string
    # IT DOESN'T!
    stack_obj.push(5)
    stack_obj.push(57)
    stack_obj.push(46)
    stack_obj.push(5327)
    stack_obj.push(5778)
    stack_obj.is_empty()
    stack_obj.top()
    stack_obj.pop()
    print(stack_obj)
    print(len(stack_obj))
