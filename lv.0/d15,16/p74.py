#한 번만 등장한 문자
from collections import Counter
def solution(s):
    answer = ''
    a = ''
    s_dict = Counter(s)
    for key in s_dict:
        if s_dict[key] == 1:
            answer += key
    if 1 not in s_dict.values():
        return ''
    answer = sorted(answer)
    for string in answer:
        a += string
    return a