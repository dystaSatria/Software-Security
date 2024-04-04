import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
import random
import io

def generate_captcha():
    width = 300
    height = 100

    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    captcha_text = ''.join(random.choices("ABCDEFGHJKLMNPQRSTUVWXYZ23456789", k=6))

    # Metni rastgele bir yerde yerleştir
    font = ImageFont.load_default()
    text_width, text_height = draw.textsize(captcha_text, font)
    x = random.randint(0, width - text_width)
    y = random.randint(0, height - text_height)
    draw.text((x, y), captcha_text, font=font, fill=(0, 0, 0))

    # Gürültü ekleme
    for _ in range(100):
        draw.point((random.randint(0, width), random.randint(0, height)), fill=(0, 0, 0))

    # Çizgi ve şekiller ekleme
    for _ in range(5):
        draw.line((random.randint(0, width), random.randint(0, height), random.randint(0, width), random.randint(0, height)), fill=(0, 0, 0))
        draw.ellipse((random.randint(0, width), random.randint(0, height), random.randint(0, width), random.randint(0, height)), outline=(0, 0, 0))

    # Convert PIL image to Tkinter PhotoImage
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    photo = tk.PhotoImage(data=img_io.getvalue())

    label.config(image=photo)
    label.image = photo

def check_captcha():
    user_input = entry.get()
    if user_input == captcha_text:
        result_label.config(text="Doğru!")
    else:
        result_label.config(text="Yanlış!")

# Create Tkinter window
root = tk.Tk()
root.title("CAPTCHA Örneği")

# Label to display CAPTCHA image
label = tk.Label(root)
label.pack()

# Entry for user input
entry = tk.Entry(root)
entry.pack()

# Button to generate CAPTCHA
generate_button = tk.Button(root, text="Yenile", command=generate_captcha)
generate_button.pack()

# Button to check CAPTCHA
check_button = tk.Button(root, text="Kontrol Et", command=check_captcha)
check_button.pack()

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Generate initial CAPTCHA
generate_captcha()

root.mainloop()
