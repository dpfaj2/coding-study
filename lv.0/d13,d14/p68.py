#암호 해독
def solution(cipher, code):
    str_list = []
    answer = ''
    if code == 1:
        return cipher
    else:
        for num in range(1,len(cipher)):
            if code*num-1 < len(cipher):
                str_list.append(cipher[code*num-1]) #등차 수열
    for string in str_list:
        answer += string
    return answer