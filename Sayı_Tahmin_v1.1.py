from tkinter import *
import random

def basla():
    global sayi
    sayi = random.randint(1,300)
    etiket1.destroy()
    baslaButon.destroy()
    global etiket2
    etiket2 = Label(font = "Helvetica 20 bold")
    etiket2.pack(pady=15)
    global giris
    giris=Entry()
    giris.pack(pady = 15)
    dugme = Button(text="Tahmin Et", command = tahmin_et)
    dugme.pack(pady=15)
    


def tahmin_et():
    tahmin = int(giris.get())
    giris.delete(0,END)

    if tahmin == sayi:
        etiket2.config(text = "Bildiniz...Tebrikler")
    elif tahmin < sayi:
        etiket2.config(text = "Tahmininizi Arttırın")
    elif tahmin > sayi:
        etiket2.config(text = "Tahmininizi Alçaltın")

pencere = Tk()
pencere.geometry("600x300")
pencere.title("Sayı Tahmin Oyunu")

etiket1 = Label(text=""" 1 ile 300 arasında bir sayı tuttum,
Basla butonuna basarak oyuna başlayabilirsiniz""",font="Helvetica, 12 bold")
etiket1.place(relx = 0.1, rely = 0.3)

baslaButon = Button(text="Oyuna Başla",width =10, command = basla)
baslaButon.place(relx = 0.4,rely = 0.6)
mainloop()
        


    
