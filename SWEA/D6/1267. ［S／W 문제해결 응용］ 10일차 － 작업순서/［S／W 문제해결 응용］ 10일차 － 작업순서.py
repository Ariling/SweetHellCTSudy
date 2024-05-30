# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''
#import sys
#sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    indegree = [0] * (v+1)
    temp_list = list(map(int, input().split()))
    for i in range(1, len(temp_list),2):
        x = temp_list[i-1]
        y = temp_list[i]
        graph[x].append(y) # 왜 이렇게 해야되는걸까? 
        indegree[y] += 1
    queue = list()
    result = []
    for i in range(1, v+1):
        if indegree[i] == 0:
           queue.append(i)
    result.append("#"+str(test_case))
    while queue:
        curr = queue.pop(0)
        result.append(str(curr))
        for i in graph[curr]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    print(' '.join(result))