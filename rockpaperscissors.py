from random import choice
global winsone
global winstwo
winsone = 0
winstwo = 0
def add():
    global winsone
    print("you win")
    winsone+=1
def minus():
    global winstwo
    print("you loose")
    winstwo+=1
def main():
    global winsone
    global winstwo
    inp = ""
    while inp != "rock" and inp != "paper" and inp != "scissors":
        inp = input("input your response")
        if inp != "rock" and inp != "paper" and inp != "scissors":
            print("bruh")
    botresp = choice(("scissors","rock","paper"))
    if inp == "rock" and botresp == "scissors":
        add()
    elif inp == "scissors" and botresp == "rock":
        minus()
    if inp == "paper" and botresp == "rock":
        add()
    elif inp == "rock" and botresp == "paper":
        minus()
    if inp == "scissors" and botresp == "paper":
        add()
    elif inp == "paper" and botresp == "scissors":
        minus()
    if inp == botresp:
        print("draw")
    print("player points =",winsone)
    print("AI wins =",winstwo)
    main()
main()
