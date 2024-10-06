#합성수 찾기
def solution(n):
    measure_count = 0
    cm_count = 0
    for num1 in range(2,n+1):
        for num2 in range(1,num1+1):
            if num1%num2 == 0:
                measure_count += 1
        if measure_count >= 3:
            cm_count += 1
        measure_count = 0
    return cm_count