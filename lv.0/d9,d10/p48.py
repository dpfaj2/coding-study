#삼각형의 완성조건(1)
def solution(sides):
    hypotenuse = max(sides)
    sides.remove(hypotenuse)
    if hypotenuse < sides[0] + sides[1]:
        return 1
    else:
        return 2