from tkinter import *
from tkinter import messagebox

def hitung():
    try:
        a=float(entry1.get())
        b=float(entry2.get())

        tinggi = b/100
        bmi = a / (tinggi**2)

        if bmi < 18.5:
            kategori = 'Kurus'
        elif bmi < 25:
            kategori = 'Normal'
        elif bmi < 30:
            kategori = 'Gemuk'
        else:
            kategori = 'Obesitas'
        
        label_hasil.config(text=f"BMI: {bmi}\n Kategori: {kategori}")

    except ValueError:
        messagebox.showerror(text="Error, masukkan angka!")

app = Tk()
app.geometry('400x400')
app.title("Kalkulator BMI")

label1=Label(app, text='KALKULATOR BMI', font=('Times New Romance', 15, 'bold'))
label1.pack(pady=3)


frame1= Frame(app)
frame1.pack(pady=5)

label2=Label(frame1, text="Berat badan", width=15, anchor='w')
label2.pack(side=LEFT)
entry1=Entry(frame1)
entry1.pack(side=LEFT)

frame2=Frame(app)
frame2.pack(pady=5)

label3=Label(frame2, text="Tinggi Badan", width=15, anchor='w')
label3.pack(side=LEFT)
entry2=Entry(frame2)
entry2.pack(side=LEFT)

Button(app, text='Hitung BMI', command=hitung).pack(pady=5)

label_hasil=Label(app, text="")
label_hasil.pack(pady=10)

app.mainloop()