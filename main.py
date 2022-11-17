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
    elif player_result < dealer_result:
        return 0
    elif player_result > dealer_result:
        return 1
    elif player_result == 21:
        return 3

def burst(player_result):  # 버스트인지 확인 (버스트 = 21이상)
    if (player_result > 21):
        print("버스트입니다 게임종료")

def get_fight_text(num):  #승패 판단
    if num == 0:
        return "Lose"
    elif num == 1:
        return "Win"
    elif num == 3:
        return "Black Jack!"
    elif num == 2:
        return "Draw"

cpu = []
you = []

for j in range(2): # 블랙잭 기본 시작
    cpu.append(get_card())
    you.append(get_card())

calc_card()

print("컴퓨터",cpu, cpu_s)
print("플레이어",you, you_s)

burst(cpu_s)

print(get_fight_text(fight(you_s, cpu_s)))












