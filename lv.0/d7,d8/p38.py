#양꼬치
def solution(n, k):
    service = (n*12000)//120000
    
    return (n*12000)+((k-service)*2000)
