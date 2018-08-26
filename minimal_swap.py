#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the lilysHomework function below.
from copy import deepcopy


def lilysHomework(arr):
    arr_sort = sorted(arr)
    arr_sort_reverse = list(reversed(arr_sort))
    return min(minimal_swap(arr_sort, arr), minimal_swap(arr_sort_reverse, arr))


def minimal_swap(arr_sort, arr):
    step = 0
    d = {}
    for i in range(len(arr)):
        d[arr[i]] = i
    for i in range(len(arr)):
        if(d[arr[i]] == -1):
            continue

        head = arr[i]
        x = head
        y = arr_sort[i]
        this_loop = 0
        d[x] = -1
        while y != head:
            x = y
            y = arr_sort[d[x]]
            d[x] = -1
            this_loop = this_loop + 1
        step = step + this_loop
    return step

