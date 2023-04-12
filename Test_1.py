import random
import time

id_personal = str(input('Your ID:'))
id_and_personal = {
    '22003': 'Alex Wolfski',
    '34556': 'Maya Doorwelle',
    '22002': 'Rei Ayanami',
    '33445': 'Drez_Den_'
}
numbers = '1234567890123456789012345678901234567890'
length_for_key = 6
num_key = ''.join(random.sample(numbers, length_for_key))

yes = "Welcome!"
no = "SORRY..."

seconds = time.time()
localTime = time.ctime(seconds)


def correct_key():
    if key == num_key:
        print(yes)
        if yes:
            return'Yes'
    else:
        print(no)
        if no:
            return'No'




if id_personal in id_and_personal:
    print(f"Hello {id_and_personal[id_personal]}!")
    print("Your numbers:", num_key)
    key = str(input("Key:"))
    print(correct_key())
    print(localTime)
else:
    print('Who are you? Get out!')
    print(localTime)


time_list = list(localTime)


def between_extremes(numbers):
    return max(numbers) - min(numbers)

