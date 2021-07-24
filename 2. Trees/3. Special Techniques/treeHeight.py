#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:41:57 2021

@author: palash
"""


def treeHeight(root):
    if root is None:
        return 0
    else:
        leftHeight = treeHeight(root.left)
        rightHeight = treeHeight(root.right)
        return 1 + max(leftHeight, rightHeight)
