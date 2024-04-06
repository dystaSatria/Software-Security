import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
import random
import io

def generate_captcha():
    global captcha_text  # CAPTCHA metnini global bir değişkene atıyoruz

    width = 200
    height = 100

    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(image)

    captcha_text = ''.join(random.choices("ABCDEFGHJKLMNPQRSTUVWXYZ23456789", k=6))

    # Metni rastgele bir yerde yerleştir
    text_bbox = draw.textbbox((0, 0), captcha_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    draw.text((x, y), captcha_text, font=font, fill=(0, 0, 0))

    for _ in range(100):
        draw.point((random.randint(0, width), random.randint(0, height)), fill=(0, 0, 0))

    # Convert PIL image to Tkinter PhotoImage
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    photo = tk.PhotoImage(data=img_io.getvalue())

    label.config(image=photo)
    label.image = photo

def check_captcha():
    entered_text = entry.get()  # Kullanıcının girdiği metni al
    if entered_text == captcha_text:
        result_label.config(text="Doğru!")
    else:
        result_label.config(text="Yanlış!")

# Create Tkinter window
root = tk.Tk()
root.title("CAPTCHA Example")

# Button to generate CAPTCHA
generate_button = tk.Button(root, text="Yenile", command=generate_captcha)
generate_button.pack()

# Label to display CAPTCHA image
label = tk.Label(root)
label.pack()

# Entry for user input
entry = tk.Entry(root)
entry.pack()

# Button to check CAPTCHA
check_button = tk.Button(root, text="Kontrol Et", command=check_captcha)
check_button.pack()

# Label to display result
result_label = tk.Label(root)
result_label.pack()

# Generate initial CAPTCHA
generate_captcha()

root.mainloop()
