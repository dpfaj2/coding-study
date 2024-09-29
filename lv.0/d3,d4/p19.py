#중앙값 구하기
from math import floor
def solution(array):
    
    sorted_list = sorted(array)
    middle_index = floor(len(array)/2)
    
    return sorted_list[middle_index]