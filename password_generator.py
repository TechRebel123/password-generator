import string
import random

def generate_password(length):
    
    chars = string.ascii_letters + string.digits + string.punctuation
   
    password = ''.join(random.choice(chars) for i in range(length))
    return password

length = int(input("Enter the length of password: "))
password = generate_password(length)
print("Generated password:", password)