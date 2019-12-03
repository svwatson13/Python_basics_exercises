import random, time

Magic_number = random.randint(1, 10)


IF statements for the magic number game with time and real answer

if User_number == Magic_number:
    print('WELL DONE YOU SMASHED IT')
elif User_number < Magic_number:
    print('Too low my friend')
    time.sleep(0.5)
    print('Real Answer: ', Magic_number)
elif User_number > Magic_number:
    print('Too high ol chum')
    time.sleep(0.5)
    print('Real Answer: ', Magic_number)

WHILE loop for magic number game so can keep guessing

User_number = int(input('Pick a number between 1 and 10: '))
while True:
    if User_number == Magic_number:
        print('WELL DONE YOU SMASHED IT')
        break
    elif User_number < Magic_number:
        print('Too low my friend')
        User_number = int(input('Pick a number between 1 and 10: '))
    elif User_number > Magic_number:
        print('Too high ol chum')
        User_number = int(input('Pick a number between 1 and 10: '))