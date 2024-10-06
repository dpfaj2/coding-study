#진료 순서 정하기
def solution(emergency):
    # 내림차순으로 정렬하고 각 값의 순위를 매핑
    emergency_sort = sorted(emergency, reverse=True)
    rank_dict = {num: rank + 1 for rank, num in enumerate(emergency_sort)}
    
    # 원래의 emergency 리스트의 각 값에 대해 순위를 적용
    return [rank_dict[num] for num in emergency]