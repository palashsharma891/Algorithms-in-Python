#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 12:22:57 2021

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

def lca(root, val1, val2):
    path1 = get_path_from_root(root, val1)
    path2 = get_path_from_root(root, val2)
    last_common = None
    i = j = 0
    while i < len(path1) and j < len(path2):
        if path1[i] == path2[j]:
            last_common = path1[i]
            i += 1
            j += 1
        else:
            break
    return last_common
