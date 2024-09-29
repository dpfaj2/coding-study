#각 수를 2배하기
def solution(numbers):
    
    answer = []
    for num in numbers:
        answer.append(num*2)
    
    
    #리스트 컴프리헨션
    '''
    answer = [num*2 for num in numbers]
    '''
    return answer

    
    