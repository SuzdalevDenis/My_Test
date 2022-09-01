import random

numbers = '1234567890123456789012345678901234567890'

length_for_key = 5

num_key = ''.join(random.sample(numbers, length_for_key))
print("Your numbers:", num_key)

key = str(input("Key:"))

Yes = "Welcome!"
No = "SORRY..."

if key == num:
    print(Yes)
else:
    print(No)
