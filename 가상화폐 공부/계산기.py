def 더하기(x, y):
    return x + y

def 빼기(x, y):
    return x - y

def 곱하기(x, y):
    return x * y

def 나누기(x, y):
    if y != 0:
        return x / y
    else:
        return "0으로 나눌 수 없습니다."

while True:
    # 사용자로부터 입력 받기
    숫자1 = float(input("첫 번째 숫자를 입력하세요: "))
    연산자 = input("연산자를 입력하세요 (+, -, *, /): ")
    숫자2 = float(input("두 번째 숫자를 입력하세요: "))

    # 입력된 연산자에 따라 계산 수행
    if 연산자 == '+':
        결과 = 더하기(숫자1, 숫자2)
    elif 연산자 == '-':
        결과 = 빼기(숫자1, 숫자2)
    elif 연산자 == '*':
        결과 = 곱하기(숫자1, 숫자2)
    elif 연산자 == '/':
        결과 = 나누기(숫자1, 숫자2)
    else:
        결과 = "올바른 연산자를 입력하세요."

    # 계산 결과 출력
    print("결과: {}".format(결과))

    # 계속할지 여부 묻기
    계속 = input("더 계산하시겠습니까? (y/n): ")
    if 계속.lower() != 'y':
        break
