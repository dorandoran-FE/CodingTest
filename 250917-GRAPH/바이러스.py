# https://www.acmicpc.net/problem/2606


import sys
from collections import deque

# 컴퓨터 개수 
COMS = int(sys.stdin.readline())

# 노드의 개수 
NODES = int(sys.stdin.readline())

# 이어진 것 담는 공 배열 
CONNECTIONS = [[] for _ in range(NODES+1)]
VISITED = [False]*(COMS+1)

# 각 노드 별 연결되는 것들 정리 
for _ in range(NODES):
    PARENT, CHILD = map(int, sys.stdin.readline().split())
    CONNECTIONS[PARENT].append(CHILD) # 🎯 다음 목적지를 리스트에 저장해둠 
    CONNECTIONS[CHILD].append(PARENT)


TOTAL = 1

queue = deque([])
queue.append(1) # 1번 먼저 집어넣음 
VISITED[1] = True

while queue:
    INFECTED = queue.popleft()
    # ✨ 해당 부분- 값을 꺼내서 FOR 문 
    for NEXT_NOCE in CONNECTIONS[INFECTED]:
        if VISITED[NEXT_NOCE] == False:
            # 방문 안했음 
            TOTAL+=1
            queue.append(NEXT_NOCE)
            VISITED[NEXT_NOCE] = True
