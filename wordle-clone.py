todays_word = 'media'

todays_word = todays_word.upper()
#player_guess = player_guess.upper()
checked_guess = [''] * 5
counter = 0

GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

while counter < 6 :
    player_guess = input('Enter a 5 letter word: ').upper()
    if player_guess == todays_word :
        print('Correct!')
        counter = 7
    else : 
        for i in range(5) :
            if player_guess[i] == todays_word[i] :
                checked_guess[i] = GREEN + player_guess[i] + RESET
            elif player_guess[i] in todays_word :
                checked_guess[i] = YELLOW + player_guess[i] + RESET
            else :
                checked_guess[i] = RED + player_guess[i] + RESET
        checked_guess_string = ''.join(checked_guess)
        print(checked_guess_string)
    counter += 1    
    if counter == 6 :
        print('Sorry. Try again tomorrow.')
    

#if 
#   print('Your first letter is correct!')
#elif player_guess[0] in todays_word :
#    print('Your first letter is in today\'s word.')

#if player_guess[1] == todays_word[1] :
#    print('Your second letter is correct!')
#elif player_guess[1] in todays_word[1] :
#   print('Your second letter is in today\'s word.')

#if player_guess[2] in todays_word :
#    print('Your third letter is in today\'s word.')

#if player_guess[3] in todays_word :
#    print('Your fourth letter is in today\'s word.')

#if player_guess[4] in todays_word :
#    print('Your fifth letter is in today\'s word.')
          