#숨어있는 숫자의 덧셈(2)
#.isalpha(), .isdigit()
'''
def solution(my_string):
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    my_string = my_string.split()
    
    return sum(list(map(int, my_string)))
'''
#정규표현식
'''
import re

def solution(my_string):
    num = re.findall(r'\d+', my_string)
    num = list(map(int, num))
    return sum(num)
'''