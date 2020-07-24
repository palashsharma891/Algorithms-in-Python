#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 17:43:56 2020

@author: palash
"""


class PriorityQueue:
    def __init__(self):
        self.qlist = list()
        
    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self.qlist)
    
    def enqueue(self, item, priority):
        entry = PriorityQEntry(item, priority)
        self.qlist.appen(entry)
        
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        
        highest = self.qlist[i].priority
        for i in range(self.len()):
            if self.qlist[i].priority < highest:
                highest = self.qlist[i].priority
                
        entry = self.qlist.pop(highest)
        return entry.item
    
class PriorityQEntry(object):
    def __init__(self):
        self.item = item
        self.priority = priority
