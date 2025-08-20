### 단지 번호 붙히기

- 다시 풀었으나 그래도 못 품

### 안전영역

- 문제도 이해 못하고 스킵
- 최대 값 구하기 위해선 최대 (for) -> 2중 루프 -> BFS 또는 재귀

#### 정답

```python
import sys
sys.setrecursionlimit(100000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def sink_DFS(x,y,h):
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]

        if (0 <= nx < N) and (0 <= ny < N) and not sink_table[nx][ny] and water_board[nx][ny] > h:
            sink_table[nx][ny] = True
            sink_DFS(nx, ny, h)


N = int(sys.stdin.readline())
water_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 1
for k in range(max(map(max, water_board))):
    sink_table = [[False]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if water_board[i][j] > k and not sink_table[i][j]:
                count += 1
                sink_table[i][j] = True
                sink_DFS(i, j, k)
    ans = max(ans, count)

print(ans)
```
