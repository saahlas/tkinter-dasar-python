from tkinter import *

app = Tk()
app.title("04-Frame")
app.geometry("300x250")

frame_atas = Frame(app, bg="lightblue", width=280, height=100)
frame_atas.pack(pady=10, padx=10)

Label(frame_atas, text="Frame Atas", bg="lightblue", font=("Arial", 12)).pack(pady=30)

frame_bawah = Frame(app, bg="lightyellow", width=280, height=100)
frame_bawah.pack(pady=5, padx=10)

Label(frame_bawah, text="Frame Bawah", bg="lightyellow", font=("Arial", 12)).pack(pady=30)

app.mainloop()