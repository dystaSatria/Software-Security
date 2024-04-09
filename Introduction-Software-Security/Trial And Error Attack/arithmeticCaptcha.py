import tkinter as tk
import random

def generate_arithmetic_captcha():

    # İşlemde kullanılacak rastgele sayıları oluştur
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Rastgele işlem seçimi
    operator = random.choice(['+', '-', '*'])
    
    # İşlem metnini oluştur
    if operator == '+':
        operation = f"{num1} + {num2}"
        result = num1 + num2
    elif operator == '-':
        operation = f"{num1} - {num2}"
        result = num1 - num2
    else:
        operation = f"{num1} * {num2}"
        result = num1 * num2
    
    return operation, result

def check_answer():
    # Kullanıcının girdiği cevabı kontrol et
    user_answer = entry.get()
    if user_answer.isdigit() and int(user_answer) == result:
        result_label.config(text="Doğru cevap! CAPTCHA doğrulandı.", fg="green")
    else:
        result_label.config(text="Yanlış cevap! CAPTCHA doğrulanamadı.", fg="red")

# CAPTCHA oluştur
operation, result = generate_arithmetic_captcha()

# Tkinter uygulamasını başlat
root = tk.Tk()
root.title("Aritmetik CAPTCHA")

# İşlemi göster
operation_label = tk.Label(root, text=operation)
operation_label.pack()

# Cevap giriş kutusu
entry = tk.Entry(root)
entry.pack()

# Doğrulama butonu
verify_button = tk.Button(root, text="Doğrula", command=check_answer)
verify_button.pack()

# Sonuç etiketi
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
