import sys
from collections import deque
r = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    m,n = map(int, r().split())
    q = deque()
    gr = [list(map(int, r().split())) for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if gr[i][j] == 1:
                q.append((i, j))
                
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0<=nx<n and 0<=ny<m and gr[nx][ny] == 0:
                q.append((nx, ny))
                gr[nx][ny] = gr[x][y] + 1
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if gr[i][j] == 0:
                print(-1)
                quit()
            ans = max(ans, gr[i][j])
            
    print(ans-1)
    
solution()