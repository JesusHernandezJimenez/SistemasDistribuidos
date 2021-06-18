from tkinter import *

root = Tk()
root.title("Prueha")
root.geometry("400x400")


panel_1 = PanedWindow(bd=4, relief='flat', bg='red')
panel_1.pack(fill=BOTH, expand=1)


panel_2 =  PanedWindow(panel_1, orient=HORIZONTAL, bd=4, relief='raised', bg='black')
panel_1.add(panel_2)

top = Label(panel_2, text='top panel')
panel_2.add(top)

root.mainloop()