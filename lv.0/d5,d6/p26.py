#아이스 아메리카노
def solution(money):
    glass = money//5500
    small_change = money%5500
    answer = []
    answer.append(glass)
    answer.append(small_change)
    return answer