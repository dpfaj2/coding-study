#가위 바위 보
def solution(rsp):
    win_str = ''
    for string in rsp:
        if string == "2":
            win_str += "0"
        elif string == "0":
            win_str += "5"
        elif string == "5":
            win_str += "2"
    return win_str