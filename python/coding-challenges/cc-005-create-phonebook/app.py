def print_menu():
    print("Welcome to the phonebook application.")
    print('1. Find phone number.')
    print('2. Insert a phone number.')
    print('3. Delete a person from the phonebook.')
    print('4. Terminate!')
    print()

def find(name):
    if name in phonebook:
        print(phonebook[name])
    else:
        print("Kayit bulunamadi!")

def delet(name):
    if name in phonebook:
        del phonebook[name]
        print("Kayit silindi!")
    else:
        print("Kayit bulunamadi!")


phonebook = {
    'Qay' :	'1234',
    'Wsx' :	'2347',
    'Zgv' :	'4324',
    'Wsx' :	'3333',
    'Tgb' :	'5432',
    'Zhb' :	'9876',
    'Esy' :	'1111',
    'Edc' :	'9876' }
menu_choice = 0
print_menu()
while menu_choice <= 4:
    menu_choice = int(input("Type in a number (1-4): "))
    if menu_choice == 1:
        print("Find phone number.")
        name = input("Name: ").title()
        find(name)
    elif menu_choice == 2:
        print("Insert a phone number.")
        name = input("Name: ").title()
        phone = input("Number: ")
        phonebook.update({name:phone})
        phonebook[name] = phone
    elif menu_choice == 3:
        print('Insert a name to delete own phone number.')
        name = input("Name: ").title()
        delet(name)
    elif menu_choice == 4:
        print('Terminate!')
        break
    else:
        print("Welcome to the phonebook application.Please insert 1..4")


Welcome to the phonebook application.
1. Find phone number.
2. Insert a phone number.
3. Delete a person from the phonebook.
4. Terminate!

Find phone number.
1234
Terminate!
In [20]:
print(phonebook)
{'Wsx': '3333', 'Zgv': '4324', 'Tgb': '5432', 'Zhb': '9876', 'Esy': '1111', 'Edc': '9876'}
In [ ]: