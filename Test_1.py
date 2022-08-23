import random

lower_case = '2222222233332222222222'
upper_case = '3333333322223333333333'


Use_for = lower_case + upper_case
length_for_pass = 5

password = ''.join(random.sample(Use_for, length_for_pass))
print("Your password:",password)

key = str(input("Key:"))
if key == password:
    print("Welcome!")
else:
    print("SORRY...")