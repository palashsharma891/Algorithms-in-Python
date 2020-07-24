#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 17:50:29 2020

@author: palash
"""


from array import array
from linkedqueue import Queue

class BPriorityQueue:
    def __init__(self, numLevels):
        self.qsize = 0
        self.qlevels = array(numLevels)
        for i in range(numLevels):
            self.qlevels[i] = Queue()
            
    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self.qsize)
    
    def enqueue(self, item, priority):
        assert priority >= 0 and priority < len(self.qlevels), "Invalid priority level"
        self.qlevels[priority].enqueue(item)
        
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        i = 0
        p = len(self.qlevels)
        while i < p and not self.qlevels[i].isEmpty():
            i += 1
        return self.qlevels[i].dequeue()
