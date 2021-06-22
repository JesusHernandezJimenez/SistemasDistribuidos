from tkinter import *
from chat import client, client2, client3, botones, frame_chat
from login import registro, login
from PIL import ImageTk, Image


class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Proyecto")
        self.resizable(True, True)
        self.geometry("1280x720")
        self.init()
        #frame_login = login.Login(master=self, init=self.init, validar_usuario=self.login_frame_validate)
    def cambiar(self):
        self.frame_m.destroy()
        self.frame_m = client2.Client2(self.container)

    def show(self):
        self.frame_m.destroy()
        self.frame_m = client3.Client3(self.container)

    def chat(self):
        self.frame_m.destroy()
        self.frame_m = frame_chat.Frame_chat(self.container)

    def login_frame_validate(self, user, password):
        if user == 'admin' and password == 'admin':
            print("Logeado con exito")
            return True

    def init(self):
        frame_botones = Frame(self)
        frame_botones.pack(side="left", expand=True, fill="y", anchor="nw")
        frame_botones.config(width=300, bg='#1E262C')

        self.container = Frame(self)
        self.container.pack(side="left", expand=True, fill="x")
        self.container.config(height=720, width=980)
        self.frame_m = Frame
        self.frame_m = frame_chat.Frame_chat(self.container)
        frame_botones.button_1 = Button(frame_botones, text="Chat", font=("Verdana", 14), bg="#1E262C", fg="white", anchor=NW,command=self.chat).place(x=0, y=0, width=300, height=35)
        frame_botones.button_2 = Button(frame_botones, text="Ayuda", font=("Verdana", 14), bg="#1E262C", fg="white", anchor=NW,command=self.show).place(x=0, y=36, width=300, height=35)
        #frame_botones.button_2 = Button(frame_botones, text="Boton2", font=("Verdana", 14), bg="#1E262C", fg="white", anchor=NW,command=self.show).place(x=0, y=72, width=300, height=35)
        #frame_botones.button_2 = Button(frame_botones, text="Boton3", font=("Verdana", 14), bg="#1E262C", fg="white", anchor=NW,command=self.cambiar).place(x=0, y=108, width=300, height=35)
#Iniciar el programa principal
root = App()
root.mainloop()
