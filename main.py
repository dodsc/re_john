import random as ran
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox

### GUI Initializing Section
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "images"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x500")
window.configure(bg = "#30485E")
window.title("BLACKJACK")

# 메인 canvas 구성
canvas = Canvas(
    window,
    bg = "#30485E",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

def getBetting():
    def betted():
        if (not entry_1.get().isdigit()):
            messagebox.showinfo("Error", "숫자만 입력해주세요.")
            return

        ## 배팅 코드
        canvas2.destroy()
        bet_button.place_forget()
        entry_1.place_forget()
        
    canvas2 = Canvas(
        window,
        bg = "#30485E",
        height = 500,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas2.place(x = 0, y = 0)

    canvas2.create_text(
        333.5,
        293.1425476074219,
        anchor="nw",
        text="얼마만큼 거시겠어요?",
        fill="#FFFFFF",
        font=("NanumSquare Neo ExtraBold", 14 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas2.create_image(
        400.0,
        337.2828369140625,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=289.0,
        y=319.2828369140625,
        width=222.0,
        height=34.0
    )

    bet_button = Button(
        borderwidth=0,
        highlightthickness=0,
        command=betted,
        text="배팅 걸기"
    )
    bet_button.place(
        x=281.0,
        y=361.2828369140625,
        width=238.0,
        height=37.0
    )


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
    elif num == 5:
        return "Dealer Bust! You Win!!"

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

# while True:
#     cpu = []
#     you = []
#     print("현재 가진 돈 :", coin)
#     if coin == 0:
#         print("더이상 가진 돈이 없습니다.")
#         break
#     bet = beting(coin) # 베팅액 확인

#     for j in range(2): # 블랙잭 기본 시작
#         cpu.append(get_card())
#         you.append(get_card())
        
#     calc_card()

#     while True:
#         print("컴퓨터",cpu[0])
#         print("플레이어",you, you_s)
        
#         if race() == 1: # 카드 더 받기
#             break
#         calc_card()
#         if burst(you_s) == 1: #버스트 판단
#             break
        
#     while cpu_s < 17: #딜러는 16이하면 무조건 카드를 받아야함
#         cpu.append(get_card())
#         calc_card()
    
        
#     print("컴퓨터",cpu, cpu_s)
#     print("플레이어",you, you_s)

#     print(get_fight_text(fight(you_s, cpu_s)))

#     if fight(you_s, cpu_s) == 0 or fight(you_s, cpu_s) == 4:
#         coin = coin - bet
#     elif fight(you_s, cpu_s) == 1 or fight(you_s, cpu_s) == 5:
#         coin = coin + bet
#     elif fight(you_s, cpu_s) == 2:
#         coin = coin
#     elif fight(you_s, cpu_s) == 3:
#         coin = coin + bet*2

# GUI Elements started
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    218.1849365234375,
    368.3338317871094,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    338.5343933105469,
    368.3338317871094,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    459.5613098144531,
    368.3338317871094,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    580.5882568359375,
    368.3338317871094,
    image=image_image_4
)

hit_image_raw = PhotoImage(
    file=relative_to_assets("button_1.png"))
hit_button = Button(
    image=hit_image_raw,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: getBetting(),
    relief="flat"
)
hit_button.place(
    x=667.1844482421875,
    y=365.25634765625,
    width=100.0,
    height=37.20671081542969
)

stay_image_raw = PhotoImage(
    file=relative_to_assets("button_2.png"))
stay_button = Button(
    image=stay_image_raw,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
stay_button.place(
    x=667.1844482421875,
    y=418.0,
    width=100.0,
    height=37.20672607421875
)

########## 잔액 처리 ###########
money_image_raw = PhotoImage(
    file=relative_to_assets("image_5.png"))
money_image = canvas.create_image(
    351.7325744628906,
    249.5,
    image=money_image_raw
)
canvas.create_text(
    372.2674255371094,
    242.5,
    anchor="nw",
    text="잔액: $1,000",
    fill="#E5DA49",
    font=("NanumSquare Neo Bold", 14 * -1)
)
##############################

card_total_computer = canvas.create_text(
    392.5,
    33.881317138671875,
    anchor="nw",
    text="21", # 컴퓨터 카드 합계
    fill="#FFFFFF",
    font=("NanumSquare Neo Bold", 12 * -1)
)

card_total_player = canvas.create_text(
    392.5,
    454.118896484375,
    anchor="nw",
    text="21", # 유저 카드 합계
    fill="#FFFFFF",
    font=("NanumSquare Neo Bold", 12 * -1)
)

count_win_computer = canvas.create_text(
    735.0516357421875,
    67.92990112304688,
    anchor="nw",
    text="승: 10",
    fill="#CCDDFF",
    font=("NanumSquare Neo Bold", 15 * -1)
)
count_lose_computer = canvas.create_text(
    734.0516357421875,
    88.92990112304688,
    anchor="nw",
    text="패: 20",
    fill="#EFACAC",
    font=("NanumSquare Neo Bold", 15 * -1)
)

canvas.create_text(
    596.0516357421875,
    26.881317138671875,
    anchor="nw",
    text="Computer",
    fill="#FFFFFF",
    font=("NanumSquare Neo Heavy", 32 * -1)
)

canvas.create_text(
    45.83544921875,
    428.0963439941406,
    anchor="nw",
    text="Player",
    fill="#FFFFFF",
    font=("NanumSquare Neo Heavy", 32 * -1)
)

count_lose_player = canvas.create_text(
    45.83544921875,
    404.2828369140625,
    anchor="nw",
    text="패: 2",
    fill="#EFACAC",
    font=("NanumSquare Neo Bold", 15 * -1)
)

count_win_player = canvas.create_text(
    45.83544921875,
    385.2828369140625,
    anchor="nw",
    text="승: 1",
    fill="#CCDDFF",
    font=("NanumSquare Neo Bold", 15 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    218.1849365234375,
    131.12710571289062,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    339.4656066894531,
    131.12710571289062,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    460.4656066894531,
    132.12710571289062,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    582.465576171875,
    132.12710571289062,
    image=image_image_9
)
# GUI elements ended

def clearGamingElement():
    # player 카드 리스트
    canvas.itemconfig(image_1, state="hidden")
    canvas.itemconfig(image_2, state="hidden")
    canvas.itemconfig(image_3, state="hidden")
    canvas.itemconfig(image_4, state="hidden")

    # computer 카드 리스트
    canvas.itemconfig(image_6, state="hidden")
    canvas.itemconfig(image_7, state="hidden")
    canvas.itemconfig(image_8, state="hidden")
    canvas.itemconfig(image_9, state="hidden")

    # 카드 토탈 카운팅 제거
    canvas.itemconfig(card_total_player, state="hidden")
    canvas.itemconfig(card_total_computer, state="hidden")

    # 힛, 스테이 버튼 제거
    # hit_button.place_forget()
    stay_button.place_forget()

window.resizable(False, False)
window.mainloop()

