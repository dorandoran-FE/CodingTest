import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split())) 


M = inst(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

N_list.sort()


# M 리스트 for 문 
for i in M_list: 
    start = 0 
    end = N-1 # N 개 주어진 숫자 안에서 찾아야하기 때문 

    while N_list[start] <= N_list[end]:
        half = (start + end)/2

        if N_list[half] > M_list[i]:
            # 더 크다라면 작은 범위에서 찾아야함 
            end = half - 1
        elif N_list[half] < M_list[i]:
            start = half + 1
        elif
            


