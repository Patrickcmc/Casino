import random
global bet
bet = 0
global balance
balance = 0
KARTE =["as",2,3,4,5,6,7,8,9,"jack","kraljica","kralj"]
VREDNOSTI = {
    "as": 1,
    "jack": 0,
    "kraljica": 0,
    "kralj": 0 
}


def accessBal() -> int:
    global balance
    return balance

def changeBal(val):
    global balance
    balance = val
    return balance


def Deposit() -> int:
    while True:
        deposit = input("Please enter the amount you'd like to deposit? $")
        if deposit.isdigit():
            if int(deposit) > 0:
                deposit = int(deposit)
                if accessBal() > 0:
                    changeBal(accessBal()+deposit)
                else:
                    changeBal(deposit)
                break
            else: print("Error: Please enter a valid number. ")
        else: print("Error: Please enter a number. ")
    print(f"You are depositing ${deposit} amount. Your current balance is ${accessBal()}")

def Bet():
    global bet
    while True:
        bet = input("Please enter the amount you'd like to bet? $")
        if bet.isdigit():
            if balance > int(bet) > 0:
                bet = int(bet)
                break
            else: print(f"Error: Please enter a number in range 1-{balance}")
        else: print("Error: Please enter a number. ")
    return bet

def TypeOfBet():
    while True:
        des = input("Would you like to bet on Player(1), Banker(2), or Tie(3): #")
        if des.isdigit():
            des = int(des)
            if des in range(1,3):
                print("Bet register successful!")
                break
            else:
                print("Error: Enter a valid number.")
        else:
            print("Error: Enter a number.")
    return des

def izberi_karti(karte):

    izbrane_karte = random.sample(karte, 2)
    vsota = sum(VREDNOSTI.get(karta, karta) for karta in izbrane_karte)

    return izbrane_karte, vsota

def Baccarat():
    igralec_karte, igralec_vsota = izberi_karti(KARTE)
    banker_karte, banker_vsota = izberi_karti(KARTE)

    if igralec_vsota > 9:
        igralec_vsota = igralec_vsota % 10
    if banker_vsota > 9:
        banker_vsota = banker_vsota % 10
    
    
    return igralec_karte,igralec_vsota,banker_karte,banker_vsota



def main():
    Deposit()
    print(TypeOfBet())
    Bet()
    Baccarat()
    
main()