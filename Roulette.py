import random
import time
import os
SIZE_OF_TABLE = 36
global balance
balance = 0

RED = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
CLRS = ["Red", "Black"]
global bet
bet = 0

def firstChar(c):
    l = []
    for i in c:
        l.append(i)
    if not l[0].isupper():
        l[0] = l[0].upper()
    return "".join(l)

def accessBal() -> int:
    global balance
    return balance

def changeBal(val):
    global balance
    balance = val
    return balance

def winBet(typeOfWin) -> int:
    global bet
    global balance
    if typeOfWin == "OnNumber":
        balance += (bet * SIZE_OF_TABLE)
    elif typeOfWin == "OnColor" or typeOfWin == "OnEorO":
        balance += (2*bet)
    else:
        print("Error: Unknown err")

def Deposit() -> int:
    while True:
        deposit = input("Please enter the amount you'd like to deposit? (min: $10) $")
        time.sleep(0.5)
        if deposit.isdigit():
            if 10000 >= int(deposit) >= 10:
                deposit = int(deposit)
                if accessBal() > 0:
                    changeBal(accessBal()+deposit)
                else:
                    changeBal(deposit)
                break
            else: print("Error: Please enter a valid number. ")
        else: print("Error: Please enter a number. ")
    print(f"You are depositing ${deposit} amount. Balance = ${accessBal()}")

def NumberToBetOn():
    while True:
        numb = input(f"Please enter the number you'd like to bet on (0-{SIZE_OF_TABLE}): ")
        if numb.isdigit() or numb == "0":
            if int(numb) in range(SIZE_OF_TABLE + 1):
                numb = int(numb)
                break

            else: print("Error: Please enter a valid number. ")
        else: print("Error: Please enter a number. ")

    print(f"Bet on Number successful!")
    Bet()
    return numb

def ColorToBetOn():
    while True:
        des = input("What color would you like to bet on? (Red, Black) -")
        if not des.isdigit():
            des = firstChar(des)
            if  des == "Red" or des == "Black":
                break
            else:
                print("Enter either Red/Black")
        else:
            print("Error: invalid input.")
    print(f"Bet on {des} successful")
    Bet()
    return des

def OoEToBetOn():
    while True:
        des = input("What type would you like to bet on? (Odd, Even) -")
        if not des.isdigit():
            des = firstChar(des)
            if des == "Odd" or des == "Even":
                break
            else:
                print("Enter a valid input - (Odd/Even). ")
        else:
            print("Enter a valid input - (Odd/Even). ")
    print(f"You bet on {des} successfully")
    Bet()
    return des

def typeOfRoll():
    while True:
        des = input("What would you like to bet on? (A number(1), A color (2), Odd or Even(3)) -")
        if des.isdigit():
            if int(des) in range(1, 4):
                des = int(des)
                break
            
            print("Error: Input not in range 1-3. ")
        print("Error: Input not valid. Enter a number in range 1-3. ")
    
    if des == 1:return NumberToBetOn()
    
    if des == 2:return ColorToBetOn()
    
    if des == 3:return OoEToBetOn()


def Bet():
    global balance
    time.sleep(0.8)
    print(f"Note: Your current balance is ${balance}")
    global bet
    while True:
        bet = input("Please enter the amount you'd like to bet? $")
        if bet.isdigit():
            if balance >= int(bet) > 0:
                bet = int(bet)
                balance = balance - bet
                break
            else: print(f"Error: Please enter a number in range 1-{balance}")
        else: print("Error: Please enter a number. ")
    time.sleep(0.3)
    print(f"Bet registered at: ${bet}")
    time.sleep(0.2)
    print(f"Good luck!")
    return bet

def GetRoll():
    time.sleep(0.5)
    for i in range(3):
        print("Rolling...")
        time.sleep(1)
        i += 1
    roll = random.randint(0,SIZE_OF_TABLE)
    return roll

def WoL(numb,roll):
    time.sleep(1)
    copy = roll
    if numb in CLRS:
        if roll in RED: roll = "Red"
        else: roll = "Black"
        
        if roll == numb:
            winBet("OnColor")
            print(f"Congrats!! You bet on {roll} and it's the winning color! :D")
        else:
            
            print(f"You picked {numb}. It was not a winning color. :(, it was {roll}")

    elif type(numb) == int:
        if numb == roll:
            winBet("OnNumber")
            print(f"Congrats!! You bet on {roll} and it's the winning number! :D")
            
        else: print(f"You picked {numb}. It was not a winning number. :(.")
    
    else:
        if roll % 2 == 0: roll = "Even"
        else: roll = "Odd"

        if roll == numb:
            winBet("OnEorO")
            print(f"Congrats!! You bet on {roll} and it's the winning in Odd or Even! :D")

        else: print(f"You picked {numb}. It was not the winning type. :(, it was {roll}")
    
    print(f"The roll was {copy}.")
    time.sleep(0.5)
    print(f"New Balance: ${balance}")
    time.sleep(0.5)
    if balance == 0:
        des = input("You went bankrupt. Would you like to deposit more? (Yes/No)- ")
        if not des.isdigit():
            des = firstChar(des)
            if des == "Yes":
                Deposit()
            else:
                print("You've been thrown out the casino, Thanks for playing.")
                time.sleep(0.3)
                return 0
    PlayAgain()

def PlayAgain():    
    time.sleep(0.8)
    while True:
        des = input("Would you like to play again? (Yes/No) -")
        if not des.isdigit():
            des = firstChar(des)
            time.sleep(0.8)
            if des == "Yes":
                print("Good Luck!")
                time.sleep(0.8)
                main()
                break
            elif des == "No":
                print(f"You've cashed out ${balance} Congrats {name}! ")
                print("Thank you for playing! Exiting...")
                break
        else:
            print("Error: Enter Yes or No. ")

while True:
    name, age = input("Enter your name: "), input("Enter your age: ")
    if not name.isdigit() and age.isdigit():
        if int(age) in range(18, 117):
            print(f"Welcome to the casino {name}.")
            time.sleep(0.5)
            break
        else:
            print("You're not allowed to play.")
            exit()
    else: print("Enter a valid name and age.")


Deposit()
def main():
    WoL(typeOfRoll(),GetRoll())
    
main()