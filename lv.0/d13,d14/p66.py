#문자열 정렬하기(2)
def solution(my_string):
    l_string = my_string.lower()
    l_string = sorted(l_string)
    answer = ''
    for string in l_string:
        answer+= string
    return answer