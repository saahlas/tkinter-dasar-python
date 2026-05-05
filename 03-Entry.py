from tkinter import *

def tampilkan():
    nama = entry.get()
    label_hasil.config(text=f"Hallo, {nama}!")

app = Tk()
app.title("03-Entry")
app.geometry("300x200")

Label(app, text="Masukkan namamu:", font=("Arial", 12)).pack(pady=10)

entry = Entry(app, width=25)
entry.pack(pady=5)

Button(app, text="Tampilkan", command=tampilkan).pack(pady=5)

label_hasil = Label(app, text="", font=("Arial", 12), fg="blue")
label_hasil.pack(pady=10)

app.mainloop()