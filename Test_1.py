import random

numbers = '1234567890123456789012345678901234567890'

length_for_key = 5

num = ''.join(random.sample(numbers, length_for_key))
print("Your numbers:", num)

key = str(input("Key:"))

Yes = "Welcome!"
No = "SORRY..."

if key == num:
    print(Yes)
else:
    print(No)
