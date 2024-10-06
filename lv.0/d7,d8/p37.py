#특정 문자 제거하기
def solution(my_string, letter):
    answer = ''
    for string in my_string:
        if string != letter:
            answer += string
    
    return answer