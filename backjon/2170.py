'''
선 긋기

list의 max 값이 주어진 데이터의 범위 안에 있는지 for 돌면서 검사

[1] 시간 초과 

반례 : 음수 생각 안함
'''
import sys


def solution(arr):
    answers = []
    arr.sort(key=lambda x: (x[0], x[1]))
    min, max = arr[0][0], arr[0][1]

    answer = 0
    pair_temp = []
    for a, b in arr:
        if max >= a:
            if max <= b:
                max = b
        else:
            pair_temp.append(min)
            pair_temp.append(max)
            answers.append(pair_temp)
            pair_temp = []
            min, max = a, b

    pair_temp.append(min)
    pair_temp.append(max)
    answers.append(tuple(pair_temp))

    for a, b in answers:
        answer += b-a
    print(answer)
    return 0


cnt = int(input())
arr = []

for _ in range(cnt):
    tmp = []
    a, b = list(map(int, sys.stdin.readline().split()))
    tmp.append(a)
    tmp.append(b)
    arr.append(tmp)

solution(arr)
