#2차원ㅇ로 만들기
def solution(num_list, n):
    answer = []
    count = 0
    for _ in range(len(num_list)//n):
        answer.append(num_list[n*count:n*(count+1)])
        count += 1
    return answer