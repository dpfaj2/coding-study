#짝수는 싫어요
def solution(n):
    answer = []
    for num in range(1,n+1):
        if num%2 !=0:
            answer.append(num)
        
    
    return sorted(answer)