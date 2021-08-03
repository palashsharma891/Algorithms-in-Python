#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:47:04 2021

@author: palash
"""


def reverseTree(root):
    if root is None:
        return
    
    else:
        reverseTree(root.left)
        reverseTree(root.right)
        root.left, root.right = root.right, root.left
