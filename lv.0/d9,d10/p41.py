#배열의 유사도
def solution(s1, s2):
    same_count = 0
    for s1_element in s1:
        for s2_element in s2:
            if s1_element == s2_element:
                same_count += 1
    return same_count