from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
import tkinter
from tkinter.font import BOLD
from typing import Sized 
from tkinter import messagebox as MessageBox
import socketClient

def recibir():
    # Se maneja la recepción de mensajes
    while True:
        try:
            msg = client_socket.recv(1024).decode("utf8")
            msg_split = msg.split("@")
            print(msg)
           
            if msg == "rootEsta en Línea":
                Login.destroy()
                print("CHat")
                print(msg)

            if msg == "Datos incorrectos":
                MessageBox.showwarning("Aviso", "Datos Incorrectos")
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

LoginPrincipal = Tk()
LoginPrincipal.title("Iniciar Sesión")
app_width = 500
app_height = 650
screen_width = LoginPrincipal.winfo_screenwidth()
scren_height = LoginPrincipal.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (scren_height /2) - (app_height / 2)
LoginPrincipal.geometry(f'{app_width}x{app_height}+{int (x)}+{int (y)}')
LoginPrincipal.config(bg="#b5cdf9")

    

Login = Frame(LoginPrincipal)
#Login.title("Iniciar Sesión")
#Login.geometry('350x600')
#Login.configure(bg='#5b8efb')
#sLogin.eval('tk::PlaceWindow . center')

Login.config(bg="#e6efff")
Login.config(width=400, height=600)
Login.pack(pady=50)

entry_user_text = tkinter.StringVar()
entry_user_password = tkinter.StringVar()

Label(Login, text="LOGIN", font=("Fedora", 20), fg="#2c3c60",
bg="#e6efff").place(anchor='n', rely=0.15, relx=0.5)
Label(Login, text="Usuario", font=("Fedora", 14), fg="#2c3c60", bg="#e6efff").place(anchor='n', rely=0.30, relx=0.35)
entry_usuario = tkinter.Entry(Login, textvariable=entry_user_text,  font=("Arial", 12), fg="black", bg="white")
entry_usuario.bind("<Return>", )
entry_usuario.place(anchor='n', rely=0.35, relx=0.5)
Label(Login, text="Contraseña", font=("Fedora", 14), fg="#2c3c60",bg="#e6efff").place(anchor='n', rely=0.45, relx=0.40)
entry_password = tkinter.Entry(Login, textvariable=entry_user_password,show='*', font=("Arial", 12), fg="black", bg="white")
entry_password.bind("<Return>",)
entry_password.place(anchor='n', rely=0.50, relx=0.5)
b_enviar = tkinter.Button(Login, text="INGRESAR", font=("Arial", 12), height=1, border=3, relief="flat", fg="white", bg="#b09cdb", command = set_name)
b_enviar.place(anchor='n', rely=0.6, relx=0.5, width=185, height=30)


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


LoginPrincipal.mainloop()
