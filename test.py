import requests
from datetime import datetime
import json
import pytz
import pycountry_convert as pc

chave = 'c6c03a00472836edcad6d26ff591d515'
cidade = 'São Paulo'
api_link = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade,chave)

# Fazendo chamada da API usando request
r = requests.get(api_link)

# Convertendo os dados presentes na variavel r em dicionario
dados = r.json()

# Obtando zona, pais e hora
pais_codigo = dados['sys']['country'] # acessando a biblioteca 

# ----- Zona -----
zona_fuso = pytz.country_timezones[pais_codigo]

# -----Pais -----
pais = pytz.country_names[pais_codigo]

# ----- data -----
zona_time = pytz.timezone(zona_fuso[0]) # Pegando o primeiro valor do zona_fuso

zona_horas = datetime.now(zona_time)
zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S:%p") # Formatando o dia/mes/ano e horario com periodo


# ----- tempo -----
tempo = dados['main']['temp'] 
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

