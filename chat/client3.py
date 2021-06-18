from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
import tkinter
from typing import Sized
from PIL import ImageTk, Image


class Client3(Frame):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, ** kwargs)
        self.pack(side="left", expand=True, fill="both")
        self.config(height=720, width=980, bg="blue")
        label_1 = Label(self, text="DOS", font=("Verdana", 12), bg="blue", fg="white", anchor=NW).place(x=0, y=0, width=300, height=35)
        #self.create_chat(master)
