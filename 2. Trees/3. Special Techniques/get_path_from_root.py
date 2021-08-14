#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 12:17:52 2021

@author: palash
"""


def get_path_from_root(root, val):
    def dfs(root, val, path):
        if root is None:
            return
        else:
            path.append(root) # add to path
            if root.val == val
            or dfs(root.left, path)
            or dfs(root.right, path):
                return True
            path.pop() # remove while backtracking
            return False
        
    path = []
    dfs(root, val, path)
    return path
