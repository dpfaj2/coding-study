#문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for string in my_string:
        answer += string*n
    
    return answer