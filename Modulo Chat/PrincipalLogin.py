from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
import tkinter
from typing import Sized 
import socketClient

def recibir():
    # Se maneja la recepción de mensajes
    while True:
        try:
            msg = client_socket.recv(1024).decode("utf8")
            msg_split = msg.split("@")
            print(msg_split)
            if len(msg_split) > 1:
                mensaje = msg_split[1]
                if mensaje == "Esta en Línea":
                    print("CHat")

            if len(msg_split) == 1:
                print("Mostrar nueva ventana")
                print(msg)

        except OSError:  # Posiblemente el cliente haya abandonado el chat
              
            break

def set_name():  # El evento es pasado por binders
    # Recibir el nombre del remitente
    msg = "@" + entry_user_text.get() + "@" + entry_user_password.get()
    print(msg)
    client_socket.send(bytes(msg, "utf8"))


def send():
    print(entry_user_text.get())

Login = Tk()
Login.geometry('350x600')
Login.configure(bg='#1E262C')
Login.eval('tk::PlaceWindow . center')

entry_user_text = tkinter.StringVar()
entry_user_password = tkinter.StringVar()

Label(Login, text="LOGIN", font=("Fedora", 20), fg="white",
bg="#1E262C").place(anchor='n', rely=0.15, relx=0.5)
Label(Login, text="Usuario", font=("Fedora", 14), fg="white", bg="#1E262C").place(anchor='n', rely=0.30, relx=0.5)
entry_usuario = tkinter.Entry(Login, textvariable=entry_user_text,  font=("Arial", 12), fg="black", bg="white")
entry_usuario.bind("<Return>", )
entry_usuario.place(anchor='n', rely=0.35, relx=0.5)
Label(Login, text="Contraseña", font=("Fedora", 14), fg="white",bg="#1E262C").place(anchor='n', rely=0.45, relx=0.5)
entry_password = tkinter.Entry(Login, textvariable=entry_user_password,show='*', font=("Impact", 12), fg="black", bg="white")
entry_password.bind("<Return>",)
entry_password.place(anchor='n', rely=0.50, relx=0.5)
b_enviar = tkinter.Button(Login, text="validar", font="Fedora 12 bold", height=1, border=3, relief="groove", fg="#483659", command = set_name)
b_enviar.place(anchor='n', rely=0.7, relx=0.5, width=300, height=35)

HOST = "localhost"
PORT = 50000
if not PORT:
    PORT = 50000
else:
    PORT = int(PORT)

ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
receive_thread = Thread(target=recibir)
receive_thread.start()

Login.mainloop()
