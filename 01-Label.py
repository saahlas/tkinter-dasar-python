from tkinter import *

app = Tk()
app.title("01-Label")
app.geometry("300x200")

label= Label(app, text="Hallo, ini Label!", font=("Arial", 14))
label.pack(pady=20)

app.mainloop()