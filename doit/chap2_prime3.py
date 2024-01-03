"""
1000 이하의 소수 구하기
제곱근 이하의 소수로 나누어 떨어지지 않는 수 -> 소수
--
python 에서는 for-else, while-else 문법 사용 가능
for, while 에 break가 있어서 반복문이 종료될 경우 else 실행 안됨.
break 가 실행되지 않고 반복문이 종료될 경우 else 실행됨.
"""
count = 0               # 곱셈과 나눗셈을 합한 연산 횟수
ptr = 0                 # 찾은 소수의 개수
prime = [None] * 500    # 소수를 저장하는 배열

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):     # 홀수만 대상으로 설정
    i = 1
    while prime[i] ** 2 <= n:   # 제곱근보다 작은 수일 때
        count += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:                       # 끝까지 나누어 떨어지지 않으면 소수에 등록
        prime[ptr] = n
        ptr += 1
        count += 1
for i in range(ptr):
    print(prime[i])

print(f'곱셈과 나눗셈을 실행한 횟수: {count}')