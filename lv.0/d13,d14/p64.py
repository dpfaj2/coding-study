#369게임
def solution(order):
    order_str = str(order)
    count = 0
    for num in order_str:
        if num in ['3','6','9']:
            count += 1
    return count