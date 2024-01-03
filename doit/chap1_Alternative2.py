print('+ 와 -를 번갈아 n개 출력합니다')
n = int(input('n값 : '))
for i in range(0, n // 2):
    print("+-", end="")
if n % 2 != 0:
    print("+")
