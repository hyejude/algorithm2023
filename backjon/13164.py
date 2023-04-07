'''
1. 키 순서대로 일렬로 줄 세움
2. 조에서 가장 키 큰, 키 작은 --> 차이만큼 비용
3. 비용 최소. ==> 그리디..?

input 원생수, 조개수
원생 키 (원생 수대로 있음)

5 3
1 3 5 6 10

투 포인트? 조 카운트가 조개수일때까지 반복하고 (while true)
순열인가? (근데 인접 조건을 문제에서 추가했음) --> 아닐듯
1/3/5 6 10 = 0+0+5
1/3 5/6 10 = 0+2+4
1/3 5 6/10 = 0+3+0

1 3/5/6 10 = 2+0+4
1 3/5 6/10 = 2+1+0

1 3 5/6/10 = 4+0+0
^ 차이 합을 set에 담고 맨 앞이나 뒤 pop return하면 좋을 거 같은데 
조로 나누는 로직을 생각 못하겠음 --> 
DP? 하나씩 끊고 다음도 하나씩 끊고 반복하는 게 DP 같긴한데 --> 터질듯

내가 생각하는 문제에서 중요한 점
1. 한 조에 하나 이상은 있어야 한다는 것

5 2
1 3 5 6 10

* 앞 뒤로 차이를 기억할까?
* 이것도 뒤에서부터 접근할까? (이유: 뒤에 있는 숫자는 max라서)
뒤에서 접근하고 pop pop while 반복하면 되지 않을까
10 6 5 3 1

앞 diff = 5, 뒤 diff = 4
각 diff = [2,2,1,4]
1 3 5 6 (10)
앞 diff = 5, 뒤 diff = 1
1 3 (5 6) (10)

'''

import sys

n,m = map(int,sys.stdin.readline().split())
data_list = list(map(int,input().split()))
cnt = m

if m == 1 :
    print(data_list[-1]-data_list[0])

else:
    while cnt != 1:
        back_diff = data_list[-1]-data_list[-2]
        front_diff = data_list[-2]-data_list[0]

        if front_diff >= back_diff:
            
        else:


        cnt -=1



print(n,m,data_list)