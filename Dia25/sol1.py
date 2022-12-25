f = open('input.txt')
lines = [i.strip() for i in f.readlines()]

def SNAFU_to_dec(num: str):
    num = num[::-1]
    final_num = 0
    for i,c in enumerate(num):
        if c == '=':
            final_num += -2*(5**i)
        elif c == '-':
            final_num += -1*(5**i)
        else:
            final_num += int(c)*(5**i)
    return final_num

def dec_to_SNAFU(num: int):
    processed_num = num 
    digits = []
    i = 0
    while processed_num > 0:
        digits.append(processed_num%5)
        processed_num = processed_num//5
    digits.append(0)
    snafu_num = ''
    for i,d in enumerate(digits):
        if d == 3:
            snafu_num += '='
            digits[i+1] += 1
        elif d == 4:
            snafu_num += '-'
            digits[i+1] += 1
        elif d == 5:
            snafu_num += '0'
            digits[i+1] += 1
        else:
            snafu_num += str(d)
    snafu_num = snafu_num[::-1]
    if snafu_num[0] == '0':
        snafu_num = snafu_num[1:]
    return snafu_num


dec_nums = [SNAFU_to_dec(i) for i in lines]
total_sum = sum(dec_nums)
print(dec_to_SNAFU(total_sum))