def solution(bin1, bin2):
    f_num = bin(int(bin1))
    s_num = bin(int(bin2))
    answer = f_num + s_num
    print(answer)

print(solution("10","11"))