# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 15:46:00 2022

@author: DELL
"""

from tkinter import*
import random
root = Tk()
root.title("Color randomized game")
root.geometry("500x500")

label=Label(root, text="")
label.place(relx=0.5, rely=0.5, anchor=CENTER)

class game:
    def __init__(self):
        self.__score=0
    def update_game(self):
        self.text=["BLACK","PINK","GREEN","YELLOW","RED"]
        self.color=["black","pink","green","yellow","red"]
        self.random_text=random.randint(0,4)
        self.random_color=random.randint(0,4)
        label["text"]=self.text[self.random_text]
        label["fg"]=self.color[self.random_color]

obj=game()
btn1=Button(root, text="START", command=obj.update_game)
btn1.place(relx=0.6, rely=0.6, anchor=CENTER)
root.mainloop()