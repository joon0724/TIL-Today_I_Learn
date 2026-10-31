#문제 1-1. 짝수만 골라 출력하고 합계 구하기
#1부터 10까지 중 짝수만 한 줄에 출력하고, 마지막 줄에 짝수들의 합을 출력하세요.

total = 0
for num in range (1,11):
    if num%2 == 0:
        print(num, end=" ")
        total =+ 1
print()
print("짝수의 합:", total)

#문제 1-2. while문 카운트다운
#while문을 사용해 5부터 1까지 한 줄씩 출력하고, 끝나면 발사!를 출력하세요.

num = 5
while num>=1:
    print(num)
    num -= 1
print("발사!")


#문제 1-3. 문자열을 한 글자씩 순회하기
# 문자열 "python"을 한 글자씩 세로로 출력하고, 마지막에 글자 수를 출력하세요

word = "python"
count = 0
for w in word :
    print(w)
    count += 1
print("글자 수:", count)


#문제 2-1. 점수 집계
#아래 리스트에서 60점 미만인 사람이 몇 명인지, 
# 그리고 전체 평균(소수 첫째 자리까지)을 출력하세요.

scores = [88, 45, 72, 59, 93, 60, 38]

a = 0
for s in scores:
    if s < 60:
        a += 1

average = sum(scores)/len(scores)

print("불합격 인원 수:", a)
print("평균:", f"{average:.1f}")


#2-2. 입력값 검증 + 구구단 (continue / break)
#사용자가 입력한 값이 1~9가 아니면 안내 문구를 출력하고 다시 입력받고, 
#올바른 값이 들어오면 그 단의 구구단을 출력한 뒤 반복을 끝내세요.

inputs = [15, 0, 3]

num = 0

while True:
    n = inputs[num]
    num += 1
    print("입력값:", n)

    if n<1 or n>9 :
        print("1~9 사이 숫자를 입력하세요")
        continue

    for i in range(1,10):
        print(f"{num} x {i} = {num*i}")
    break


#2-3 서버 응답시간(ms) 리스트에서 max(), min()을 쓰지 말고 반복문으로 최댓값과 최솟값을 찾으세요.

times = [120, 87, 340, 95, 210]
max = times[0]
min = times[0]

for t in times:
    if t > max:
        t = max
    if t < min:
        t = min
print("최대 응답시간:", max)
print("최소 응답시간:", min)


#3-1 2단부터 9단까지, 한 줄에 한 단씩 가로로 출력하세요. 숫자는 자리를 맞춰 정렬합니다.

for dan in range(2,10):
    for num in range(1,10):
        print(f"{dan}x{num} = {dan*num:2d}",end =" ")
    print()

    