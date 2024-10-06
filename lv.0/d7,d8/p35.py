#가장 큰 수 찾기
def solution(array):
    answer = []
    num_max = max(array)
    num_index = array.index(num_max)
    
    answer.append(num_max)
    answer.append(num_index)
    return answer