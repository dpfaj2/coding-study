#문자열 정렬하기(1)
from string import ascii_lowercase
def solution(my_string):
    alphabet = list(ascii_lowercase)
    answer = []
    for num in my_string:
        if num in alphabet:
            pass
        else:
            answer.append(int(num))
    return sorted(answer)