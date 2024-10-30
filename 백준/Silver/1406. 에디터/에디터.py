import sys
input = sys.stdin.readline

word_left = list(input().rstrip())
word_right = []
N = int(input())
for _ in range(N):
    edit = list(input().rstrip())
    if edit[0] == 'L' and word_left:
        word_right.append(word_left.pop())
    if edit[0] == 'D' and word_right:
        word_left.append(word_right.pop())
    if edit[0] == 'B' and word_left:
        word_left.pop()
    if edit[0] == 'P':
        word_left.append(edit[2])
print(''.join(word_left + word_right[::-1]))