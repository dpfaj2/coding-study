#최댓값 만들기(2)
def solution(numbers):
    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    max_num1 = max(numbers)
    numbers.remove(max_num1)
    max_num2 = max(numbers)
    
    min_num1 = min(numbers)
    numbers.remove(min_num1)
    min_num2 = min(numbers)
    
    return max(max_num1*max_num2,min_num1*min_num2)
###
def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0]*numbers[1], numbers[-1], numbers[-2])