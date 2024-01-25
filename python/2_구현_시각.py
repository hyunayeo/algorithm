'''
 00시 00분 00초 ~ N시 59분 59초 까지
 3이 하나라도 포함되는 모든 경우의 수를 출력
'''

N = int(input())
count = 0
for h in range(0, N + 1):
    for m in range(0, 60):
        for s in range(0, 60):
            if "3" in str(h) + str(m) + str(s):
                count += 1
print(count)
