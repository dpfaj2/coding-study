#팩토리얼
def solution(n):
    n_f = 1
    next_num = 2
    while n_f*next_num < n:
        if n == 1:
            return 1
        n_f *= next_num
        next_num += 1
    if n_f*next_num == n:
        return next_num
    return next_num-1