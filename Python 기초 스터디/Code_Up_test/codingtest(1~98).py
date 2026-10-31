#1. print( )를 이용해 다음 단어를 출력하시오. => Hello
print("Hello")

#2. 다음 문장을 출력해보자
Hello World
print("Hello", "World")

#3. 이번에는 줄을 바꿔 출력하는 출력문을 연습해보자.
Hello
World
print("Hello", "\nWorld")

#4. 이번에는 작은 따옴표(')(single quotation mark)가 들어있는 출력물 연습을 해보자
#'Hello'
print("'Hello'")

#5 이번에는 큰따옴표(")(double quotation mark)가 포함된 출력문을 연습해보자.
#"Hello World"
print('"Hello World"')

#6. 다음 문장을 출력하시오.
#"!@#$%^&*()'
(단, 큰따옴표와 작은따옴표도 함께 출력한다.)
print("\"!@#$%^&*()\'")

#7. 윈도우 운영체제의 파일 경로를 출력하는 연습을 해보자.다음 경로를 출력하시오.
#"C:\Download\'hello'.py"
print("C:\\Download\\'hello'.py\"")

#8. 이번에는 다음과 같은 python프로그램의 소스코드를 출력해보자.
#print("Hello\nWorld") 코드를 정확히 그대로 출력하여라
print('print("Hello\\nWorld")')

#9 변수에 문자 1개를 저장한 후 변수에 저장되어 있는 문자를 그대로 출력해보자.
#예시 c= input() print(c)
a = input()
print(a)

#10 변수에 정수값을 저장한 후 정수로 변환하여 출력해보자.
n = input()
n = int(n)
print(n)

#11 변수에 실수값을 저장한 후 변수에 저장되어 있는 값을 그대로 출력해보자.
f = input()
f = float(f)
print(f)

#12 줄을 바꿔 정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자 
a = input()
b = input()
a = int(a)
b = int(b)
print(a)
print(b)

#13 줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.
a = input()
b = input()
print(b)
print(a)

#14 실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.
f = input()
f = float(f)
print(f) #f에 저장되어있는 값을 출력하고 바꾼다
print(f)
print(f)

#15 공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.
a,b = input().split()
a=int(a)
b=int(b)
print(a)
print(b)

#16 공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자
a,b = input().split()
print(b,a)

#17 정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자
s = input()
print(s,s,s)

#18 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
a,b = input().split(':')
print(a,b,sep=':')

#19 "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
y,m,d = input().split('.')
print(d,m,y, sep='-')

#20 왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.주민번호를 입력받아 형태를 바꿔 출력해보자.
a,b = input().split('-')
print(a,b, sep='')

#21 입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

#22 6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.
a = input()
print(a[0:2], a[2:4], a[4:6])

#23 시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.
h, m, s = input().split(':')
print(m)

a = input()
a = chr(ord(a)+1)

#24 알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아 순서대로 붙여 출력하는 프로그램을 작성해보자.
w1, w2 = input().split()
s = w1 + w2
print(s)

#25 정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
a,b = input().split()
c = int(a) + int(b)
print(c)

#26 실수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
a = input()
b = input()
print(float(a) + float(b))

#27 10진수를 입력받아 16진수(hexadecimal)로 출력해보자
a = input()
n = int(a)
print('%x'%n)

#28 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
a = input()
n = int(a)
print('%X'%n)

#29 16진수를 입력받아 8진수(octal)로 출력해보자.
a = input()
a = int(a,16)
print('%o'%a)

#30 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.
a = ord(input())
print(a)

#31 10진 정수 1개를 입력받아 유니코드 문자로 출력해보자.
a = int(input())
a = chr(a)
print(a)

#32 입력된 정수의 부호를 바꿔 출력해보자.
a = input()
a = int(a)
print(-a)

#33 문자 1개를 입력받아 그 다음 문자를 출력해보자.
a = input()
a = chr(ord(a)+1)
print(a)

#34 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.
a,b = input().split()
a = int(a)
b = int(b)
c = a - b
print(c)

#35 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.
f1,f2 = input().split()
m = float(f1)*float(f2)
print(m)

#36 단어와 반복 횟수를 입력받아 여러 번 출력해보자.
w,n = input().split()
n = int(n)
print(w*n)

#37 반복 횟수와 문장을 입력받아 여러 번 출력해보자.
n = input()
s = input()
print(int(n)*s)

#38 정수 2개(a, b)를 입력받아 a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.
a,b = input().split()
c = int(a)**int(b)
print(c)

#39 실수 2개(f1, f2)를 입력받아 f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.
f1,f2 = input().split()
f = float(f1)**float(f2)
print(f)

#40 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.
a,b = input().split()
c = int(a)//int(b)
print(c)

#41 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.
a,b = input().split()
print(int(a)%int(b))

#42 실수 1개를 입력받아 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.
a = input()
a = float(a)
print(format(a,".2f"))

#43 실수 2개(f1, f2)를 입력받아 f1 을 f2 로 나눈 값을 출력해보자. 
#이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.
f1,f2 = input().split()
f3 = float(f1)/float(f2)
print(format(f3,".3f"))

#44 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
a,b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b,".2f"))

#45 정수 3개를 입력받아 합과 평균을 출력해보자.
a,b,c = input().split()
d = int(a)+int(b)+int(c)
e = d/3
print(d,format(e,".2f"))

#46 정수 1개를 입력받아 2배 곱해 출력해보자.(비트시프트 연산자)
a = input()
print(int(a)<<1)

#47 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.(비트시프트 연산자)
#0 <= a <= 10, 0 <= b <= 10
a,b = input().split()
print(int(a)<<int(b))

#48 두 정수(a, b)를 입력받아 a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
print(int(b)>int(a))

#49 두 정수(a, b)를 입력받아 a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
print(int(a)==int(b))

#50 두 정수(a, b)를 입력받아 b의 값이 a의 값 보다 크거나 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
print(int(b)>=int(a))

#51 두 정수(a, b)를 입력받아 a의 값이 b의 값과 서로 다르면 True 를, 같으면 False 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
print(int(a)!=int(b))

#52 정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.
a = input()
a = int(a)
print(bool(a))

#53 정수값이 입력될 때,그 불 값을 반대로 출력하는 프로그램을 작성해보자.
a = bool(int(input()))
print(not a)

#54 2개의 정수값이 입력될 때, 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
print(bool(int(a)) and bool(int(b)))

#55 2개의 정수값이 입력될 때,그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
print(bool(int(a)) or bool(int(b)))

#56 2개의 정수값이 입력될 때,그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

#57 2개의 정수값이 입력될 때,그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
a = bool(int(a))
b = bool(int(b))
print((not a and not b) or (a and b))

#58 2개의 정수값이 입력될 때,그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
c = bool(int(a))
d = bool(int(b))
print((not c) and (not d))

#59 ~ 62 : 비트단위논리연산문제


#63입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.단, 3항 연산을 사용한다.
a,b = input().split()
a = int(a)
b = int(b)
c = (a if(a>=b) else b)
print(c)

#64 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.단, 3항 연산을 사용한다.
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = (a if(b>a) else b)
e = (d if(c>d) else c)
print(e)

#65 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)

#66 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a%2 == 0:
	print("even")
else:
	print("odd")

if b%2 == 0:
	print("even")
else :
	print("odd")
	
if c%2 == 0:
	print("even")
else :
	print("odd")

#67 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
a = input()
a = int(a)

if 0>a and a%2 == 0 :
    print("A")

if 0>a and a%2 == 1 :
    print("B")

if a>0 and a%2 == 0:
    print("C")

if a>0 and a%2 == 1:
    print("D")

#68 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
a = int(input())

if a >= 90 :
    print("A")

elif a >= 70 :
    print("B")

elif a>= 40 :
    print("C")

else :
    print("D")

#69 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
grade = input()

if grade == "A" :
    print("best!!!")
elif grade == "B" :
    print("good!!")
elif grade == "C" :
    print("run!")
elif grade == "D" :
    print("slowly~")
else :
    print("what?")

#70 월이 입력될 때 계절 이름이 출력되도록 해보자.
a = int(input())

if a//3==1 :
    print("spring")

elif a//3==2 :
    print("summer")

elif a//3 ==3 :
    print("fall")

elif a//3 == 4 or a<=2 :
    print("winter")

#71 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
n = 1
while n!=0:
    n = int(input())
    if n!=0:
        print(n)

#72 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
n = int(input())
while n != 0:
    print(n)
    n = n-1

#73 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
n = int(input())
while n != 0:
    n = n-1
    print(n)

#74 영문 소문자(a ~ z) 1개가 입력되었을 때, a부터 그 문자까지의 알파벳을 순서대로 출력해보자.
w1 = ord(input())
w2 = ord('a')
while w2 <= w1 :
	print(chr(w2), end = ' ')
	w2 += 1

#75 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
i = int(input())
for i in range(0,i+1):
    print(i)

#76 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
i = int(input())
for i in range(0,i+1):
    print(i)

#77 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
n = int(input())
n1 = 0
for n in range(1,n+1):
    if n%2==0:
        n1 += n
print(n1)

#78 영문 소문자 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.
while True:
    w1 = input()
    print(w1)
    if w1 == 'q':
        break

#79 1, 2, 3 ... 을 계속 더해 나갈 때,그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만 계속 더하는 프로그램을 작성해보자.
a = int(input())
total = 0
b = 0
while True:
    if a <= total:
        break
    total += b
    b += 1
print(b-1)

#80 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,나올 수 있는 모든 경우를 출력해보자.
n,m=input().split()

n=int(n)
m=int(m)

for i in range(1, n+1) :
  for j in range(1, m+1) :
    print(i, j)

#81 A, B, C, D, E, F 중 하나가 입력될 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
n = int(input(), 16)

for i in range(1, 16):
    print('%X' % n, '*%X' % i, '=%X' % (n * i), sep='')

#82 3 6 9 게임의 왕이 되기 위한 369 마스터 프로그램을 작성해 보자.
n = int(input())

for i in range(1, n+1) :
  if i%10==3 or i%10==6 or i%10==9 :
    print("X", end=' ')
  else :
    print(i, end=' ')


#83 빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때, 주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산해보자.
r, g, b = input().split()

r = int(r)
g = int(g)
b = int(b)

for i in range(0, r) :
  for j in range(0, g) :
    for k in range(0, b) :
      print(i, j, k)

print(r*g*b)

#84 소리 파일 저장용량 계산하기
h, b, c, s = map(int, input().split())

size_mb = h * b * c * s / 8 / 1024 / 1024
print('%.1f MB' % size_mb)

#85 그림 파일 저장용량 계산하기
w, h, b = map(int, input().split())

size_mb = w * h * b / 8 / 1024 / 1024
print('%.2f MB' % size_mb)

#86 1, 2, 3 ... 을 순서대로 계속 더해 합을 만드는데,그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.
n = int(input())
s = 0
c = 1

while True:
    s += c
    c += 1
    if s >= n:
        break

print(s)

#87 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,3의 배수인 경우는 출력하지 않도록 만들어보자.
n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i, end=' ')

#88 수 나열하기1
a,d,n=input().split()

a=int(a)
d=int(d)
n=int(n)

s=a
for i in range(2, n+1):
   s+=d

print(s)

#89 수 나열하기2
a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

for i in range(1, n) :
  a = a*r

print(a)

#90 수 나열하기3
a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)

for i in range(1, n) :
  a = a*m+d

print(a)

#91 함께 문제 푸는 날(설명)
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1

print(d)

#92 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end=' ')

#93 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

for i in range(n-1, -1, -1):
  print(a[i], end=' ')

#94 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

min = a[0]
for i in range(0, n) :
  if a[i] < min :
    min = a[i]

print(min)

#95 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때, n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

n = int(input())
for i in range(n):
    x, y = input().split()
    d[int(x)][int(y)] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()

#96 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.
d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(1, 20):
    row = input().split()
    for j in range(1, 20):
        d[i][j] = int(row[j - 1])

n = int(input())
for i in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    for j in range(1, 20):
        if d[j][y] == 0:
            d[j][y] = 1
        else:
            d[j][y] = 0

        if d[x][j] == 0:
            d[x][j] = 1
        else:
            d[x][j] = 0

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()

#97 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),막대를 놓는 방향(d:가로는 0, 세로는 1)과막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,
#격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
h,w = input().split()
h = int(h)
w = int(w)

m = []
for i in range(h+1) :
  m.append([])
  for j in range(w+1) :
    m[i].append(0)

n = int(input())
for i in range(n) :
  l,d,x,y = input().split()
  if int(d)==0 :
    for j in range(int(l)) :
      m[int(x)][int(y)+j] = 1
  else :
    for j in range(int(l)) :
      m[int(x)+j][int(y)] = 1

for i in range(1, h+1) :
  for j in range(1, w+1) :
    print(m[i][j], end=' ')
  print()

#98 성실한 개미
