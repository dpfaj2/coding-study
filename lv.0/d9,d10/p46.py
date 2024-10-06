#제곱수 판별하기
from math import sqrt
def solution(n):
    if n%int(sqrt(n)) == 0:
        return 1
    else:
        return 2