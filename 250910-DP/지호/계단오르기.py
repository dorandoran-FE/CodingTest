# https://www.acmicpc.net/problem/2579 누적합! 

import sys

# 총 개수 
STAIRS = int(sys.stdin.readline())

# 빈 배열 
STARIS_ARRAY = [0]*(STAIRS)

# 누적합
DP = [0]*(STAIRS) 
# DP의 -1은 뒤에 값 

# 넘어온 값 배열에 넣기 
for i in range(STAIRS):
    STARIS_ARRAY[i] = int(sys.stdin.readline())

#-----------------세팅-----------------------------------

# 일단 먼저 집어넣기 
DP[0] = STARIS_ARRAY[0]
DP[1] = STARIS_ARRAY[0] + STARIS_ARRAY[1] 

if len(STARIS_ARRAY)>2:
    for i in range(2, STAIRS):
        # 인덱스 2번부터 STAIRS-1까지 
        DP[i] = max(DP[i-3]+STARIS_ARRAY[i-1]+STARIS_ARRAY[i],DP[i-2] + STARIS_ARRAY[i]) # 현재값은 무조건 더해야함 
                # (3칸전과 한칸전)                               2칸전                       
    print(DP[STAIRS-1])
else:
    print(sum(STARIS_ARRAY)) # 2보다 작으면 그땐 그냥 다 더하기 



""" 
+1 +1 +1 3번 나오면 안됨 
+1/ +2 까지만 가능 
            *   *
0   1   2   3   4   5 
10  20  15  25  10  20

    
1) (STAIRS-1) -2 에서 +2 하는 경우 
    (STAIRS-1) -2을 1 2로 분해 
    
    1/2
    2/1

2) (STAIRS-1) -1 에서 +1 하는 경우 
    (STAIRS-1) -1를 1 2로 분해 
    1 1 2
    1 2 1 
    2 1 1 

0 과 STAIRS-1 값은 무조건 
"""