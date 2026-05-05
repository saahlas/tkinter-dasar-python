from tkinter import *

def tampilkan():
    hasil = []
    if var1.get(): hasil.append("Python")
    if var2.get(): hasil.append("Tkinter")
    if var3.get(): hasil.append("MySQL")
    label_hasil.config(text="Dipilih: " + ", ".join(hasil) if hasil else "Tidak ada yang dipilih")

app = Tk()
app.title("05 - Checkbutton")
app.geometry("300x250")

Label(app, text="Pilih yang kamu pelajari:", font=("Arial", 12)).pack(pady=10)

var1 = BooleanVar()
var2 = BooleanVar()
var3 = BooleanVar()

Checkbutton(app, text="Python", variable=var1).pack()
Checkbutton(app, text="Tkinter", variable=var2).pack()
Checkbutton(app, text="MySQL", variable=var3).pack()

Button(app, text="Tampilkan", command=tampilkan).pack(pady=10)

label_hasil = Label(app, text="", font=("Arial", 11), fg="green")
label_hasil.pack(pady=5)

app.mainloop()