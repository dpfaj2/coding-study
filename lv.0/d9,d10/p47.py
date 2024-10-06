#순서쌍의 개수
def solution(n):
    divisor = 0
    for num in range(1,n+1):
        if n%num == 0:
            divisor += 1
    return divisor