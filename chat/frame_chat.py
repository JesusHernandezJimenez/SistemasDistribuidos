from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
import tkinter
from typing import Sized
from PIL import ImageTk, Image

class Frame_chat(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, ** kwargs)
        self.pack(side="left", expand=True, fill="both")
        self.config(height=720, width=980, bg="#D2EBFA")
        label_1 = Label(self, text="Chat", font=("Arial Black", 20), bg="#D2EBFA",fg="black", anchor=NW).place(relx=0.02, y=0, width=300, height=35)
        #campo_conversacion = tkinter.Frame(window)
        remitente = tkinter.StringVar()
        destinatario = tkinter.StringVar()
        asunto = tkinter.StringVar()
        mensaje = tkinter.StringVar()

        scrollbar = tkinter.Scrollbar(self)
        scrollbar2 = tkinter.Scrollbar(self)
        """
        remitente = tkinter.StringVar()
        destinatario = tkinter.StringVar()
        asunto = tkinter.StringVar()
        mensaje = tkinter.StringVar()

        scrollbar = tkinter.Scrollbar(campo_conversacion)
        scrollbar2 = tkinter.Scrollbar(campo_conversacion)

        #window.combo = ttk.Combobox(window)
        #window.combo.place(x=80, y=150)
        l_remitente = tkinter.Label(
            window, text="   Remitente:", font="Ubuntu 14", width=11, height=2, bg="#ffffff")
        l_destinatario = tkinter.Label(
            window, text=" Destinatario:", font="Ubuntu 14", width=11, height=2, bg="#ffffff")
        l_asunto = tkinter.Label(window, text="       Asunto:",
                                font="Ubuntu 14", width=11, height=2, bg="#ffffff")
        l_mensaje = tkinter.Label(window, text="   Mensaje:",
                                font="Ubuntu 14", width=11, height=2, bg="#ffffff")

        l_conversacion = tkinter.Label(
            window, text=" Conversación: ", font="Ubuntu 14", height=2, bg="#ffffff")

        msg_list = tkinter.Listbox(window, height=11, width=38, font="Ubuntu 12 bold", fg="#483659", border=2,
                                yscrollcommand=scrollbar.set)

        e_remitente = tkinter.Entry(
            window, font="Fedora 12 bold", fg="#483659", textvariable=remitente)
        e_remitente.bind("<Return>", )
        e_destinatario = tkinter.Entry(
            window, font="Fedora 12 bold", fg="#483659", textvariable=destinatario)
        e_destinatario.bind("<Return>", )
        e_asunto = tkinter.Entry(window, font="verdana 12 bold",
                                fg="#483659", textvariable=asunto)
        e_asunto.bind("<Return>", )
        e_mensaje = tkinter.Entry(window, font="Fedora 12 bold",
                                fg="#483659", width=65, textvariable=mensaje)
        e_mensaje.bind("<Return>", )

        b_enviar_remitente = tkinter.Button(window, text="    Enviar    ", font="Fedora 12 bold", height=1, border=3,
                                            relief="groove", fg="#483659", command=set_name)
        b_enviar = tkinter.Button(window, text="Enviar Mensaje", font="Fedora 12 bold", height=1, border=3,
                                relief="groove", fg="#483659", command=send)
        b_salir = tkinter.Button(window, text="Salir", font="Fedora 12 bold", fg="red", border=3, relief='groove',
                                command=window.place_forget)

        scrollbar.grid()
        msg_list.grid(row=2, column=3)
        campo_conversacion.grid(column=3)

        l_remitente.grid(row=1, column=1, sticky="n")
        l_destinatario.grid(row=2, column=1)
        l_asunto.grid(row=3, column=1)
        l_mensaje.grid(row=4, column=1)
        l_conversacion.grid(row=1, column=3)

        e_remitente.grid(row=1, column=2)
        e_destinatario.grid(row=2, column=2)
        e_asunto.grid(row=3, column=2)
        e_mensaje.grid(row=4, column=2, columnspan=6)

        b_enviar.grid(row=5, column=2, sticky="n")
        b_enviar_remitente.grid(row=2, column=2, sticky="n")
        b_salir.grid(row=5, column=3)
        chat_button.pack(pady=20, side=BOTTOM)
"""
