import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split())) # String으로 받은 값을 , 으로 잘라서 [] 리스트에 담음 
N_list.sort()




M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split())) # String으로 받은 값을 , 으로 잘라서 [] 리스트에 담음 



# M_list의 값이 N_list에 속하는지 확인하면 됨 -> 시간초과 뜸 
# 간단하게 이중 for문으로 
for m in M_list 
    chk = False

    for n in N_list
        if m == n : 
            # 속했을 때 
            print(1)
            chk = True 
            break
            # 내부 for 문 밖으로 
    if chk == False:
        print(0)
        # 끝까지 돌았는데 false 이면 그땐 0


# 좀 더 빠르게 나오도록 해야함 
# L_list를 정렬한 후, M_list의 값이 정렬한 L_list의 왼쪽 (작은 값) 이라면 앞에서부터 / 오른쪽 (큰 값)이라면 뒤에서부터


for m in M_list : 
    start = 0 
    end = N -1 

    while(start <= end) : 
        mid = (start + end) // 2 # 중앙값 

        if m > N[mid] : 
            start = mid + 1 # 숫자가 중앙 값보다 크면 큰 쪽에서 다시 (시작 포인트를 중앙 뒷편으로 넘김 )
        elif m < N[mid] : 
            end = mid - 1 # 숫자가 중앙 값 보다 작으면 앞 쪽에서 (end 포인트를 중앙 앞으로 당김)
        else : 
            start = mid
            end = mid 
            break # while 반복문에서 나옴 

    if start == mid and end == mid : 
        print(1)
    else : 
        print(0)
    

