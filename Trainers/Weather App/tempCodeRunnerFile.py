import requests
import datetime
import json
import pandas as pd
import pycountry
import pytz

#colocando a API Key
chave = '1062ec08873bd859bc2bb0b4e0ee1e4e'
cidade = "Lisboa"
api_link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}'

#chamando API com request
r = requests.get(api_link)

#pegando e colocando os dados em formato de dicionário
dados = r.json()
codigo_pais = dados['sys']['country'] #pega a sigla do pais ex: BR
#fuso_horario = dados['sys']['timezone']

#usando a sigla do pais, retorna o nome: BR -> Brazil
country = pycountry.countries.get(alpha_2=codigo_pais)

if country:
    print(country.name)
else:
    print("País não encontrado!")
    
#pega o horário do país e coloca no formato UTC
horario = pytz.country_timezones[codigo_pais]

# --- Zona ---
zona = pytz.country_timezones[codigo_pais]

# --- Cidade ---
cidade = dados['name']

# --- País ---
horario = pytz.country_names[codigo_pais]

# --- Estado ---
estado = dados['name']

# --- Data e Hora ---
data = datetime.datetime.now(pytz.timezone(f"{horario}"))
print(data.strftime("%d/%m/%Y | %H:%M:%S"))

# --- Tempo ---


print(data.strftime("%d/%m/%Y | %H:%M:%S")) 

