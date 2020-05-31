# -*- coding: utf-8 -*-
"""
Created on Sun May 31 12:13:00 2020

@author: Palash
"""

class Node(object):
    """ Represents a node in a linked list"""
    def __init__(self, data):
        """
        Constructor to initalize the node
        """
        self.data = data
        self.next = None
        
class LinkedList(object):
    """ Represents a linked list of node object"""
    def __init__(self):
        """
        Constructor to initalize the linked list object
        """
        self.head = None
    
    def push(self, new_data):
        """
        Pushes a node on top of the list
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def insertAfterData(self, node_data, new_data):
        """
        Inserts an element after a given element's data in the list
        """
        current_node = self.head
        while current_node.next.data != node_data: 
            # AttributeError raised if '.data' is omitted
            # traversing until the first instance of node_data is found
            current_node = current_node.next
        new_node = Node(new_data)
        new_node.next = current_node.next
        current_node.next = new_node
        
    def insertAfterNode(self, prev_node, new_data):
        """
        Inserts an element after a given node in the list
        """
        if prev_node:                       # if the node exists, i.e. not None
            new_node = Node(new_data)
            new_node.next = prev_node.next
            prev_node.next = new_node
        else:                               # if the value of prev_node is None
            print("No such node in the list")
        
    def append(self, new_data):    
        """
        Adds a node to the end of the list
        """
        new_node = Node(new_data)
        
        if self.head is None:
            # checking if the list is empty
            self.head = new_node
            new_node.next = None
            
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            
        current_node.next = new_node
        new_node.next = None
        
    def printList(self):
        """
        Prints the linked list
        """
        temp  =self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6) 
    llist.insertAfterNode(llist.head, 5)
    llist.push(69)
    llist.push(56) 
    llist.push(17);
    llist.append(74) 
    llist.insertAfterNode(llist.head.next, 87) 
    llist.insertAfterData(74, 99)
  
    print('Created linked list is:')
    llist.printList()
    
    
