from tkinter import *
from PIL import ImageTk, Image

class Login(Frame):
    #Creacion del frame, recibe root=La ventada creada, delete = funcion para eliminar el frame, joder = funcion de prueba
    def __init__(self, master=None, init=None, validar_usuario=None):
        super().__init__(master)
        self.init = init
        self.master = master
        self.config(height=600, width=350, bg="#1E262C")
        self.pack(ipadx=50, ipady=10, expand=True)
        self.create_login(master, validar_usuario)
 
    def create_login(self, Frame, validar_usuario):
        entry_user_text = StringVar()
        entr_user_password = StringVar()
        Label(Frame, text="LOGIN", font=("Impact", 20), fg="white",
            bg="#1E262C").place(anchor='n', rely=0.15, relx=0.5)
        Label(Frame, text="Usuario", font=("Impact", 14), fg="white", bg="#1E262C").place(anchor='n', rely=0.30, relx=0.5)
        entry_usuario = Entry(Frame, textvariable=entry_user_text,  font=("Arial", 12), fg="black", bg="white").place(anchor='n', rely=0.35, relx=0.5)
        
        Label(Frame, text="Contraseña", font=("Impact", 14), fg="white",bg="#1E262C").place(anchor='n', rely=0.45, relx=0.5)
        entry_password = Entry(Frame, textvariable=entr_user_password,show='*', font=("Impact", 12), fg="black", bg="white").place(anchor='n', rely=0.50, relx=0.5)

        button_ingresar = Button(Frame, text="Ingresar", font=("Verdana", 12), bg="#1E262C", fg="white", anchor=NW,
                                 command=lambda:  self.login_validate(entry_user_text.get(), entr_user_password.get(), validar_usuario)).place(anchor='n', rely=0.7, relx=0.5, width=300, height=35)

    def login_validate(self, user, password, validate_frame):
        if validate_frame(user, password) == True:
            print("Validado, neta creeme")
            for widgets in self.master.winfo_children():
               widgets.destroy()
            self.init()
#Iniciar este frame
"""
root = Tk()
app=Login(master=root,delete=delete)
app.mainloop()
"""
