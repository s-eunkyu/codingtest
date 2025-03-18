# https://www.acmicpc.net/problem/2839

import sys

input = sys.stdin.readline

n = int(input()) # need to deliver

result = -1
cnt = n // 3

for cnt_3 in range(cnt + 1):
    cnt_5 = (n - (3 * cnt_3)) // 5
    
    if n == 3 * cnt_3 + 5 * cnt_5:
        if result == - 1:
            result = cnt_3 + cnt_5
        else:
            result = min(result, cnt_3 + cnt_5)
    
print(result)
