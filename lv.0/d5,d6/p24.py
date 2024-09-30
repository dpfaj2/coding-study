#피자 나눠 먹기(3)
def solution(slice,n):
    if slice > n:
        return 1
    elif n%slice == 0:
        return n//slice
    else:
        return n//slice + 1