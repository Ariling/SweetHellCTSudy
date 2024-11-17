from math import gcd
def solution(arrayA, arrayB):
    # 이거 근데... 약수를 해서 하면 난리날 것 같은데.. 
    # arrayA는 최대공약수를 찾아야 하고... 아닌가...? 공약수여야 하나..?
    # B는 일단 약수들을 다 구한다음에 가야할 것 같은데 비교하면서
    # 안 겹치는 느낌으로 가야할 것 같은데.. 이러면 시간초과 나지 않나..?
    answer = 0
    def gcd(a,b):
        while b:
            a,b = b, a%b
        return a
    def get_array_gcd(arr):
        arr.sort()
        result = arr[0]
        for i in range(1, len(arr)):
            result = gcd(result, arr[i])
        return result
    gcd_A = get_array_gcd(arrayA)
    gcd_B = get_array_gcd(arrayB)
    isB = False
    isA = False
    for B in arrayB:
        if B % gcd_A == 0:
            isA = False
            break
        else:
            isA = True
    for A in arrayA:
        if A % gcd_B == 0:
            isB = False
            break
        else:
            isB = True
    answer = max(gcd_A if isA else 0, gcd_B if isB else 0)
    return answer