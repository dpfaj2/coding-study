#컨트롤 제트
def solution(s):
    s_sum = 0
    s = s.split(' ')
    
    for num in range(len(s)):
        if s[num] != 'Z':
            s_sum += int(s[num])
            
        elif s[num] == 'Z':
            s_sum -= int(s[num-1])
    return s_sum