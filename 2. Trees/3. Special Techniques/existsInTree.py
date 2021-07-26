#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:43:34 2021

@author: palash
"""


def existsInTree(root, value):
    if root is None:
        return False
    else:
        leftExist = existsInTree(root.left, value)
        rightExist = existsInTree(root.right, value)
        return root.data == val or leftExist or rightExist
