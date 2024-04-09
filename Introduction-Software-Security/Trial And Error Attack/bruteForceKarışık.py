import itertools
import string

def brute_force_password(target):

    characters = string.digits + string.ascii_letters  # Sayılar ve harfler
    attempts = 0
    
    # 1'den 6'ya kadar şifre uzunluğunu deneyerek brute force yap
    for length in range(1, 6):
        for guess in itertools.product(characters, repeat=length):
            # Tahmin edilen karakterleri birleştir
            guess = ''.join(guess)
            attempts += 1
            if guess == target:
                return attempts, guess
    return -1, 

# Tahmin edilecek şifre
target_password = "111a2b"

# Brute force tahmini başlat
attempts, correct_guess = brute_force_password(target_password)

if attempts != -1:
    print(f"Şifre '{correct_guess}' {attempts} denemede tahmin edildi.")
else:
    print("Şifre tahmin edilemedi.")
