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

cpu = []
you = []

for j in range(2): # 블랙잭 기본 시작
    cpu.append(get_card())
    you.append(get_card())

calc_card()

print(cpu, cpu_s)
print(you, you_s)