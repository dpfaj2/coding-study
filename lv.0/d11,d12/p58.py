#배열 회전시키기
def solution(numbers, direction):
    if direction == 'right':
        remove_num = numbers[-1]
        numbers.pop(-1)
        numbers.insert(0,remove_num)
    elif direction == 'left':
        remove_num = numbers[0]
        numbers.pop(0)
        numbers.append(remove_num)
    return numbers