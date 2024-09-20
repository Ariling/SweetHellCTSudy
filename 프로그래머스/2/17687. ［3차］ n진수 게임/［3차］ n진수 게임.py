def convert_base(num, base):
    if num == 0:
        return '0'
    digits = '0123456789ABCDEF'
    result = ''
    while num:
        result = digits[num % base] + result
        num //= base
    return result

def solution(n, t, m, p):
    answer = ''
    cnt = 0
    num = 0
    idx = 1
    
    while cnt < t:
        converted_num = convert_base(num, n)
        for digit in converted_num:
            if idx == p:
                answer += digit
                cnt += 1
                if cnt == t:
                    break
            idx += 1
            if idx > m:
                idx = 1
        if cnt == t:
            break
        num += 1
    
    return answer