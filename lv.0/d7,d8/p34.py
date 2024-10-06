#대문자와 소문자
def solution(my_string):
    answer = ''
    for string in my_string:
        if string == string.lower():
            answer += string.upper()
        elif string == string.upper():
            answer += string.lower()
            
    
    return answer