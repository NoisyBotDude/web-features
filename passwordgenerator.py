import random

print("Length Of The Password?")
    # speak("Length Of The Password?")
n1 = input()
    # while not n1.isdigit():
    #     print("Length Of The Password In Number")
    #     n1 = input()

digits = '0123456789'

lowercase = 'abcdefghijklmnopqrstuvwxyz'

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

symbols = '!@#$%&'

combined_digits = digits + lowercase + uppercase + symbols

password1 = ''.join((random.choice(combined_digits)) for i in range(int(n1)))
print(f"Your Password Is : {password1}")