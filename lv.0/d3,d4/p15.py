#세균 증식
def solution(n, t):
    for num in range(1,t+1):
        n *= 2
    return n