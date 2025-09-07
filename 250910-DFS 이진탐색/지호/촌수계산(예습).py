# https://www.acmicpc.net/problem/2644 DFS/BFS

import sys
from collections import deque

### 세팅 
# 전체 사람 
ALL= int(sys.stdin.readline())

# 구해야하는 2명
A,B = map(int, sys.stdin.readline().split())

# 관계의 총 수 
REL_TOTAL = int(sys.stdin.readline())

## 각 서로의 관계를 담기위한 공 리스트 즉, 
## 따라서 ALL+1 (0, 1, 2, 3) ALL이 3일때 
FAMILY = [[] for _ in range(ALL+1)]

## 방문했는지 여부 
VISITED = [False] * (ALL+1) 

# 1촌 관계만을 나타내는 리스트 -  1의 1촌 1인덱스에 넣기/ 2의 2촌 2 인덱스 
for _ in range(REL_TOTAL):
    PARENT, CHILD = map(int, sys.stdin.readline().split())
    FAMILY[PARENT].append(CHILD) # FAMILY = [[2,3,4], [4,5,6]] FAMILY[0]의 값....
    FAMILY[CHILD].append(PARENT)



#---------------------------------------------------------------------------
def BFS(a, b):
    queue = deque([])
    queue.append([a, 0]) # 최초 값 
    VISITED[a] = True # 방문
    
    
    while queue:
        person, depth = queue.pop()
        
        if person == b:
            # 찾는 사람이면 
            return depth
        
        for next in FAMILY[person]:
            if not VISITED[next]:
                queue.append([next, depth+1])
                VISITED[next] = True # 방문표시
    
    return -1 # 없을 때 

# 주어진 사람 깊이 탐색 시작
print(BFS(A, B))


#---------------------------------------------------------------------------
## 정답을 위한 공 리스트 
result = []

# 1촌 관계만을 나타내는 리스트 -  1의 1촌 1인덱스에 넣기/ 2의 2촌 2 인덱스 
for _ in range(REL_TOTAL):
    PARENT, CHILD = map(int, sys.stdin.readline().split())
    FAMILY[PARENT].append(CHILD) # FAMILY = [[2,3,4], [4,5,6]] FAMILY[0]의 값....
    FAMILY[CHILD].append(PARENT)



def DFS(p, num):
    num+=1 #관계 카운팅 시작
    VISITED[p] = True #해당 인물 방문 완
    
    if(p==B):
        # 내가 궁금했던 부분, 이제 서로의 관계를 구해야하는 사람이 온 경우 
        # 끝내야할 듯 
        result.append(num)

    # 해당 노드 depth 끝나면 width 가로로 탐색해야함 
    for i in FAMILY[p]:
        if not VISITED[i]:
            DFS(i, num) # 방문 안했으면 깊이로 
        

# 주어진 사람 깊이 탐색 시작
DFS(A, 0) 
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)