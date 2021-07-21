#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 10:55:59 2021

@author: palash
"""


def treeSum(root):
    if root is None:
        return 0
    else:
        leftSum = treeSum(root.left)
        rightSum = treeSum(root.right)
        return root.data + leftSum + rightSum

'''
1. Finding one or more base cases

2. Calling the same function on the left subtree

3. Calling the same function on the right subtree

4. Joining the results
'''
