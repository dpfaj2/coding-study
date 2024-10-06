#가까운 수
def solution(array, n):
    # 배열의 요소들과 n의 차이를 계산하여 절대값 기준으로 정렬
    return min(array, key=lambda x: (abs(x - n), x))

#abs에 key값이 있으면 array로 전달 받은 요소를 하나씩 key 함수에 넣어서 검사함
'''
ex
array = [3,10,20]
n = 20
일 때
반환되는 요소는 17, 10, 0 이므로 가장작은 0에 대응되는 20이 반환됨'''