import random  # random 모듈은 무작위로 숫자 생성 관련 모듈이다.

a1 = "오늘도 행복하세요."
a2 = "폭염 주의하세요."
a3 = "오늘 로또를 사세요."
a4 = "당신은 천재에요."
a5 = "영화 무료 쿠폰을 보내드립니다."
# 위의 문자열을 리스트로 구현해 보세요.
print(":::오늘의 운세:::")
input("엔터를 누르면 시작됩니다.")
c = random.randint(1, 5)
if c == 1:
    d = a1
elif c == 2:
    d = a2
elif c == 3:
    d = a3
elif c == 4:
    d = a4
else:
    d = a5
print('-------------------')
print(d)
print('-------------------')
