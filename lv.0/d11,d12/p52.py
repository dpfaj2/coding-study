#외계행성의 나이
def solution(age):
    age_alphabet = 'abcdefghijklnmopqrstuvwxyz'
    reall_age = ''
    age_str = str(age)
    for num in age_str:
        reall_age += age_alphabet[int(num)]
        
    return reall_age