#최빈값 구하기
'''
from collections import Counter

def solution(array):
    counter_list = []
    mode = 0
    count_num = Counter(array)
    for num_key in count_num:
        counter_list.append(count_num[num_key])
    counter_list = sorted(counter_list)
    for num in counter_list:
        if num > mode:
            mode = num
            counter_list.pop(counter_list.index(num))
    if len(counter_list) != 0:
        if max(counter_list) == mode:
            mode = -1
    
    return mode
#이미 counter 객체를 통해 각 숫자의 빈도를 파악하고 있으므로 counter_list는 불필요함
#중복 최빈값 처리가 명확하지 않아 의도대로 작동하지 않을 수도 있음
#리스트에서 pop으로 요소를 제거하는 방식은 필요 이상으로 복잡하고 버그 유발 가능성이 있음
'''
from collections import Counter

def solution(array):
    count_num = Counter(array)
    max_num = max(count_num.values())
    mode = []
    for key,value in count_num.items(): #items은 튜플로 전달함
        if max_num == value:
            mode.append(key)
    if len(mode) > 1:
        return -1
    else:
        return mode[0]
