#인덱스 바꾸기
def solution(my_string, num1, num2):
    string = ''
    first_str = my_string[num1]
    second_str = my_string[num2]
    string_list = list(my_string)
    string_list[num1] = second_str
    string_list[num2] = first_str
    for s in string_list:
        string += s
    return string