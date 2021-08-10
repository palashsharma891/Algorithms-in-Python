#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 12:13:40 2021

@author: palash
"""


def dfs(root):
    if root is None:
        return
    else:
        print(root.val)
        dfs(root.left)
        dfs(root.right)
