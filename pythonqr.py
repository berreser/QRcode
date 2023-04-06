from tkinter import ttk
from tkinter import *
import qrcode
from PIL import Image, ImageTk


def generate_button():
    data = ent1.get()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")
    img = Image.open("qr_code.png")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    at.config(image=img)
    at.image = img


def exit_button():
    window.destroy()


window = Tk()
window.title("QRCODE")
window.configure(background="#D7BDE2")
window.geometry("500x500")

lbl1 = Label(window, text="Please enter the text.", height=3, width=30, background="#AF7AC5", fg="white")
lbl1.pack(pady=5)

ent1 = Entry(window, width=40)
ent1.pack(pady=10)

button1 = Button(window, text="click", command=generate_button, background="#AF7AC5", fg="white")
button1.pack(pady=15)

button2 = Button(window, text="Exit", command=exit_button, font=("Arial"), bg="#AF7AC5", fg="white")
button2.pack(pady=20)

at = Label(window)
at.pack(pady=25)

window.mainloop()
