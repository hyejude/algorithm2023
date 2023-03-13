#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
압축되지 않은 문자열 S가 주어졌을 때, 이 문자열중 어떤 부분 문자열은 K(Q)와 같이 압축 할 수 있다. K는 한자리 정수이고, Q는 0자리 이상의 문자열이다. 
이 Q라는 문자열이 K번 반복된다는 뜻이다. 압축된 문자열이 주어졌을 때, 이 문자열을 다시 압축을 푸는 프로그램을 작성하시오.

33(562(71(9))) --> 19
123 --> 3
10342(76) --> 8
0(0) --> 0
1(1(1(1(1(1(1(0(1234567890)))))))) --> 0
1()66(5) --> 7

거꾸로 가지 않아도 돼요
'''

a = input()
temp, length = '', 0
stack = []

for val in a:
    if val == '(':
        stack.append((temp, length-1))
        length = 0  # 괄호가 또 나올 수 있어 길이 초기화
    elif val == ')':
        multiNum, preL = stack.pop()
        length = (int(multiNum) * length) + preL
    else:  # .isdigit() True
        length += 1
        temp = val
print(length)
