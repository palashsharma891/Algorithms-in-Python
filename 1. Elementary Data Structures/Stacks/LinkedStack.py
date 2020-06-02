# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 10:54:10 2020

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
        
class LinkedStack(object):
    """Represents the Stack ADT, implemented using a linked list"""
    def __init__(self):
        """
        Constructor to initalize the stack
        """
        self.head = None
        self.size = 0
        
    def __len__(self):
        """
        Getter for the size of the stack
        Returns the length of (number of elements in) the stack
        """
        return self.size
    
    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise
        """
        return self.size == 0
    
    def push(self, data):
        """
        Adds an element on top of the stack
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def top(self):
        """
        Returns the element last inserted in the stack
        """
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            return self.head.data
        
    def pop(self):
        """
        Removes(unlinks) and returns the top element in the stack
        """
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            popped = self.head
            self.head = self.head.next # unlinks the current head of the list
            return popped
        
    def printStack(self):
        """
        Prints the elements in the stack
        """
        temp = self.head
        stack = []
        while temp:
            stack += [temp.data]
            temp = temp.next
        return stack
            
    
if __name__ == '__main__':
    stack_obj = LinkedStack()
    stack_obj.push(5)
    stack_obj.push(234)
    print(stack_obj.is_empty())
    print(stack_obj.printStack())
    print(stack_obj.top())
    stack_obj.push(546)
    stack_obj.push(7)
    print(stack_obj.printStack())
    stack_obj.pop()
    print(stack_obj.printStack())
