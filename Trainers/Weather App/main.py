import tkinter
from tkinter import *
from tkinter import ttk

################# Cores ###################

co0 = "#444466" # Preta
co1 = "#feffff" # Branca
co2 = "#6f9fbd" # Azul

fundo_dia = "6cc4cc" # Ciano
fundo_noite = "#484f60" # Cinza Escuro
fundo_tarde = "bfb86d" # Amarelo "sujo"

fundo = fundo_dia

janela = Tk()
janela.title("Weather APP")
janela.geometry("320x350")
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columspan=1, ipadx=157) # Linha horizontal do tkinter

janela.mainloop()