#A로 B만들기
from collections import Counter
def solution(before, after):
    before_c = Counter(before)
    after_c = Counter(after)
    
    for key in before_c:
        if key in after_c.keys():
            if after_c[key] == before_c[key]:
                pass
            else:
                return 0
        else:
            return 0
    return 1