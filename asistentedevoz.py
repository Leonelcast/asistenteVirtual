from tkinter import *
from time import strftime
from PIL import ImageTk,Image

ws = Tk()
ws.title('PythonGuides')
ws.geometry('800x450')
ws.config(bg='white')
ws.resizable(False,False)
img = PhotoImage(file='img/wallpaper.png')
label = Label(
    ws,
    image=img,
    
)
label.place(x=0, y=0)

text = Text(
    ws,
    height=10,
    width=53
)
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
lbl = Label(ws, font = ('calibri', 40, 'bold'),
            background = 'grey',
            foreground = 'white')
lbl.pack(anchor = 'center')

#Imgenes de botontes
img1 = PhotoImage(file = "img/spotify.png")
img2 = PhotoImage(file = "img/alarm.png")
img3 = PhotoImage(file = "img/gmail.png")
img4 = PhotoImage(file = "img/search.png")
img5 = PhotoImage(file = "img/transcriptor.png")

button1 = Button(
    ws,
    image=img1,
    command= lambda:boton(1)
    
)
button1.place(x=120, y=380)
button2 = Button(
    ws,
    image=img2,
    command= lambda:boton(2)
)
button2.place(x=220, y=380)
button3 = Button(
    ws,
    image=img3,
    command= lambda:boton(3)
)
button3.place(x=320, y=380)
button4 = Button(
    ws,
    image=img4,
    command= lambda:boton(4)
)
button4.place(x=420, y=380)
button5 = Button(
    ws,
    ws.resizable(False,False),
    image=img5,
    command= lambda:boton(5)
)
button5.place(x=520, y=380)



def boton(press):
    if press == 1:
        from spotify import escuchar
        escuchar()
    if press == 2:
        from alarmaTemp import iniciar
        iniciar()
    if press == 3:
        from gmail import envioCorreo
        envioCorreo()
    if press == 4:
        from busqueda import escuchar
        escuchar()
    if press == 5:
        from transcriptor import escuchar
        escuchar()      

time()
  
mainloop()


ws.mainloop()