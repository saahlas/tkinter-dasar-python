from tkinter import *

def klik():
    label.config(text="Tombol diklik!")

app = Tk()
app.title("02-Button")
app.geometry("300x200")

label=Label(app, text="Klik tombol di bawah", font=("Arial, 12"))
label.pack(pady=20)

button = Button(app, text="Klik Aku!", command=klik)
button.pack(pady=10)

app.mainloop()