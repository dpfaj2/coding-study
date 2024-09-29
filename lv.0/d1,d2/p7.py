#기약 분수 만들기
def solution(denum1, num1, denum2, num2):
    answer = []
    s = 0

    #통분
    denum0 = (denum1*num2) + (denum2*num1) 
    num0 = num1*num2

    #최대공약수 찾기
    for i in range(min(denum0,num0),0,-1):
        if denum0%i == 0 and num0%i == 0:
            s = i
            break
    
    #약분
    denum0 /= s
    num0 /= s
    answer.append(denum0)
    answer.append(num0)

    return answer