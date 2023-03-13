#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
1. 원숭이는 멍멍이보다 키가 작다. 
2. 원숭이가 멍멍이를 쓰다듬으려면 둘의 키가 같아야 한다.
3. 원숭이는 키의 양을 1cm 씩만 조절할 수 있다. 
    3-1. 예를 들어 오늘 키를 5cm 만큼 늘렸다면, 내일은 키를 4cm, 5cm, 6cm 중 하나만큼 키를 늘릴 수 있다. 
    3-2. 늘릴 수 있는 키의 양은 음수가 될 수 없다. 
4. 첫째 날과 마지막 날에는 무조건 1cm 만큼 늘릴 수 있다.

현재 원숭이와 멍멍이의 키가 주어졌을 때, 원숭이가 매일 키를 늘려서 멍멍이와 키가 같아지는 최소의 일수를 구하는 프로그램을 작성하시오.

45, 49 -> 3
45, 50 -> 4
'''
import sys

a, b = map(int, sys.stdin.readline().split())  # 원숭이, 멍멍이

diff = b - a

if diff == 0:
    print(diff)

else:
    if diff**0.5 % 1 == 0:
        print(2*int(diff**0.5)-1)
    else:
        # print(int(diff**0.5)) = 2
        # diff**0.5 +1 이상 diff**2 + int(diff**0.5) 이하
        if int(diff**0.5)**2 <= diff & diff <= int(diff**0.5)**2 + int(diff**0.5):
            print(2*int(diff**0.5))
        else:
            print(2*(int(diff**0.5)+1)-1)
