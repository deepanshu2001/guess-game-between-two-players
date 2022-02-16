import random

a=int(input("Please enter a number:"))
b=int(input("Please enter b number:"))

number1=random.randint(a,b)
#we use random module to randomly generate numbers a and b
number2=random.randint(a,b)

trial1=0
trial2=0
while True:
    player1=int(input("Player 1,please guess a number:"))
    if player1>number1:
        print("Please guess a smaller number player 1!")
        
    elif player1<number1:
        print("Please guess a bigger number player 1!")
        

    elif player1==number1:
        print("Congratulations player1,you have guessed the number right!")
        break
    trial1+=1
print(f"It took player 1 ***** no of guesses")

while True:
    player2=int(input("Player 2,please guess a number:"))
    if player2>number2:
        print("Please guess a smaller number player 2!")
        
    elif player2<number2:
        print("Please guess a bigger number player 2!")
       

    elif player2==number2:
        print("Congratulations player2,you have guessed the number right!")
        break
    trial2+=1
print(f"It took player 2 ***** no of guesses")


if trial1>trial1:
    print("It took player 2 less guesses to guess the right number")
    print("Congratulations player 2,You Win")
elif trial1<trial2:
    print("It took player 1 less guesses to guess the right number")
    print("Congratulations player 1,You Win")
