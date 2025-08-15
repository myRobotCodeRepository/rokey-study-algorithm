import sys
from collections import deque

input = sys.stdin.readline

n, m = input().split()
n = int(n)
m = int(m)
mazeMat = []

# 미로 설정
# for i in range(n):
#     # dummy = input()
#     # dummyList = []
#     # for j in range(m):
#     #     dummyList.append(int(dummy[j]))
#     # mazeMat.append(dummyList)
#     # 최적화 작업 - 근본적인 성능 문제가 아님
#     mazeMat.append([int(char) for char in input().strip()])
# 최적화 작업 - input 전체를 list comprehension으로
mazeMat = [list(map(int, input().strip())) for _ in range(n)]

# BFS
pos = ()
dummyDeque = deque([(0,0)])
arrive = (n-1, m-1)
# distDict = {(0,0): 1}
# Dictation이 오히려 해시/튜플 생성 오버헤드가 커서 성능 저하를 불러일으킬 수 있다고 함.
dist = [[0]*m for _ in range(n)]
dist[0][0] = 1
udlr = [(-1,0), (1,0), (0,-1), (0,1)]
flag = False
while dummyDeque:
    pos = dummyDeque.popleft()
    mazeMat[pos[0]][pos[1]] = 0
    for ori in udlr:
        mov = (pos[0]+ori[0], pos[1]+ori[1])
        if mov[0] in range(n) and mov[1] in range(m) and mazeMat[mov[0]][mov[1]] == 1:
            dummyDeque.append(mov)
            dist[mov[0]][mov[1]] = dist[pos[0]][pos[1]] + 1
            if mov == arrive: 
                flag = True # 연산자 잘못 넣음(== => =)
                break
    if flag == True: break

print(dist[arrive[0]][arrive[1]])