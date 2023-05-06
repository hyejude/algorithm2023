# def dfs(graph,v,visited):
#     visited[v] = True
#     print(v, end=' ')

#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph,i,visited)


# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visited = [False]*len(graph)

# dfs(graph,1,visited)

# from collections import deque

# def bfs(graph,start,visited):
#     queue = deque([start])
#     visited[start] = True

#     while queue:
#         v = queue.popleft()
#         print(v,end=" ")
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visited = [False]*len(graph)
# bfs(graph,1,visited)


# 꼬리물기?
# import sys
# n,m = map(int, sys.stdin.readline().split())
# graph = []

# def dfs(x,y):
#     if x<=-1 or x>=n or y<=-1 or y>=m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         return True
#     return False

# for i in range(n):
#     graph.append(list(map(int, input())))

# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j):
#             result += 1
# print(result)

# 정해진 소수의 범위라 완전 탐색 가능
# dfs가 아니라 bfs였음

import sys
from collections import deque

def pour(x,y):
    if not visited[x][y]:
        visited[x][y] = True
        queue.append((x,y))

def bfs():

    while queue:
        x,y = queue.popleft()
        z = c-x-y

        # a 비어있는 경우 c 남은 양 저장
        if x == 0:
            answer.append(z)

        # x->y
        water = min(x,b-y)
        pour(x-water, y+water)
        # x->z
        water = min(x,c-z)
        pour(x-water, y)
        # y->x
        water = min(y,a-x)
        pour(x+water, y-water)
        # y->z
        water = min(y,c-z)
        pour(x, y-water)
        # z->x
        water = min(z,a-x)
        pour(x+water, y)
        # z->y
        water = min(z,b-y)
        pour(x, y+water)

a,b,c = map(int, sys.stdin.readline().split())
queue = deque()
queue.append((0,0)) # typeError

visited = [[False] * (b+1) for _ in range(a+1)]
visited[0][0] = True

answer = []

bfs()

answer.sort()
for i in answer:
    print(i, end=" ")

# 6가지 물 옮기는 방법 (x,y,z)
# water = min(x,b-y) : x->y 일때 x 전체를 옮기거나 / b 물통을 꽉 채우는 방법
# pour(x-water,y+water) : 옮긴 후 x,y 상태를 큐에 저장

# c물통 남은 양은 z=c-x-y

# visited로 (x,y) 경우의 수에 대한 중복 방지


