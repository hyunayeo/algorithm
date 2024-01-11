def recur(n: int) -> int:
    """재귀를 제거한 함수 recur"""
    if memo[n + 1] != None:
        print(memo[n + 1], end="")  # 메모를 출력
    else:
        if (n > 0):
            recur(n - 1)
            print(n)
            recur(n - 2)
            memo[n + 1] = f'{memo[n]}{n}\n{memo[n - 1]}'  # 메모화
        else:
            memo[n + 1] = ""  # 메모화: recur(0),recur(-1)은 빈 문자열


if __name__ == '__main__':
    x = int(input('정수값을 입력하세요.: '))
    memo = [None for _ in range(x + 2)]
    recur(x)
