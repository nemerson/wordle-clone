todays_word = 'media'
player_guess = input('Enter a 5 letter word: ')
todays_word = todays_word.lower()
player_guess = player_guess.lower()
checked_guess = ''


if player_guess == todays_word :
    print('Correct!')
elif player_guess[0] == todays_word[0] :
    checked_guess[0] = player_guess[0].upper()
elif player_guess[0] in todays_word :
    checked_guess[0] = player_guess[0]
else :
    checked_guess[0] = 'x'      


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
          