#소인수부해
def solution(n):
    arg = []
    re_list = []
    pf = []
    for num in range(2,n+1):
        if n%num == 0:
            arg.append(num)
    
    for num1 in arg:
        for num2 in arg:
            if num1*num2 in arg:
                re_list.append(num1*num2)
    re_list = list(set(re_list))
    for num in re_list:
        arg.remove(num)
    return arg