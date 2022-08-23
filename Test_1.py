import random

a = '2222222233332222222222'
b = '3333333322223333333333'


Num_key = a + b
length_for_key =20

num = ''.join(random.sample(Num_key, length_for_key))
print("Your numbers:",num)


key = str(input("Key:"))
if key == num:
    print("Welcome!")
else:
    print("SORRY...")

if 'Welcome!':
        print("Opppa")


