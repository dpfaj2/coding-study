#7의 개수
from collections import Counter
def solution(array):
    count = 0
    string = ''
    for num in array:
        string += str(num)
    count = Counter(string)
    return count['7']