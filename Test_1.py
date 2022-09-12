import random

#personal = str(input('First name Last name:'))
id_personal = str(input('Your ID:'))
personal_list_and_id = {'22003AW_personal': 'Alex Wolfski', '34556MD_personal': 'Maya Doorwelle', '22002RA_admin': 'Rei Ayanami', 'u': '33445'}

if id_personal in personal_list_and_id:
    print("Hello!")
else:
    print('Who are you? Get out!')


numbers = '1234567890123456789012345678901234567890'

length_for_key = 6

num_key = ''.join(random.sample(numbers, length_for_key))
print("Your numbers:", num_key)

key = str(input("Key:"))

yes = "Welcome!"
no = "SORRY..."

if key == num_key:
    print(yes)
    if yes:
        print('Yes')
else:
    print(no)
    if no:
        print('No')
