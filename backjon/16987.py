'''
내구도와 무게
1. 내구도는 상대 계란의 무게만큼 깎임
2. 내구도 0이하 계란 깨짐
3. (7,5) (2,3) 계란1 내구도 7-3=4, 계란2 내구도 2-5=-3(깨짐)

1. 왼쪽부터 든다 
2. 단, 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어감, 다시 내려 놓음
3. 가장 최근 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 진행 (가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 종료)

계란 수
내구도, 무게 list
'''
from collections import deque
import sys

n = int(input())
data_list = []
answer = 0

for _ in range(n):
    tmp_data = list(map(int,input().split()))
    data_list.append(tmp_data)

data_list = deque(data_list)
print(data_list)

while data_list:
    pick_up = data_list.popleft()
    # 내구도만 변하는 것이다.
    pick_up[0] -= data_list[0][0]
    data_list[0][0] -= pick_up[0] 
    if pick_up[0] <= 0:
        if data_list[0][0] <= 0:
            answer += 2
        else:
            answer += 1
    else:
        if data_list[0][0] <= 0:
            answer += 1
        else:
            pass
        

