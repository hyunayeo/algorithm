N = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0  # 총 그룹수
count = 0  # 포함된 모험가 수
for i in data:
    count += 1
    if i <= count:
        result += 1
        count = 0
print(result)
