'''
유클리드 호제법으로 최대 공약수 구하기
'''
def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


if __name__ == '__main__':
    print("두 정숫값의 최대 공약수를 구합니다.")
    x = int(input("첫 번째 정수값:"))
    y = int(input("두 번째 정수값:"))
    print(f'두 정숫값의 최대 공약수는 {gcd(x, y)}입니다.')
