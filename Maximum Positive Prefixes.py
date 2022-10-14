import math
import os
import random
import re
import sys


def maxPosPrefixes(arr):
    pos,neg,new,ans,only_pos,pos_count=[],[],[],[],[],0
    pos = [num for num in arr if num > 0]
    neg = [num for num in arr if num <= 0]
    pos.sort()
    neg.sort(reverse=True)
    new=pos+neg
    ans = [sum(new[ : i + 1]) for i in range(len(new))]
    only_pos = [num for num in ans if num > 0]
    pos_count = len(only_pos)
    return pos_count

    
arr = [-3,0,2,1]     
print(maxPosPrefixes(arr))
