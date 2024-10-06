#숨어있는 숫자의 덧셈(1)
import string
def solution(my_string):
    num = 0
    alphabet = list(string.ascii_letters)
    for element in my_string:
        if element in alphabet:
            pass
        else:
            num += int(element)
    return num
