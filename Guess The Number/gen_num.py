import random

class Number:

    def __init__(self, player):
        self.player = player
        self.chances = 6

    def gen_num(self):
       
        num = random.randint(0, 100)

        
        # print(num)
        print(f"Hello! {self.player} Game Starts... I've selected a number between 0-100. You have total 6 chances! Guess it!")
        current_guess = int(input('\n Enter the number: '))
    
        while True:
            if (num == current_guess):
                print(f'You won the game! Congratulations {self.player}. You guessed the correct number.')
                break

            else:
                self.chances -= 1
                if (self.chances == 0):
                    print(f'You lost {self.player}! Game Over. The number was {num}')
                    break

                if (num < current_guess):
                    current_guess = int(input(f'Your guess is too high. You have {self.chances} chances remaining.\n Guess Again? '))

                elif (num > current_guess):
                    current_guess = int(input(f'Your guess is too low. You have {self.chances} chances remaining.\n Guess Again? '))
                print('\n')
            

            def hints():
                # Hint 1: Sum of the digits
                ones_digit=num%10
                tens_digit=int(num/10)
                num_sum=ones_digit+tens_digit

                while self.chances==5:
                    print(f'Hint: The sum of the digits of the number is {num_sum}')
                    break
                
                # Hint 2: Number is odd or even?
                while self.chances==2:
                    if num%2==0:
                        print('Hint: The given number is even.')
                    else:
                        print('Hint: The given number is odd.')
                    break
                    
            hints()
        

    
