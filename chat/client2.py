from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
import tkinter
from typing import Sized 
from PIL import ImageTk, Image
class Client2(Frame):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, ** kwargs)
        self.pack(side="left", expand=True, fill="both")
        self.config(height=720, width=980, bg="#9722D6")
        #container.configure(bg="#9722D6")

        label_1 = Label(self, text="UNO", font=(
            "Verdana", 12), bg="#9722D6", fg="black", anchor=NW).place(x=0, y=0, width=300, height=35)
        #label_1 = Label(container, text="JODER BUENAS TARDES", font=("Verdana", 12),bg="blue", fg="black", anchor=NW).place(x=0, y=0, width=300, height=35)
        #self.create_chat(master)
