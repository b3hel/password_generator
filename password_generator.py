import random
print("Welcome to the password generator!")
print("Choose the difficulty level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")
difficulty = input("Enter the difficulty level (1, 2, or 3): ")
if difficulty == "1":
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    all_chars = letters
elif difficulty == "2":
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    all_chars = letters + numbers
elif difficulty == "3":
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()"
    all_chars = letters + numbers + symbols
else:
    print("Invalid difficulty level!")
    exit()


print("Enter the desired password length, it should be at least 8 characters.")
try:
    length = int(input("Enter the desired password length: "))
except:
    print("Enter a number!")
    exit()
if length < 8:
    print("Password length should be at least 8 characters!")
    exit()
else:    print("Generating password...")

password = ""

for _ in range(length):
    password += random.choice(all_chars)

print("Your password:", password)