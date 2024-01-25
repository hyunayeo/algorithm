N = int(input())  # 공간의 크기
plans = input().split()  # 이동 계획
# 시작 인덱스 1,1
x, y = 1, 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = {"R": 1, "L": 3, "U": 0, "D": 2}
for i in plans:
    nx = x + dx[direction[i]]
    ny = y + dy[direction[i]]
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    x, y = nx, ny
print(x, y)
"""
5
R R R U D D
"""
