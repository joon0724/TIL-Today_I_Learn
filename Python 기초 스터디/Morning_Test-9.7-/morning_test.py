def get_input(prompt, value):
    try:
        return input(prompt)
    except EOFError:
        print(f"입력처리 불가 -> {value} 기본 값으로 진행합니다.")
        return value

# ============================================================================
# [응용 문제 1] 학생 성적 관리 시스템 
# 시나리오: 여러 학생의 정보를 리스트 안의 딕셔너리로 관리합니다.
##  students = [      {"이름": "김클라라", "점수": 90},      {"이름": "이개발", "점수": 75},  ]
# # **요구사항**:
#     1. 학생을 추가하는 함수 : add_student(name, score)
#     2. 전체 평균을 구하는 함수: get_average()
#     3. 평균 이상인 학생만 출력하는 함수:  get_top_students()
# ============================================================================
students = [      {"이름": "김클라라", "점수": 90},      {"이름": "이개발", "점수": 75},  ]

def add_student(name,score):
    students.append({"이름": name, "점수": score})

def get_average():
    if not students:
        return 0

    total = 0
    averageValue = 0.0
    for student in students:
        total += student["점수"]
        averageValue = total / len(students)
    return averageValue

def get_top_students():
    avg = get_average()
    return[s for s in students if s["점수"]>=avg]

add_student("준", 85)
print(f"평균점수 : {get_average():.1f}")
print(f"평균 이상 우수학생 : {get_top_students()}")


# ============================================================================
# [응용 문제 2]  온라인 쇼핑몰 장바구니 계산기
# 장바구니에 담긴 상품(이름, 가격, 수량)의 총 결제금액을 계산합니다
##  cart =[      {"상품명": "키보드", "가격": 50000, "수량": 1},   {"상품명": "마우스", "가격": 20000, "수량": 2},  ]
# # **요구사항**:
#     1. 1. 총 금액을 계산하는 함수 `calculate_total(cart)`
#     2. 총 금액이 **50,000원 이상이면 10% 할인**을 적용하는 조건문 추가
#     3. 최종 결제 금액 출력
# ============================================================================

print("=====응용문제 2번 장바구니 구현=====")

cart =[      {"상품명": "키보드", "가격": 50000, "수량": 1},   
       {"상품명": "마우스", "가격": 20000, "수량": 2},  ]

def calcuate_total(cart):
    total = 0
    for item in cart:
        total += item["가격"]*item["수량"]
    return total

def apply_discount(total):
    if total >= 50000:
        discount = total * 0.1
        return total - discount

print("cart 실행")    
subtotal = calcuate_total(cart)
final_price = apply_discount(subtotal)

print(f"할인 전 금액 : {subtotal: ,}원")
print(f"최종 결제 금액 : {final_price: ,}원")


# ============================================================================
# [응용 문제 3]  회원 등급 필터링 시스템 
# 긴 문장(예: 리뷰 텍스트)에서 각 단어가 몇 번 등장하는지 세는 프로그램을 만듭니다.
#
# # **요구사항**:
#     1. 구매금액이 100만원 이상이면 "VIP", 50만원 이상이면 "일반", 그 미만이면 "신규"로 등급을 매기는 함수 get_grade(amount)
#     2. 회원 리스트를 순회하며 각 회원의 등급을 딕셔너리에 추가
#     3. "VIP" 등급 회원만 따로 리스트로 출력
# ============================================================================

print("===회원 등급 VIP 필터링===")
members = [
     {"이름":"박영준","구매금액":1200000,"등급":"VIP"},
     {"이름":"정희석","구매금액":600000,"등급":"일반"},
     {"이름":"김성중","구매금액":20000,"등급":"신규"}
]

def get_grade(amount):
    if amount >= 1000000:
        return "VIP"
    elif amount >= 500000:
        return "일반"
    else:
        return "신규"

for member in members:
    member["등급"] = get_grade(member["구매금액"])

print(f"등급이 매겨진 회원 목록 : {members}")  #형식 그냥 외워(f"ddddddddd : {aaaaaa}")

vip_members = [m for m in members if m["등급"] == 'VIP'] #리스트 컴프리핸션
#풀어서 쓰면
vip_members = []
for m in members:
    if m["등급"] == 'VIP':
        vip_members.append(m) #members 안의 회원들을 하나씩 보면서
                              #등급이 'VIP'인 사람만 새 리스트에 담아라

print(f"VIP 회원 리스트 : {vip_members}")


# ============================================================================
# [응용 문제 4]  텍스트 단어 빈도수 분석기 [딕셔너리 + 반복문 + 함수]
# 긴 문장(예: 리뷰 텍스트)에서 각 단어가 몇 번 등장하는지 세는 프로그램을 만듭니다.
##  text = "이 제품 정말 좋아요 배송도 빠르고 품질도 좋아요"
# # **요구사항**:
#     1. 공백 기준으로 단어를 나누고(split()), 딕셔너리에 {단어: 등장횟수} 형태로 저장
#     2. 가장 많이 등장한 단어 TOP 3을 출력
# ============================================================================

text = "이 제품 정말 좋아요 배송도 빠르고 품질도 좋아요"

#1 문장을 쪼갠 후 , {단어:횟수} 구성하여 반환하는 함수 
def count_word(sentence):
    words = sentence.split()
    counts = {}              #빈 딕셔너리 준비 / {단어: 등장횟수} 형태로 채워나갈 예정
    for word in words:
        #dict.get(key,기본값) : key가 존재한다면 해당값 리턴, 없으면 기본값 0 리턴
        counts[word] = counts.get(word,0)+1 #이 단어가 counts에 이미 있으면 횟수 +1
    return counts                           # 없으면 1로 새로 등록 

word_count = count_word(text) #텍스트를 함수에 넣어 결과를 word_count에 저장

#2 내림차순 정렬 : 가장 많이 등장하는 단어 TOP3 
sorted_words = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
# word_count.items() --> 딕셔너리를 [("이",1), ("제품",1), ("좋아요",2), ...]처럼
                         #(단어, 횟수) 짝의 리스트로 바꿉니다.

# sorted(~~, key=~~~,reverse=True)-->리스트를 정렬하되 key로 지정한 기준값으로 비교
# lambda x: x[1]-->각 짝(예:("좋아요",2))에서 인덱스 1번, 횟수만 보고 정렬기준으로 삼아라
# reverse = True --> 횟수가 큰 것부터 내림차순으로 정렬

#3 Top3만 잘라서 출력
top3 = sorted_words[:3]
print("가장 많이 등장한 단어 Top 3:")


# ============================================================================
# [응용 문제 5]  To-Do 리스트 관리 프로그램 — [종합: 함수 + while + 데이터구조 + 제어문]
# 사용자가 메뉴를 선택해 할 일을 추가/삭제/조회하는 콘솔 프로그램입니다
# # **요구사항**:
#     1. while 반복문으로 프로그램이 계속 실행되도록 메뉴(추가/삭제/조회/종료)를 반복 출력
#     2. 각 기능을 함수로 분리: add_task(), delete_task(), show_tasks()
#     3. 할 일 목록은 리스트에 저장, 완료 여부는 딕셔너리({"할일": "장보기", "완료": False})로 관리
# ============================================================================

print("간단한 To-Do 리스트 관리 프로그램")

tasks = []   # {"할일":str,"완료":bool}

def add_task(task):
     tasks.append({"할일":task,"완료":False})

def delete_task(index):
     if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"'{removed['할일']}'삭제완료")
     else: 
          print("잘못된 번호입니다.")

def complete_task(index):
     if 0<= index <len(tasks):
          tasks[index]['완료'] = True

def show_tasks():
     if not tasks:
          print("할일 목록이 비어 있습니다.")
          return 
     for i,task in enumerate(tasks):
          status = "완료" if task["완료"] else "미완료"
          print(f"{i}.{task['할일']} [{status}]")