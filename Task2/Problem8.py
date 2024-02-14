import random
import string
def main():
    options = string.ascii_letters + string.digits
    password = ""
    for _ in range(8):
        password += random.choice(options)
    print(password)
main()