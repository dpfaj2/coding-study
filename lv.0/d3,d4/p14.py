#짝수 홀수 개수
def solution(num_list):
    even_count = 0
    odd_count = 0
    count_list = []
    for num in num_list:
        if num%2 == 0:
            even_count += 1
        else:
            odd_count += 1
    count_list.append(even_count)
    count_list.append(odd_count)
    return count_list