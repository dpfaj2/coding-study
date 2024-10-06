#최댓값 만들기(1)
def solution(numbers):
    num_list = []
    for _ in range(2):
        num_list.append(max(numbers))
        numbers.remove(max(numbers))
    
    return num_list[0]*num_list[1]