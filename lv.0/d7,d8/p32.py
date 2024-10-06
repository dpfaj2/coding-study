#개미 군단
def solution(hp):
    ant_1 = 0
    ant_2 = 0
    ant_3 = 0
    ant_1 = hp//5
    hp -= ant_1*5
    if hp != 0:
        ant_2 = hp//3
        hp -= ant_2*3
        if hp != 0:
            ant_3 = hp//1
            hp -= ant_3
    return ant_1 + ant_2 + ant_3