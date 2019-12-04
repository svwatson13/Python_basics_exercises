user_input = input('What is it you want my sweet child? ')
Mr_Miyagi = 'Young grasshopper,'
training_complete = 'Sensei, I am at peace'

# While loop meaning that the participant remains in the game until they say 'Sensei, I am at peace
while True:
    if 'sensei, i am at peace' in user_input.lower():
        print('You are the chosen one:  I shall depart you with one gem of wisdom... sometimes, what heart know, head forget')
        # Breaks loop
        break
    else:
        # If the user asks a question
        if "?" in user_input:
            print(Mr_Miyagi,'questions are wise, but for now wax on, and wax off!')
            user_input = input('What is it you want my sweet child? ')
        # If the user doesn't address Mr.Miyagi as Sensei
        if user_input.startswith("Sensei") or user_input.startswith("sensei"):
            user_input = input('What is it you want my sweet child? ')
        else:
            print(Mr_Miyagi, 'you are smart, but not wise - address me as Sensei please')
            user_input = input('What is it you want my sweet child? ')
            # If the user says block
            if "block" in user_input or "blocking" in user_input:
                print(Mr_Miyagi, 'remember, best block, not to be there')
                user_input = input('What is it you want my sweet child? ')
            else:
                print(Mr_Miyagi, 'Do not lose focuse. Wax on. Wax off.')



