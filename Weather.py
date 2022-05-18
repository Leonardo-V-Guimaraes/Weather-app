import tkinter
from tkinter import *
from tkinter import ttk

# Importando Pillow # para manipular as imagens melhor
from PIL import Image, ImageTk

# CORES #
cor_0 = "#444466" # PRETO
cor_1 = "#FEFFFF" # BRANCO
cor_2 = "#6F9FBD" # AZUL

fundo_dia="#6CC4CC"
fundo_noite="#484F60"
fundo_tarde="#BFB86D"
fundo = fundo_dia

# JANELA #
janela = Tk()
janela.title('') # Nome janela
janela.geometry('320x350') # Tamanho
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, column=1, ipadx=157)

# CRIANDO FRAMES #

frame_top = Frame(janela, width=320, height=50, bg=cor_1, pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0)
frame_corpo.grid(row=2, column=0, sticky=NW) #sticky NW leitura da esquerda para direita

# ESTILOS #
estilo = ttk.Style(janela)
estilo.theme_use('clam') # Irá personalizar alguns widgets estilo clam

# CONFIGURANDO FRAME TOP #

e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid') # Criando a box
e_local.place(x=15, y=10) # onde a box será setada
b_ver = Button(frame_top, text="Ver clima", bg=cor_1, fg=cor_2, font=("Ivy 9 bold"), relief='raised', overrelief=RIDGE) # Criando o botão. fg = cor da letra
b_ver.place(x=250, y=10) # onde a box será setada

# CONFIGURANDO FRAME CORPO #

l_cidade = Label(frame_corpo, text="São Paulo - Brazil / South America", anchor='center', bg=fundo, fg=cor_1, font=("Arial 14"))
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text="09 03 2022 | 10:50:00 AM", anchor='center', bg=fundo, fg=cor_1, font=("Arial 9"))
l_data.place(x=10, y=54)

l_humidade = Label(frame_corpo, text="84", anchor='center', bg=fundo, fg=cor_1, font=("Arial 45"))
l_humidade.place(x=10, y=100)

l_h_simbolo = Label(frame_corpo, text="%", anchor='center', bg=fundo, fg=cor_1, font=("Arial 10 bold"))
l_h_simbolo.place(x=85, y=110)

l_h_nome = Label(frame_corpo, text="Umidade", anchor='center', bg=fundo, fg=cor_1, font=("Arial 10"))
l_h_nome.place(x=85, y=140)

l_pressao = Label(frame_corpo, text="Pressão : 1000", anchor='center', bg=fundo, fg=cor_1, font=("Arial 9"))
l_pressao.place(x=10, y=184)

l_velocidade = Label(frame_corpo, text="Velocidade do vento : 30", anchor='center', bg=fundo, fg=cor_1, font=("Arial 9"))
l_velocidade.place(x=10, y=212)


imagem = Image.open('images/Sol.png') # Abrindo a imagem
#imagem = imagem.resize(130, 130) # Ajustando tamanho
imagem = ImageTk.PhotoImage(imagem) # Para que o Tk possa abrir a imagem

l_iconSol = Label(frame_corpo, image=imagem, bg=fundo,)
l_iconSol.place(x=200, y=100)

l_descricao = Label(frame_corpo, text="Nublado", anchor='center', bg=fundo, fg=cor_1, font=("Arial 9"))
l_descricao.place(x=210, y=170)

janela.mainloop()