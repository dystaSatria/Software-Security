import itertools
import string
import time

def brute_force_password(target):

    chars = string.ascii_lowercase  # a'dan z'ye tüm küçük harfler
    attempts = 0
    start_time = time.time()

    # 1'den 5'e kadar (5 dahil değil) tüm kombinasyon uzunluklarını dene
    for length in range(1, 5):
        # İtertools.product, verilen karakter setiyle tüm mümkün kombinasyonları üretir
        for guess in itertools.product(chars, repeat=length):
            # Kombinasyonları birleştirerek bir string oluştur
            guess = ''.join(guess)
            attempts += 1
            if guess == target:
                duration = time.time() - start_time
                return attempts, duration
    return -1, 

# Hedef şifre
target_password = "abcd"

# Brute force şifre tahmini başlat
attempts, time_taken = brute_force_password(target_password)

if attempts != -1:
    print(f"Şifre '{target_password}' {attempts} denemede {time_taken:.2f} saniyede tahmin edildi.")
else:
    print("Şifre tahmin edilemedi.")
