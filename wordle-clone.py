todays_word = 'queer'

todays_word = todays_word.upper()
checked_guess = [''] * 5
counter = 0

WHITE = '\033[97m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

while counter < 6 :
    player_guess = input('Enter a 5 letter word: ').upper()
    if player_guess == todays_word :
        print(WHITE + 'Correct!' + RESET)
        counter = 7
    else : 
        for i in range(5) :
            if player_guess[i] == todays_word[i] :
                checked_guess[i] = BLUE + player_guess[i] + RESET
            elif player_guess[i] in todays_word :
                checked_guess[i] = YELLOW + player_guess[i] + RESET
            else :
                checked_guess[i] = RED + player_guess[i] + RESET
        checked_guess_string = ''.join(checked_guess)
        print(checked_guess_string)
    counter += 1    
    if counter == 6 :
        print('Sorry. Try again tomorrow.')
    