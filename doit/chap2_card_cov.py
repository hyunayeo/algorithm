"""
10진수 정수값을 입력받아 2~36진수로 변환하여 출력하기
"""

def card_conv(x: int, r: int) -> str:
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while x > 0:
        d += dchar[x % r]  # 해당하는 문자를 꺼내 결합
        x //= r
    return d[::-1]  # 역순으로 반환


if __name__ == '__main__':
    print('10진수를 n 진수로 변환합니다.')
    while True:
        while True:
            n = int(input("음이 아닌 정수를 입력하세요.: "))
            if n > 0:
                break
        while True:
            cd = int(input("어떤 진수로 변환할까요?: "))
            if 1 < cd < 37:
                break
        print(f'{cd}진수로는 {card_conv(n, cd)}')
        retry = input('한번더 변환할까요?(y..예/n..아니오)')
        if retry in {'N', 'n'}:
            break
