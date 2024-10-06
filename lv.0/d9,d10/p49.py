#약수 구하기
def solution(n):
    divisor = []
    for num in range(1,n+1):
        if n%num == 0:
            divisor.append(num)
    divisor.sort()
    return divisor