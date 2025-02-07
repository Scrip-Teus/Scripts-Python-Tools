import os
import tkinter

os.environ['TCL_LIBRARY'] = r'C:\ActiveTcl\lib\tcl8.6'

from tkinter import *
from tkinter import ttk

################# Cores ###################

co0 = "#444466" # Preta
co1 = "#feffff" # Branca
co2 = "#6f9fbd" # Azul

fundo_dia = "#6cc4cc" # Ciano
fundo_noite = "#484f60" # Cinza Escuro
fundo_tarde = "#bfb86d" # Amarelo "sujo"

fundo = fundo_dia

janela = Tk()
janela.title("Weather APP")
janela.geometry("320x350")
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157) # Linha horizontal do tkinter (So uma estilização)

#Frame Top (Os botões, pesquisas e etc)
#Frame Corpo (Retorna as informações pesquisadas)

Frame_Top = Frame(janela, width=320, height=55, bg=co1, pady=0, padx=0)
Frame_Top.grid(row=1, column=0)

Frame_Corpo = Frame(janela, width=320, height=295, bg=fundo, pady=0, padx=0)
Frame_Corpo.grid(row=2, column=0, sticky=NW) #NW = Escrita da esquerda para direita

estilo = ttk.Style(janela)
estilo.theme_use("clam") #Não muda muita coisa mas deixa os width's mais agradáveis visualmente.

#Configuração do Frame Top

e_pesq = Entry(Frame_Top, width=20, justify='left', font=("", 14), highlightthickness=1, relief=SOLID)
e_pesq.place(x=15, y=15) #Cria e adiciona a barra de pesquisa

#b_exec = Entry(Frame_Top, width=20, text="Ver clima", bg=fon font=("", 14), highlightthickness=1, relief=SOLID)
#b_exec.place(x=15, y=15) #Cria e adiciona o botão de execução

janela.mainloop()
