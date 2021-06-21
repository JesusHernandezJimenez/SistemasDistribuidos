from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
import tkinter
from typing import Sized 
from PIL import ImageTk, Image

class Client(Frame):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        """self.cambiarUno = cambiarUno
        self.cambiarDos = cambiarDos"""

        self.pack(side="left", expand=True, fill="y",anchor="nw")
        #Frame_2.pack(side="left", expand=True, fill="x")
        self.config(width=300, bg="#1E262C")
        self.titulo= Label(self, text="TEXTO EN FRAME 2 JODER SI FUNCIONA PERRO", font=(
            "Verdana", 12), bg="#F08269", fg="black", anchor=NW)
        self.button_1 = Button(self, text="Boton1", font=("Verdana", 12), bg="#1E262C", fg="white",
                               anchor=NW, command=lambda: controller.show_frame(cambiar)).place(x=0, y=0, width=300, height=35)
        #self.button_2 = Button(self, text="Boton1", font=("Verdana", 12), bg="#1E262C", fg="white",
        #                       anchor=NW, command=lambda: controller.show_frame(client2.Client2)).place(x=0, y=34, width=300, height=35)
        #self.create_chat()
    def create_chat(self):
        self.quit = Button(self, text="QUIT", fg="red",command=self.destroy).place(x=0, y=64, width=300, height=35)
        #Label(Frame, text="LOGIN", font=("Impact", 20), fg="white", bg="#1E262C").place(anchor='n', rely=0.15, relx=0.5)
    def cambiar_a_unoF(self):
        self.cambiarUno()
        pass

    def cambiar_a_dosF(self):
        self.cambiarDos()
        pass
