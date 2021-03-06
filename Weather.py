import tkinter
from tkinter import *
from tkinter import ttk

# Importando Pillow # para manipular as imagens melhor 
from PIL import Image, ImageTk

# Importações #

import requests
from datetime import datetime
import json
import pytz
import pycountry_convert as pc
import math

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
janela.title('Tempo') # Nome janela
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

global imagem
# Função que retorna as informações #
def informacao():
    
    chave = 'c6c03a00472836edcad6d26ff591d515'
    cidade = e_local.get() # agora pega o valor de entrada para pesquisa da cidade
    api_link = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade,chave)

    # Fazendo chamada da API usando request
    r = requests.get(api_link)

    # Convertendo os dados presentes na variavel r em dicionario
    dados = r.json()

    print(dados)

    # Obtando zona, pais e hora
    pais_codigo = dados['sys']['country'] # acessando a biblioteca 

    # ----- Zona -----
    zona_fuso = pytz.country_timezones[pais_codigo]

    # -----Pais -----
    pais = pytz.country_names[pais_codigo]

    # ----- data -----
    zona_time = pytz.timezone(zona_fuso[0]) # Pegando o primeiro valor do zona_fuso
    print(zona_fuso)

    zona_horas = datetime.now(zona_time)
    zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S:%p") # Formatando o dia/mes/ano e horario com periodo


    # ----- tempo -----
    tempo = dados['main']['temp']
    # convertendo de kelvin para celsius
    Kelvin = 273.15
    tempo = tempo - Kelvin

    tempo = round(tempo)
    pressao = dados['main']['pressure']
    umidade = dados['main']['humidity']
    velocidade = dados['wind']['speed']
    descricao = dados['weather'][0]['description'] # 'weather': [{indice>0>description}]

    # mudando informações

    def pais_para_continente(i):
        pais_alpha = pc.country_name_to_country_alpha2(i)
        pais_continent_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
        pais_continent_nome = pc.convert_continent_code_to_continent_name(pais_continent_codigo)

        return pais_continent_nome

    continente = pais_para_continente(pais)

    # Passando informações nas labels

    l_cidade['text'] = cidade.title() + " - " + pais + " / " + continente # alterando o valor da l_cidade text imprimindo esses valores concatenados
    l_data['text'] = zona_horas
    l_tempo['text'] = tempo
    l_tempo_simb['text'] = "°C"
    l_pressao['text'] = " Pressão : " + str(pressao)
    l_velocidade['text'] = " Velocidade do Vento: " + str(velocidade)
    l_umidade['text'] = umidade
    l_h_simbolo['text'] = "%"
    l_h_nome['text'] = "Umidade"
    if descricao == "clear sky":
        descricao = "Céu claro"
    elif descricao == "overcast clouds":
        descricao = "Nublado"
    elif descricao == "light rain":
        descricao = "Chuva leve"
    elif descricao == "scattered clouds":
        descricao = "Nuvens dispersas"
    elif descricao == "few clouds":
        descricao == "Poucas nuvens"

    l_descricao['text'] = descricao

    # Logica para trocar fundo

    zona_periodo = datetime.now(zona_time)
    zona_periodo = zona_periodo.strftime("%H")

    global imagem

    zona_periodo = int(zona_periodo)

    if zona_periodo <= 5: # Ajustando o horario
        imagem = Image.open('images/Lua.png') # Abrindo a imagem
        fundo = fundo_noite
    elif zona_periodo <= 11:
        imagem = Image.open('images/Sol.png') # Abrindo a imagem
        fundo = fundo_dia
    elif zona_periodo <= 22:
        imagem = Image.open('images/Lua.png') # Abrindo a imagem
        fundo = fundo_noite
    else:
        pass
    

    #imagem = imagem.resize(130, 130) # Ajustando tamanho
    imagem = ImageTk.PhotoImage(imagem) # Para que o Tk possa abrir a imagem

    l_icon = Label(frame_corpo, image=imagem, bg=fundo,)
    l_icon.place(x=200, y=100)

        # Passando informações nas labels

    janela.configure(bg=fundo)
    frame_top.configure(bg=fundo)
    frame_corpo.configure(bg=fundo)

    l_cidade['bg'] = fundo
    l_data['bg'] = fundo
    l_tempo['bg'] = fundo
    l_tempo_simb['bg'] = fundo
    l_pressao['bg'] = fundo 
    l_velocidade['bg'] = fundo
    l_umidade['bg'] = fundo 
    l_h_simbolo['bg'] = fundo
    l_h_nome['bg'] = fundo
    l_descricao['bg'] = fundo


# CONFIGURANDO FRAME Top #

e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid') # Criando a box
e_local.place(x=15, y=10) # onde a box será setada
b_ver = Button(frame_top,command=informacao, text="Ver clima", bg=cor_1, fg=cor_2, font=("Ivy 9 bold"), relief='raised', overrelief=RIDGE) # Criando o botão. fg = cor da letra
b_ver.place(x=250, y=10) # onde a box será setada

# CONFIGURANDO FRAME CORPO #

l_cidade = Label(frame_corpo, text="", anchor='center', bg=fundo, fg=cor_1, font=("Arial 14"))
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text="", anchor='center', bg=fundo, fg=cor_1, font=("Arial 9"))
l_data.place(x=10, y=54)

# modificação de lugar para colocada da temperatura no lugar da umidade
# l_tempo = Label(frame_corpo, text="", anchor='center', bg=fundo, fg=cor_1, font=("Arial 9"))
# l_tempo.place(x=210, y=54)

l_tempo = Label(frame_corpo, text="", anchor='center', bg=fundo, fg=cor_1, font=("Arial 45"))
l_tempo.place(x=10, y=82)

# Simbolo de °C
l_tempo_simb = Label(frame_corpo, text="", anchor='center', bg=fundo, fg=cor_1, font=("Arial 18"))
l_tempo_simb.place(x=85, y=90)

l_umidade = Label(frame_corpo, text="", anchor='center', bg=fundo, fg=cor_1, font=("Arial 9"))
l_umidade.place(x=70, y=169)

# umidade agora em apenas uma linha
# l_umidade = Label(frame_corpo, text="", anchor='center', bg=fundo, fg=cor_1, font=("Arial 45"))
# l_umidade.place(x=10, y=100)

l_h_simbolo = Label(frame_corpo, text="", anchor='center', bg=fundo, fg=cor_1, font=("Arial 10 bold"))
l_h_simbolo.place(x=90, y=169)

l_h_nome = Label(frame_corpo, text="", anchor='center', bg=fundo, fg=cor_1, font=("Arial 10"))
l_h_nome.place(x=10, y=169)

l_pressao = Label(frame_corpo, text="", anchor='center', bg=fundo, fg=cor_1, font=("Arial 9"))
l_pressao.place(x=8, y=197)

l_velocidade = Label(frame_corpo, text="", anchor='center', bg=fundo, fg=cor_1, font=("Arial 9"))
l_velocidade.place(x=8, y=225)

l_descricao = Label(frame_corpo, text="", anchor='center', bg=fundo, fg=cor_1, font=("Arial 9"))
l_descricao.place(x=210, y=170)

janela.mainloop()