import sys

N = int(sys.stdin.readline())
# 받아온 값 쪼개서 int로 바꾸고 배열 형태로 
N_list = list(map(int, sys.stdin.readline().split())) 


M = inst(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline()))

#M_list에 있는 값이 N_list에 있냐를 확인 
# N_list를 정렬하고, M_list 의 값 하나씩을 loop를 돌면서 N_list에 앞뒤 확인 

answerArray = []

N_list.sort()

startIndex = 0 
endIndex = N-1

for i in M_list :
    flag = False


    while N_list[startIndex] <= N_list[endIndex] :
        half = (startIndex + endIndex) / 2

        if N_list[half] > M_list[i] : 
            endIndex = half -1

        if N_list[half] < M_list[i] : 
            startIndex = half +1 

        if N_list[half] == M_list[i] :  # 여기서 break 
            flag = True

    if flag == True : 
        answerArray[i] = 1
    else : 
        answerArray[i] = 0





