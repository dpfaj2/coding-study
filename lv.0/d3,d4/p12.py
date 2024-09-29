#짝수 합 구하기
def solution(n):
    even = 0
    for num in range(1,n+1):
        if num%2 == 0:
            even += num

    return even