#숫자 찾기
def solution(num, k):
    num_str = str(num)
    if str(k) in num_str:
        num_list = list(num_str)
        return num_list.index(str(k))+1
    else:
        return -1