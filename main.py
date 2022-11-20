import random as ran

def get_card():
    s = ran.randint(1, 4) # 문양 선택
    n = ran.randint(1, 13) # 숫자 선택

    if(s == 1):
        shape = "스페이드"
    elif(s == 2):
        shape = "하트"
    elif(s == 3):
        shape = "클로버"
    else:
        shape = "다이아몬드"

    return shape, n

def calc_card():
    global cpu_s, you_s

    cpu_s = 0
    you_s = 0

    """
    while (cpu == you): # 서로 같은 카드가 나올 경우 다시 뽑기
        you.pop()
        you.append(choice_card())
    """

    for i in range(len(cpu)):
        if(cpu[i][1] >= 11): # K, Q, J는 10으로 계산
            cpu_s += 10
        elif(cpu[i][1] == 1 and cpu_s <= 10):
            cpu_s += 11
        else:
            cpu_s += cpu[i][1]

    for i in range(len(you)):
        if(you[i][1] >= 11): # K, Q, J는 10으로 계산
            you_s += 10
        elif(you[i][1] == 1 and you_s <= 10):
            you_s += 11
        else:
            you_s = you_s + you[i][1]

def fight(player_result, dealer_result):  #플레이어와 컴퓨터의 카드값 비교
    if player_result == dealer_result:
        return 2
    elif player_result > 21:
        return 4
    elif dealer_result > 21:
        return 5
    elif player_result == 21:
        return 3
    elif player_result < dealer_result:
        return 0
    elif player_result > dealer_result:
        return 1
    
    

def burst(player_result):  # 버스트인지 확인 (버스트 = 21이상)
    if (player_result > 21):
        return 1

def get_fight_text(num):  #승패 판단
    if num == 0:
        return "Lose"
    elif num == 1:
        return "Win"
    elif num == 3:
        return "Black Jack!"
    elif num == 2:
        return "Draw"
    elif num == 4:
        return "Bust!"

def race(): # 카드 더 받기 (hit일경우 더 받고 stay일 경우 멈춤)
    dobak = input("카드를 더 받으실거면 hit, 멈추실거면 stay를 입력해주세요 : ") # 도박
    if (dobak == 'hit'):
        you.append(get_card())
        return 0
    elif (dobak == 'stay'):
        return 1
    else:
        print("잘못입력하셨습니다.")
        return 2
        

def beting(coin): # 베팅
    bet = int(input("베팅할 금액을 입력하시오 : ")) # 베팅액 확인
    if (bet > coin):
        print("베팅한 금액이 가지고 있는 금액보다 큽니다.")
        return beting(coin)
    if bet <= 0:
        print("양수를 입력해주세요")
        return beting(coin)
    return bet
        

coin = 1000 # 초기 코인

while True:
    cpu = []
    you = []
    print("현재 가진 돈 :", coin)
    if coin == 0:
        print("더이상 가진 돈이 없습니다.")
        break
    bet = beting(coin) # 베팅액 확인

    for j in range(2): # 블랙잭 기본 시작
        cpu.append(get_card())
        you.append(get_card())
        
    calc_card()

    while True:
        print("컴퓨터",cpu[0])
        print("플레이어",you, you_s)
        
        if race() == 1: # 카드 더 받기
            break
        calc_card()
        if burst(you_s) == 1: #버스트 판단
            break
        
    print("컴퓨터",cpu, cpu_s)
    print("플레이어",you, you_s)

    print(get_fight_text(fight(you_s, cpu_s)))

    if fight(you_s, cpu_s) == 0 or fight(you_s, cpu_s) == 4:
        coin = coin - bet
    elif fight(you_s, cpu_s) == 1:
        coin = coin + bet
    elif fight(you_s, cpu_s) == 2:
        coin = coin
    elif fight(you_s, cpu_s) == 3:
        coin = coin + bet*2

    
    



