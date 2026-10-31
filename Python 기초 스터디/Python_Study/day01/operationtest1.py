number = 100
number += 10
print(number)
number -= 10
print(type(number))
number *= 10
print(number)
number /= 10
print(number)
print(type(number))
number /= 10
print(number)

a = 100
if a%2 == 0 :
    print("짝수")
else:
    print("홀수")

    a = 101
if a%2 == 0 :
    print("짝수")
else :
    print("홀수")

c = a // 2
print(c)

a = 101
if a % 2 == 0 :  # 만약 a를 2로 나눈 나머지가 0이라면
    print("짝수") # '짝수'라는 문자를 출력
else :           # 그게 아니라면,
    print("홀수") # '홀수'라는 문자를 출력

c = a // 2 # c라는 변수를 만들고 c의 값에 a를 2로 나눈 몫을 넣었음
print(c) # c 출력했을 때 나오는 값은, 101 / 2 = 50

# if 조건 :
#     조건이 맞으면 실행
# else :
#     조건이 맞지않으면 실행