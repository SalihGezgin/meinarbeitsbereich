import random

name=input("Please enter your name and sirname without any space :").lower()
password_name = ""
password_length_name = 3
for x in range(password_length_name):
    password_name += random.choice(name)

numbers = "0123456789"
password_num= ""
password_length_num = 4
for x in range(password_length_num):
    password_num += random.choice(numbers)

password = password_name + password_num
print(password)

mtu5707

import random
name=input("Please enter your name and sirname without any space :").lower()
password_name = ""
password_length_name = 3
for x in range(password_length_name):
    password_name += random.choice(name)

print(password_name)

ejn

numbers = "0123456789"
password_num= ""
password_length_num = 4
for x in range(password_length_num):
    password_num += random.choice(numbers)

print(password_num)

2766

password = password_name + password_num
print(password)

ejn2766

def password():
    import random

    name=input("Please enter your name and sirname without any space :").lower()
    password_name = ""
    password_length_name = 3
    for x in range(password_length_name):
        password_name += random.choice(name)

    numbers = "0123456789"
    password_num= ""
    password_length_num = 4
    for x in range(password_length_num):
        password_num += random.choice(numbers)

    password = password_name + password_num
    print(password)
    password()
    
def3921

def isVowel(char):
    return char.lower() in 'aeiou'

word = input("Please enter a string: ")

def isConsecutive(word):
    # initialize vowel count
    vCounter = 0
    for letter in word:
        if isVowel(letter): # <= check if the letter is a vowel
            vCounter += 1
            if vCounter >= 2: # <= do the check right here
                return 'Positive'
        else:
            vCounter = 0

    return 'Negative' # <= if we did not find three vovels in the loop, then there is none

print("Please enter a string: " + word)
print(str(isConsecutive(word)))

Please enter a string: eew
Positive
'wsaxeertz'