#점 위치 구하기
def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        elif dot[1] < 0:
            return 4
    elif dot[0] < 0:
        if dot[1] > 0:
            return 2
        elif dot[1] < 0:
            return 3