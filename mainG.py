from tkinter import *
from login import registro, login
from PIL import ImageTk, Image
def delete():
    frame_login.forget()
    for widgets in frame_login.winfo_children():
        widgets.destroy()
    #frame_login.winfo_children()
    frame_login.destroy()
    #frame_registro.destroy()
    init()

def loginFrame(root):
    windows = Toplevel(root)
    windows.title("Proyecto")
    windows.resizable(False, False)
    windows.geometry("400x800")


def login_frame_validate(user, password):
    if user == 'admin' and password == 'admin':
        print("Logeado con exito")
        #init()
        #delete()
        return True
def botton_1_cambiar():
    Frame_3.forget()
    Frame_2.pack(side="left", expand=True, fill="x")


def botton_2_cambiar():
    Frame_2.forget()
    Frame_3.pack(side="left", expand=True, fill="x")
    Frame_3.config(height=720, width=720, bg="#F08269")


def init():
    print("JODER SI ENTRO ESTA PORQUERIA")
 
    global Frame_1
    Frame_1 = Frame(root)
    global Frame_2
    Frame_2 = Frame(root)
    global Frame_3
    Frame_3 = Frame(root)
    
    Frame_1.pack(side="left", expand=True, fill="x")
    Frame_1.config(height=720, bg="#1E262C")

    Frame_2.pack(side="left", expand=True, fill="x")
    Frame_2.config(height=720, width=720, bg="#EAEEEF")

    label_1 = Label(Frame_2, text="TEXTO EN FRAME 1", font=(
        "Verdana", 12), bg="#EAEEEF", fg="black", anchor=NW)
    label_1.pack()
    label_1.place(x=200, y=0, height=35)

    label_1 = Label(Frame_3, text="TEXTO EN FRAME 2 JODER SI FUNCIONA PERRO", font=(
        "Verdana", 12), bg="#F08269", fg="black", anchor=NW)
    label_1.pack()
    label_1.place(x=200, y=0, height=35)

    button_1 = Button(Frame_1, text="Boton1", font=("Verdana", 12), bg="#1E262C", fg="white",
                      anchor=NW, command=botton_1_cambiar).place(x=0, y=0, width=300, height=35)
    button_2 = Button(Frame_1, text="Boton1", font=("Verdana", 12), bg="#1E262C", fg="white",
                      anchor=NW, command=botton_2_cambiar).place(x=0, y=34, width=300, height=35)
root = Tk()
root.title("Proyecto")
root.resizable(False, False)
root.geometry("1280x720")
root.config(bg="#EAEEEF")
Frame_1 = Frame(root)
Frame_2 = Frame(root)
Frame_3 = Frame(root)
#INICIO DE LA INTERFAZ GRAFICA

frame_login = login.Login(master=root, init=init, login_frame_validate = login_frame_validate)
#frame_registro = registro.Registro(master=root)

root.mainloop()

