import math
import os
import random
import re
import sys

#
# Complete the 'getMaxCharCount' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. 2D_INTEGER_ARRAY queries
#

def getMaxCharCount(s, queries):
    for i in range(len(queries)):
        for j in range(len(queries)):
           #a=queries[i][j]
          # print(a)
           res_s=s[queries[i][j]]
           max='A'
           for _ in range(len(res_s)):
               if (s[_] > max):
                   max = s[_]
                   print(max)
          # print(s.queries[i][j])

    # queries is a n x 2 array where queries[i][0] and queries[i][1] represents x[i] and y[i] for the ith query.


n = int(input().strip())

s = input()

q = int(input().strip())

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

getMaxCharCount(s,queries)