import random

a = '1234567890123456789012345678901234567890'

Num_key = a
length_for_key =8


num = ''.join(random.sample(Num_key, length_for_key))
print("Your numbers:",num)


key = str(input("Key:"))

Yes = "Welcome!"
No = "SORRY..."

if key == num:
    print(Yes)
else:
    print(No)


