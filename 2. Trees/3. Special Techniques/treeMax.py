#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:38:02 2021

@author: palash
"""


def treeMax(root):
    if root is None:
        return float('-inf')
    else:
        leftMax = treeMax(root.left)
        rightMax = treeMax(root.right)
        return max(root.data, leftMax, rightMax)
    
