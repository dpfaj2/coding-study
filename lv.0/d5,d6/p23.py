#피자 나눠 먹기(2)
def solution(n):
    a=0
    b=0
    c=0
    for num in range(min(6,n),1,-1):
        if n%num == 0 and 6%num == 0:
            a = num
            b = 6//num
            c = n//num
            return (a*b*c)//6
    if a == 0:
        return n