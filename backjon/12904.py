'''
A와 B
[ S -> T ]
1. 문자열 + 'A'
2. 문자열을 뒤집고 + 'B'

B, ABBA
B
BA
ABB
ABBA (True)

S.len() == T.len() 때만 검사하고 이면 1 아니면 0

반례)
A
AAAAAAAB
'''


def isSame(a, b):
    if a == b:
        return True
    return False


def solution(list):
    a = list[0][0]  # A
    b = list[1][0]  # ABBA

    while len(a) <= len(b):
        if len(a) == len(b):
            if isSame(a, b):
                print(1)
                return 1

        if b[-1] == 'A':
            b = b[:-1]
        else:
            b = b[:-1]
            b = b[::-1]

    print(0)
    return 0


arr = []
for _ in range(2):
    arr.append(list(map(str, input().split())))
solution(arr)
