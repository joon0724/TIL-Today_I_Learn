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

#20 왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
주민번호를 입력받아 형태를 바꿔 출력해보자.
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
