# https://www.acmicpc.net/problem/1436

import sys

input = sys.stdin.readline

n = int(input()) # Count
i = 666

while True:
    if '666' in str(i):
        n = n - 1
    
    if n == 0:
        result = i
        break
    
    i = i + 1

print(result)
