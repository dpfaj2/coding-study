#중복된 문자 제거
def solution(my_string):
    answer = ''
    for string in my_string:
        if string not in answer:
            answer += string
    
    return answer

#set은 순서를 알 수 없음