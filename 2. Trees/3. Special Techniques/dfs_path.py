#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 12:16:09 2021

@author: palash
"""


def dfs(root, path):
    if root is None:
        return
    else:
        print(root.val)
        path.append(root) # add to path
        dfs(root.left, path)
        dfs(root.right, path)
        path.pop() # remove while backtracking
