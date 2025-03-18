# https://www.acmicpc.net/problem/1018

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

result = float('inf')

for N in range(n - 7):
    for M in range(m - 7):
        
        white_first = 0
        black_first = 0
        
        for row in range(N, N + 8, 1):
            for col in range(M, M + 8, 1):
                if (row + col) % 2 == 0:
                    if board[row][col] == 'W':
                        black_first += 1
                    else: # B
                        white_first += 1
                else:                        
                    if board[row][col] == 'B':
                        black_first += 1
                    else:
                        white_first += 1
                        
        result = min(white_first, black_first, result)
                
print(result)
