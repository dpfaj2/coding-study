#공 던지기
def solution(numbers, k):
    number = 2*(k-1)
    while number > len(numbers):
        number -= len(numbers)
    return numbers[number]