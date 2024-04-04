import random
import string
import itertools

def generate_random_password(length=4):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def brute_force_password(target):
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    for length in range(1, len(target) + 1):
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == target:
                return attempts, guess
    return -1,

# Rastgele bir şifre oluştur
target_password = generate_random_password(4)
print(f"Hedef Şifre: {target_password}")

# Brute force tahmini başlat
attempts, correct_guess = brute_force_password(target_password)

if attempts != -1:
    print(f"Şifre '{correct_guess}' {attempts} denemede bulundu.")
else:
    print("Şifre bulunamadı.")
