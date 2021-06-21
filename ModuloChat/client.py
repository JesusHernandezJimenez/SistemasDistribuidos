from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
import tkinter
from typing import Sized 
from PIL import ImageTk, Image

def recibir():
    # Se maneja la recepción de mensajes
    while True:
        try:
            msg = client_socket.recv(1024).decode("utf8")
            msg_split = msg.split("@")
            print(msg_split)
            if len(msg_split) > 1:
                destino = msg_split[1]
                print(destino)
                if destino == remitente.get():
                    print(msg_split)
                    msg_list.insert(tkinter.END, "Remitente: " + msg_split[0])
                    msg_list.insert(tkinter.END, "Asunto: " + msg_split[2])
                    msg_list.insert(tkinter.END, "Mensaje: " + msg_split[3])
                    msg_list.insert(tkinter.END, " ")

            if len(msg_split) == 1:
                msg_list.insert(tkinter.END, msg)
                print(msg)

        except OSError:  # Posiblemente el cliente haya abandonado el chat
            principal.destroy()    
            break

def set_name():  # El evento es pasado por binders
    # Recibir el nombre del remitente
    msg = remitente.get()
    print(msg)
    client_socket.send(bytes(msg, "utf8"))

def send():
    # Se maneja el envío de mensajes
    if destinatario.get() != "" and mensaje.get() != "":
        msg = "@" + destinatario.get() + "@" + asunto.get() + "@" + mensaje.get()
        destinatario.set("")  # limpa o campo do destinatário
        asunto.set("")
        mensaje.set("")  # limpa o campo de mensagem
        client_socket.send(bytes(msg, "utf8"))

def exit():
    # Finalizar conexión
    msg = "quit"
    client_socket.send(bytes(msg, "utf8"))
    client_socket.close()
    window.destroy()
    principal.destroy()

def fecha():
    # Función que se manda a llamar cuando la ventana está cerrada
    mensaje.set("quit")
    send()

#Muestra es frame del chat
def mostrarChat():
    window.place(x=0, y=0)
#Ventana principal
principal = Tk()
principal.geometry("{0}x{1}+0+0".format(principal.winfo_screenwidth()-3, principal.winfo_screenheight()-3))
principal.configure(bg='#eff2fe')
#Parte gráfica 

window = Frame(principal, bg="white", width=500, height=300, bd=4,highlightbackground='black', highlightthickness=2)
window.configure(bg='#eff2fe')
#window.place(x=0, y=0)

chat_btn = PhotoImage(file='img/chat2.png')

chat_button = Button(principal,image = chat_btn,borderwidth=0, command=mostrarChat, bg='#eff2fe')
#window.place(x=510, y=280)
#window.title("Chat")
#window.configure(bg="#ffffff")
#window.geometry('760x450')
#window.geometry("{0}x{1}+0+0".format(
            #window.winfo_screenwidth()-3, window.winfo_screenheight()-3))  # Tamaño y posicionamiento

campo_conversacion= tkinter.Frame(window)
remitente = tkinter.StringVar()
destinatario = tkinter.StringVar()
asunto = tkinter.StringVar()
mensaje = tkinter.StringVar()

scrollbar = tkinter.Scrollbar(campo_conversacion)
scrollbar2 = tkinter.Scrollbar(campo_conversacion)

#window.combo = ttk.Combobox(window)
#window.combo.place(x=80, y=150)
l_remitente = tkinter.Label(window, text="   Remitente:", font="Ubuntu 14", width=11, height=2, bg="#ffffff")
l_destinatario = tkinter.Label(window, text=" Destinatario:", font="Ubuntu 14", width=11, height=2, bg="#ffffff")
l_asunto = tkinter.Label(window, text="       Asunto:", font="Ubuntu 14", width=11, height=2, bg="#ffffff")
l_mensaje = tkinter.Label(window, text="   Mensaje:", font="Ubuntu 14", width=11, height=2, bg="#ffffff")

l_conversacion = tkinter.Label(window, text=" Conversación: ", font="Ubuntu 14", height=2, bg="#ffffff")

msg_list = tkinter.Listbox(window, height=11, width=38, font="Ubuntu 12 bold", fg="#483659", border=2,
                           yscrollcommand=scrollbar.set)

e_remitente = tkinter.Entry(window, font="Fedora 12 bold", fg="#483659", textvariable=remitente)
e_remitente.bind("<Return>", )
e_destinatario = tkinter.Entry(window, font="Fedora 12 bold", fg="#483659", textvariable=destinatario)
e_destinatario.bind("<Return>", )
e_asunto = tkinter.Entry(window, font="verdana 12 bold", fg="#483659", textvariable=asunto)
e_asunto.bind("<Return>", )
e_mensaje = tkinter.Entry(window, font="Fedora 12 bold", fg="#483659", width=65, textvariable=mensaje)
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

# Ejecución de la interfaz
#window.mainloop()
principal.mainloop()
