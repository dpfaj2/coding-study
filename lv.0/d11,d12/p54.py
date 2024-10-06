#모스부호(1)
def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    solution_str = ''
    sample_str = ''
    for string in letter + ' ':
        while True:
            sample_str += string
            if string == ' ':
                solution_str += morse[sample_str.replace(' ','')]
                sample_str = ''
                break

            else:
                break
    return solution_str