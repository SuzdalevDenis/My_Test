import random

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
