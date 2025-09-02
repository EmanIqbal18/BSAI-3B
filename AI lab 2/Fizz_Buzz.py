print("Fizz Buzz ")
name = input("Enter your name:")
print("Welcome!",name)
import random
total = 0
last_num = 0
while True:

    number = random.randint(1, 20)
    total = last_num + number    
    last_num = number            
    if total % 3 == 0 and total % 5 == 0:
        correct = "fizzbuzz"
    elif total % 3 == 0:
        correct = "fizz"
    elif total % 5 == 0:
        correct = "buzz"
    else:
        correct = str(total)
    

    print(number)  
    guess = input("Your answer: ").lower()
        
    if guess != correct:
        print(f"The correct answer was {correct}.")
        print("Game Over!")
        break


