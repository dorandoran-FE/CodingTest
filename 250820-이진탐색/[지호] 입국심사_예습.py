def solution(n, times):

    answer = 0 
    # 우선 times 배열을 정렬한다. 
    times.sort()

    # 최대 시간은 
    # times[times.size -1] X n/times.size로

    inspectorTotal = len(times)
    firstInspector = n/inspectorTotal
    endInspector = n/inspectorTotal
    minTime = times[inspectorTotal-1]*firstInspector

    while times[0]*firstInspector <= times[inspectorTotal-1]*endInspector
        firstInspector = firstInspector +1
        if endInspector -1 == 0 break




    # 중간 배열 값은 생각 안해도 되나 


    # [3, 3] 최소 <- 최대  하나씩 줄여나감 
    # [4, 2]

    # ex [1, 2, 3] 6인
    # [2, 2, 2] 최대는 6분 
    # [3, 2, 1] 4분

    # ex [1, 6, 10]
    # [2, 2, 2]
    # [3, 2, 1]
    # [4, 1, 1]
    # peopleByEachInspector가 들어간 times 길이 만큼의 배열 









    return answer