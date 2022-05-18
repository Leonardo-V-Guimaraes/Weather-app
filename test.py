import requests
from datetime import datetime
import json
import pytz

chave = ''
cidade = 'São Paulo'
api_link = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade,chave)

# Fazendo chamada da API usando request
r = requests.get(api_link)

# Convertendo os dados presentes na variavel r em dicionario
dados = r.json()
print(dados)
# Obtando zona, pais e hora
pais_codigo = dados['sys']['country'] # acessando a biblioteca 
print(pais_codigo)

# ----- Zona -----
zona_fuso = pytz.country_timezones[pais_codigo]
print(zona_fuso)
# -----Pais -----
pais = pytz.country_names[pais_codigo]

# ----- data -----
zona_time = pytz.timezone(zona_fuso[0]) # Pegando o primeiro valor do zona_fuso
print(zona_time)

zona_horas = datetime.now(zona_time)
zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S:%p") # Formatando o dia/mes/ano e horario com periodo
print(zona_horas)

# ----- tempo -----
tempo = dados['main']['temp']