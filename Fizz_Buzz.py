# Write a bizz and fizz game ##project

# Without loop
# Asks user for number
num = int(input('Whats your number? '))
#Run through game function
def fizz_buzz(num):
    # If remainder of number after being divided by 3 and 5 is 0 then return Bizzuu
    if num%3 == 0 and num%5 == 0:
        return 'Bizzuu'
    # If remainder of number after being divided by 3 then return Bizz
    if num%3 == 0:
        return 'Bizz'
    # If remainder of number after being divided by 5 then return Fizz
    if num%5 == 0:
        return 'Fizz'
    else:
        return 'Loser'

# In loop
while True:
    num = int(input('Whats your number? '))
    if num == 0:
        break
    if num % 3 == 0 and num % 5 == 0:
        print('Bizzizz')
        # If remainder of number after being divided by 3 then return Bizz
    elif num % 3 == 0:
        print('Bizz')
    elif num % 5 == 0:
        print('Fizz')
    else:
        print(num)


# print user input number and the function output
#print(num, (fizz_buzz(num)))







## separating parts of a computer program into modules that deal with a single feature or behavior


# Definition of done for the project:
# This should be it's own project
# it should have a read me
    # it should outline the project
    # it should have simple instructions on how to run the project
# it should have git and git history
# it should be on git hub