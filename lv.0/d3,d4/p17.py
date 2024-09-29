#중복된 숫자 개수
from collections import Counter

def solution(array, n):
    c = Counter(array)
    return c[n]