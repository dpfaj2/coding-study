#모음 제거
def solution(my_string):
    vowel = ['a','e','i','o','u']
    remove_string = ''
    for string in my_string:
        if string not in vowel:
            remove_string += string

    return remove_string