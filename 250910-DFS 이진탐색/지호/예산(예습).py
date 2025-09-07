# https://www.acmicpc.net/problem/2512
import sys

CITIES = int(sys.stdin.readline())
NEED_BUDGETS = list(map(int, sys.stdin.readline().split())) # 각 시가 필요한 예산 잘라서 리스트로 변경함 
NEED_BUDGETS.sort() # 작은 순서대로 정렬

FULL_BUDGET = int(sys.stdin.readline()) # 넘으면 안됨 

# ✨ 답을 구하려면 호출을 해야함  
def binary():
    # 최초 최대 최소 세팅 
    START = 0 # ✨ 최소 값이 아니라 0 부터 
    END =max(NEED_BUDGETS)

    # MIN이 아니라 0 부터 시작하는 것 
    while START<=END:
        # 첫번째 중앙값을 구하기 
        MID = (START+END)//2 
        PRE_TOTAL_BUDGET = 0 # 예산의 합 
        
        # ✨ 이 부분이 제일 중요. 중앙값 또는 필요 예산을 비교해서 넣어주는 부분 
        for CITY in range(CITIES):
            # 더 작은 값을 넣어줌 
            if NEED_BUDGETS[CITY] >= MID: # 중앙값 >= 도시 예산 (더 많이 받음) 
                PRE_TOTAL_BUDGET += MID # 중앙값 더 함 
            else:
                PRE_TOTAL_BUDGET += NEED_BUDGETS[CITY] # 중앙값 < 도시 예산 (못 받음) 증앙 값으로
        
        if PRE_TOTAL_BUDGET <= FULL_BUDGET: 
            # 아직 더 남음 
            # 앞에값 뒤로 
            START = MID +1
        else:
            END = MID - 1
            
            
            
    return END


print(binary()) # 중앙값이 정답이겠지 
        

