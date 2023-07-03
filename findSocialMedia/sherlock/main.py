import tkinter as tk
import subprocess

def run_sherlock():
    # Mendapatkan username dari input pengguna
    username = username_entry.get()

    # Menjalankan perintah "py sherlock" dengan username yang dimasukkan oleh pengguna
    process = subprocess.Popen(["py ", "sherlock", username],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               universal_newlines=True)

    # Membaca output dari proses
    output, error = process.communicate()

    # Menghapus teks yang sudah ada pada Text widget
    output_text.delete("1.0", tk.END)

    # Menampilkan output hasil perintah di Text widget
    output_text.insert(tk.END, output)

# Membuat window utama
window = tk.Tk()
window.title("Sherlock Program with Interface by dystaSatria")
window.configure(background='black')
font_style = ('Arial', 12, 'bold')

# Membuat label dan entry untuk memasukkan username
attention = tk.Label(window, text="Find The Social Medias Target's Username", font=font_style)
attention.pack(pady=30)
username_label = tk.Label(window, text="Username:", font=font_style)
username_label.pack(pady=10)

username_entry = tk.Entry(window)

username_entry.pack(pady=10)

# Membuat tombol "Run" untuk menjalankan Sherlock
run_button = tk.Button(window, text="Run", command=run_sherlock,  font=font_style)
run_button.pack()

# Membuat Text widget untuk menampilkan output
output_text = tk.Text(window, background='whitesmoke')
output_text.pack(pady=20)

# Menjalankan event loop utama
window.mainloop()
