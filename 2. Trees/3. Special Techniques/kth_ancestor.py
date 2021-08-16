#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 12:21:38 2021

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

def kth_ancestor(root, val, k):
    path = get_path_from_root(root, val)
    if k >= len(path):
        return None
    else:
        return path[len(path)-k-1]
