def rps():
    import random
    l1=["rock", "paper", "scissors"]
    c=input("Do you want to play?y/n: ")
    if c=='y':
        c1=input("Enter your choice type rock, paper or scissors: ")
        c2=random.choice(l1)
        if c1!=c2:
            if c1=="paper" and c2=="rock":
                print("Computer is decideing...")
                print("Computer has decided!")
                print("You played", c1)
                print("Computer played", c2)
                print ("You are the winner")
            elif c1=="scissor" and c2=="paper":
                print("Computer is decideing...")
                print("Computer has decided!")
                print("You played", c1)
                print("Computer played", c2)
                print ("You are the winner")
            elif c1=="rock" and c2=="sscissor":
                print("Computer is decideing...")
                print("Computer has decided!")
                print("You played", c1)
                print("Computer played", c2)
                print ("You are the winner")
            elif c1=="rock" and c2=="paper":
                print("Computer is decideing...")
                print("Computer has decided!")
                print("You played", c1)
                print("Computer played", c2)
                print ("Computer is the winner")
            elif c1=="paper" and c2=="scissor":
                print("Computer is decideing...")
                print("Computer has decided!")
                print("You played", c1)
                print("Computer played", c2)
                print ("Computer is the winner")
            elif c1=="paper" and c2=="scissor":
                print("Computer is decideing...")
                print("Computer has decided!")
                print("You played", c1)
                print("Computer played", c2)
                print ("Computer is the winner")
        else:
            print("Its a tie!")
    elif c=="n":
        print("That's alright see you next time!")
    else:
        print("Invalid Input")

def number_guess():
    import random
    print("Welcome To number Guessing game!!!!")
    print("Computer is picking a number between 1 and 100")
    n=random.randint(1, 10)
    print("Computer has selected a number")
    a=0
    while a!=3:
        m=int(input("Place Your Guess, You have 3 Guesses"))
        if abs(m-n)>5:
            print("You are not even close lol")
            a+=1
        elif abs(m-n)in range (3,6):
            print("Get a little closer")
            a+=1
        elif abs(m-n)<3:
            print("You are very close")
            a+=1
        elif abs(m-n)==1:
            print("You are just one awayy")
            a+=1
        elif m==n:
            print ("You got it!!!! Good job")
            break
        elif abs(m-n)>=10:
            print("Invalid Input")
            a+=1
    if a==3:
        print("Better Luck Next Time")
        print("The number computerji had selected was ",n)
rps()