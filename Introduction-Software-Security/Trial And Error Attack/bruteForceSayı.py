def brute_force_pin(pin):
    for i in range(99999):
        # PIN kodunu dört haneli bir string olarak formatla
        guess = str(i).zfill(4)
        # Doğru tahmin kontrolü
        if guess == pin:
            return i, guess
    return -1,

# Tahmin edilecek PIN kodu
target_pin = "9999"

# Brute force tahmini başlatma
attempts, correct_guess = brute_force_pin(target_pin)

if attempts != -1:
    print(f"PIN '{correct_guess}' {attempts + 1} denemede tahmin edildi.")
else:
    print("PIN tahmin edilemedi.")

