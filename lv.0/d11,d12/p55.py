#구슬을 나누는 경우의 수
def solution(balls, share):
    mo = 1
    de = 1
    count_mo = 0
    count_de = 0
    for num in range(balls,0,-1):
        if count_mo < share:
            mo *= num
            count_mo += 1
        else:
            break
    for num in range(share,0,-1):
        if count_de < share:
            de *= num
            count_de += 1
        else:
            break
    return mo//de