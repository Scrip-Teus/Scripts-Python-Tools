import os
import tkinter

#API: https://openweathermap.org/api

os.environ['TCL_LIBRARY'] = r'C:\ActiveTcl\lib\tcl8.6'


import os
#from PIL import Image  # Certifique-se de que a importação seja correta
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image



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

e_pesq = Entry(Frame_Top, width=12, justify='left', font=("", 20), highlightthickness=1, relief=SOLID)
e_pesq.place(x=10, y=10) #Cria e adiciona a barra de pesquisa

b_exec = Button(Frame_Top, text="Ver clima", bg=co1, fg=co2, font=("Ivy 9 bold", 14), relief='raised', overrelief=RIDGE)
b_exec.place(x=213, y=8) #Cria e adiciona o botão de execução

#Configuração do Frame Corpo

l_local = Label(Frame_Corpo, text="Piumhi - Brazil / Minas Gerais", anchor='center', bg=fundo, fg=co1, font=("Gill Sans", 12, "bold"))
l_local.place(x=10, y=15) #Adiciona a cidade, pais e estado.

l_data = Label(Frame_Corpo, text="11/02/2025 | 14:12:00 AM", anchor='center', bg=fundo, fg=co1, font=("Gill Sans", 10, "bold"))
l_data.place(x=10, y=50) #Adiciona a data e hora.

l_humidade = Label(Frame_Corpo, text="85", anchor='center', bg=fundo, fg=co1, font=("Gill Sans", 50, "bold"))
l_humidade.place(x=10, y=105) #Adiciona a humidade do ar.

l_porcentagem = Label(Frame_Corpo, text="%", anchor='center', bg=fundo, fg=co1, font=("Gill Sans", 10, "bold"))
l_porcentagem.place(x=90, y=115) #Adiciona o simbolo de porcentagem.

l_h_nome = Label(Frame_Corpo, text="Humidade", anchor='center', bg=fundo, fg=co1, font=("Gill Sans", 10, "bold"))
l_h_nome.place(x=90, y=150) #Adiciona a palavra "humidade".

l_pressao = Label(Frame_Corpo, text="Pressão: 1013", anchor='center', bg=fundo, fg=co1, font=("Gill Sans", 10, "bold"))
l_pressao.place(x=15, y=215) #Determina o valor da pressão.

#l_p_valor = Label(Frame_Corpo, text="1013", anchor='center', bg=fundo, fg=co1, font=("Gill Sans", 8, "bold"))
#l_p_valor.place(x=68, y=215) #Determina um valor a "pressão".

l_vento = Label(Frame_Corpo, text="Velocidade do vento: 1.03", anchor='center', bg=fundo, fg=co1, font=("Gill Sans", 10, "bold"))
l_vento.place(x=15, y=245) #Determina o valor do vento.

#l_v_valor = Label(Frame_Corpo, text="1.03", anchor='center', bg=fundo, fg=co1, font=("Gill Sans", 8, "bold"))
#l_v_valor.place(x=140, y=245) #Determina um valor a "vento".

l_ceu = Label(Frame_Corpo, text="Céu um pouco nublado", anchor='center', bg=fundo, fg=co1, font=("Gill Sans", 9, "bold"))
l_ceu.place(x=168, y=190) #Mostra como está o céu naquele momento.

imagem = Image.open(r"C:\Users\matheus.souza\Documents\Scripts-Python-Tools\Trainers\Weather App\Imagens\Manhã.png")
imagem = imagem.resize((95, 95))
imagem_tk =  ImageTk.PhotoImage(imagem)

img_manha = Label(Frame_Corpo, image=imagem_tk, bg=fundo)
img_manha.place(x=190, y=90)





janela.mainloop()



