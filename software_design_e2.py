# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 11:50:46 2022

@author: nicol

src = https://youtu.be/-njsRb8Tn70
"""

guess = 1


while True:
    num = input("please guess the number between{0-100}:")
    try:
        num = int(num)
        
    except:
        print("Invalide number,\nplease guess again")
        continue
    
    if num < 45:
        print("your guess was under")
        
    elif num>45:
        print("your guess was over")
        
    else:
        break
    guess += 1
print(f"your guessed it in {guess} guesses")

#%% improuvement

class GuessNumber:
    def __init__(self,number,mn = 0,mx = 100):
        self.guesses = 0
        self.number = number
        self.mn = mn
        self.mx = mx
        
    def get_guess(self):
        
        guess = input(f"please guess the number between  ({self.mn}-{self.mx}):")
        
        if self.valid_number(guess):
            return int(guess)
        else:
            print("Please enter a valid number.")
            
    def valid_number(self,str_number):
        #True condition
        try:
            number = int(str_number)
            
        except:
            return False
        return self.mn <= number <= self.mx
    
    def play(self):
        
        while True:
            self.guesses += 1
            
            guess = self.get_guess()
            
            if guess < self.number:
                print("You guess was under.")
                
            elif guess > self.number:
                print("You guess was over.")
                
            else: #They guessed it
                break
            
        print(f"You guessed it in {self.guesses} guesses.")

game = GuessNumber(56,0,100)
game.play()            
                