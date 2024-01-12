def move(no: int, x: int, y: int):
    # no 개를 x 에서 y로 옮긴다
    if no > 1:
        move(no - 1, x, 6 - x - y)
    print(f'원반 {no}을 {x}기둥에서 {y}기둥으로 옮김')
    if no > 1:
        move(no - 1, 6 - x - y, y)


if __name__ == '__main__':
    print("하노이의 탑")
    n = int(input("원반의 개수: "))
    move(n, 1, 3)
