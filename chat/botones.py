from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
import tkinter
from typing import Sized
from PIL import ImageTk, Image


class Botones(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(side="left", expand=True, fill="y", anchor="nw")
        self.config(width=300, bg='#1E262C')

        self.button_1 = Button(self, text="Boton1", font=("Verdana", 12), bg="#1E262C", fg="white", anchor=NW, command=lambda: controller.show_frame(cambiar)).place(x=0, y=0, width=300, height=35)
        #self.create_chat(master)
