#Better Way 10 대입식 반복을 피하라

# 왈러스 연산자
# := 는 if나 while문등 조건식에 대입후 실제 평가가 이루어짐. (왈러스는 바다코끼리 눈과 어금니 처럼 생겨서 붙여진 이름)

# 예시 코딩을 위한 코드들 pass 해도 무관
fresh_fruit = {
    '사과': 10,
    '바나나': 8,
    '레몬': 5,
}

def make_lemonade(count):
    n = 1
    print(f'레몬 {count*n} 개로 레모네이드 {count//n} 개를 만듭니다.')
    fresh_fruit['레몬'] -= (count * n)
    print(f'레몬이 {fresh_fruit["레몬"]} 개 남았습니다.')

def out_of_stock():
    print(f'제료가 부족합니다. 재료를 보충해 주세요.')
    
    
# 기존에는 레몬의 개수를 읽은 후 if문을 통해 그 값이 0인지 아닌지 확인이 가능하다.
count = fresh_fruit.get('레몬', 0) #따로 count는 무엇이다 설정이 불편하다라고 생각할 수 있음.
if count:
    make_lemonade(count)
else:
    out_of_stock()
    
    
#왈러스를 사용한 코딩은 if문 식에 직접 왈러스를 이용하여 대입

fresh_fruit['레몬'] = 5  # 테스트를 위해 갯수 리셋
if count := fresh_fruit.get('레몬', 0):   #길벗 코드에 lemon이라고 잘못 입력 되어있음.
                                           # 값이 0이면 flase로 else가 실행
    make_lemonade(count)
else:
    out_of_stock()
    
    
# 또 하나의 예제

# 사과 4개가 1개의 주스를 만들 수 있게 설정
def make_cider(count):
    n = 4

    print(f'사과 {count} 개로 사과주스 {count//n} 개를 만듭니다.')
    fresh_fruit['사과'] -= (n *(count//n))
    print(f'사과가 {fresh_fruit["사과"]} 개 남았습니다.')

fresh_fruit['사과'] = 10  # 테스트를 위해 갯수 리셋


#기존 사과 4개로 몇개의 주스를 만들 수 있는지 코드
count = fresh_fruit.get('사과', 0)  #따로 count는 무엇이다 설정이 불편하다라고 생각할 수 있음.
if count >= 4:                # 개수가 4보다 작을 경우 flase로 else 실행
    make_cider(count)
else:
    out_of_stock()

    
#왈러스를 이용한 코드
fresh_fruit['사과'] = 10  # 테스트를 위해 갯수 리셋

if (count := fresh_fruit.get('사과', 0)) >= 4: # 왈러스를 이용하여 대입한 값이 4보다 크면 True로 실행하기 위해 괄호 사용.
    make_cider(count)
else:
    out_of_stock()
    

# 또 또 하나의 예제

# 고객이 바나나 스무디를 주문했을 때 
#스무디를 만들려면 바나나 슬라이스가 최소 두 개는 필요하고 
#슬라이스가 부족하면 OutOfBananas 예외 발생시킴


def slice_bananas(count):
    print(f'바나나 {count} 개를 슬라이스합니다.')
    fresh_fruit['바나나'] -=  count
    return count

class OutOfBananas(Exception):
    pass

def make_smoothies(count):
    n=2
    if count > n:
        print(f'바나나 슬라이스 {count} 개로 스무디 {count//n} 개를 만듭니다.')
        print(f'바나나가 {fresh_fruit["바나나"]} 개 남았습니다.')
    else:
        raise OutOfBananas



#기존 방식인 두가지 예시
#첫번째 pieces를 조건문 밖에 둔 경우

pieces = 0
count = fresh_fruit.get('바나나', 0)
if count >= 2:
    pieces = slice_bananas(count)

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()
    
    
    
#두번째 pieces를 조건문 안에 둔 경우


fresh_fruit['바나나'] = 8  # 테스트를 위해 갯수 리셋

count = fresh_fruit.get('바나나', 0)
if count >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()
    
    
#왈러스를 이용한 개선된 방식
#첫번째 개선 pieces가 외부

fresh_fruit['바나나'] = 8  # 테스트를 위해 갯수 리셋

pieces = 0
if (count := fresh_fruit.get('바나나', 0)) >= 2: #괄호의 이유는 위에 확인
    pieces = slice_bananas(count)

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()


# 두번째 개선 pieces가 내부

fresh_fruit['바나나'] = 8  # 테스트를 위해 갯수 리셋

if (count := fresh_fruit.get('바나나', 0)) >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

#파이썬에는  switch/ case 문이 따로 없음
#if, elif, else 문 사용
# 가장 좋은 주스 바나나 스무디 --> 애플 주스 --> 레모네이드 순으로 제공
# 기존 방식을 이용한 첫번째 예시

fresh_fruit = {
    '사과': 10,
    '바나나': 8,
    '레몬': 5,
}
count = fresh_fruit.get('바나나', 0)

if count >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit.get('사과', 0)
    if count >= 4:
        to_enjoy = make_cider(count)
    else:
        count = fresh_fruit.get('레몬', 0)
        if count:
            to_enjoy = make_lemonade(count)
        else:
            to_enjoy = '아무것도 없음'
            
#왈러스를 이용한 방식
fresh_fruit = {
    '사과': 10,
    '바나나': 8,
    '레몬': 5,
}

if (count := fresh_fruit.get('바나나', 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get('사과', 0)) >= 4:
    to_enjoy = make_cider(count)
elif count := fresh_fruit.get('레몬', 0):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = '아무것도 없음'
    
# do / while루프가 없음.
# while 루프의 예시
#신선한 과일이 배달돼서 이 과일을 모두 주스로 마든 후 병에 담기로 하는 코드
import random

def pick_fruit():
    if random.randint(1,10) > 2:   # 80% 확률로 새 과일 보충
                                # random.randint를 이용하여 랜덤으로 int값을 불러옴.
        return {
            '사과': random.randint(0,10), 
            '바나나': random.randint(0,10),
            '레몬': random.randint(0,10),
        }
    else:
        return None

def make_juice(fruit, count):
    if fruit == '사과':
        return [('사과주스', count/4)]
    elif fruit == '바나나':
        return [('바나나스무디',count/2)]
    elif fruit == '레몬':
        return [('레모네이드',count/1)]
    else:
        return []
    
#기존의 첫번째 예시
# while에서 fresh_fruit = pick_fruit() 를 반복사용

bottles = []
fresh_fruit = pick_fruit()
while fresh_fruit: # pick_fruit안의 random.randint 값이 0이 아닌 이상 True로 무한 루프 실행
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
    fresh_fruit = pick_fruit() # pick_fruit안의 random.randint 값이 0이 나온다면 바로 멈춤

print(bottles)


# 두번째 예시
#while의 무한 루프와 break을 이용하여 단순화

bottles = []
while True: # 무한루프
    fresh_fruit = pick_fruit()
    if not fresh_fruit: # 중간에서 끝내기
        break

    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

print(bottles)


#왈러스를 이용한 단순화

bottles = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

print(bottles)


# 총 몇 병이 담겨있는지 확인 인터폴레이션 활용해보고 싶어서 사용.
apple_count=0
banana_count=0
lemon_count=0

for fruit, count in bottles:
    if fruit == "사과주스":
        apple_count=apple_count+count
    if fruit == "바나나스무디":
        banana_count=banana_count+count
    if fruit == "레모네이드":
        lemon_count=lemon_count+count
        
a=f"""
사과 주스 병은 총 {apple_count}개 입니다.
바나나스무디 병은 총 {banana_count}개 입니다.
레모네이드 병은 총 {lemon_count} 개 입니다.
"""
print(a)

# 왈러스(:=)를 이용하여 반복식를 단순화 한다.
#swich / case, do / while 루프를 쓸 수 없지만, 대입식으로 깔끔하게 표현이 가능하다.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    