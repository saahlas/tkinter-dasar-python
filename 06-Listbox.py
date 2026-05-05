from tkinter import *

def tampilkan():
    selected = listbox.curselection()
    if selected:
        nilai = listbox.get(selected[0])
        label_hasil.config(text=f"Kamu memilih: {nilai}")
    else:
        label_hasil.config(text="Pilih salah satu dulu!")

app = Tk()
app.title("07 - Listbox")
app.geometry("300x300")

Label(app, text="Pilih mata kuliah:", font=("Arial", 12)).pack(pady=10)

listbox = Listbox(app, width=30, height=5)
listbox.pack(pady=5)

matkul = ["Basis Data", "Sistem Operasi", "Probstat", "Bahasa Inggris", "Pancasila"]
for m in matkul:
    listbox.insert(END, m)

Button(app, text="Pilih", command=tampilkan).pack(pady=10)

label_hasil = Label(app, text="", font=("Arial", 11), fg="green")
label_hasil.pack(pady=5)

app.mainloop()