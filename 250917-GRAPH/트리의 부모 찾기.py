# https://www.acmicpc.net/problem/11725

import sys
from collections import deque

# 노드의 개수 
NODES = int(sys.stdin.readline())

# 이어진 것 담는 공 배열 
CONNECTIONS = [[] for _ in range(NODES+1)]

# 각 노드 별 연결되는 것들 정리 
for _ in range(NODES):
    PARENT, CHILD = map(int, sys.stdin.readline().split())
    CONNECTIONS[PARENT].append(CHILD) # 🎯 다음 목적지를 리스트에 저장해둠 
    CONNECTIONS[CHILD].append(PARENT)


# 양쪽 방향이 아니라 1에서 낙하 ... 어떻게? 
# 안으로 집어넣어졌을 때 나오는 값이 1 멈춤 부모 

PARENT = [0]*(NODES+1)

for i in range(2, NODES+1):
    queue = deque([])
    queue.append(i) # 1번 먼저 집어넣음 
    VISITED = [False]*(NODES+1)
    VISITED[i] = True

    while queue: 
        CONNECTED_NODE = queue.popleft()
        # 4 나옴 
        for NEXT_NODE in CONNECTIONS[CONNECTED_NODE]:
            if NEXT_NODE == 1:
                # 루트임 
                print(CONNECTED_NODE) # 연결된게 부모 
                break
            else:
                VISITED[NEXT_NODE] = True
                queue.append(NEXT_NODE)

