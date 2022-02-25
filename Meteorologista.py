from pip import main
import requests as rq

cidade = input("Diga a sua cidade:")

desejo = input("Você deseja algo completo ou mais rapido?:")

def clima_tempo():	
	endereco_api = "http://api.openweathermap.org/data/2.5/weather?appid=9e1280f88eef9db700e867bb898fd3ec&q="
	url = endereco_api + cidade

	infos = rq.get(url).json()

	# Coord
	longitude = infos['coord']['lon']
	latitude = infos['coord']['lat']
	# main
	temp = infos['main']['temp'] - 273.15 # Kelvin para Celsius
	pressao_atm = infos['main']['pressure'] / 1013.25 #Libras para ATM
	humidade = infos['main']['humidity'] # Recebe em porcentagem
	temp_max= infos['main']['temp_max'] - 273.15 # Kelvin para Celsius
	temp_min = infos['main']['temp_min'] - 273.15 # Kelvin para Celsius

	#vento
	v_speed = infos['wind']['speed'] # km/ h
	v_direc = infos['wind']['deg'] #Recebe em graus

	#clouds / nuvens

	nebulosidade = infos['clouds']['all']

	#id
	id_da_cidade = infos['id']

	# 11
	return [longitude, latitude, 
		temp, pressao_atm, humidade, 
		temp_max, temp_min, v_speed, 
		v_direc, nebulosidade, id_da_cidade]
#TEMPO
def temperatura():
	temp_atual = clima_tempo()[2]
	temp_max = clima_tempo()[5]
	temp_min = clima_tempo()[6]
	
	return [temp_atual, temp_max, temp_min]

if 'rapido' in desejo:
	lista_tempo = temperatura()
	temp = lista_tempo[0]
	temp_max = lista_tempo[1]
	temp_min = lista_tempo[2]
	print("A temperatura de hoje é {:.2f}º. Temos uma máxima de {:.2f}º e uma minima de {:.2f}º".format(temp, temp_max, temp_min))

elif 'completo' in desejo:
	lista_infos = clima_tempo()
	longitude = lista_infos[0]
	latitude = lista_infos[1]
	temp = lista_infos[2]
	pressao_atm = lista_infos[3]
	humidade = lista_infos[4]
	temp_max = lista_infos[5]
	temp_min = lista_infos[6]
	v_speed = lista_infos[7]
	v_direc = lista_infos[8]
	nebulosidade = lista_infos[9]
	id_da_cidade = lista_infos[10]

	print("Metereologista:")
	print("Mostrando informações de {}\n\n".format(cidade))
	print("Longitude: {}, Latitude: {}\nId: {}\n".format(longitude, latitude, id_da_cidade))
	print("Temperatura: {:.2f}º".format(temp))
	print("Temperatura máxima: {:.2f}º".format(temp_max))
	print("Temperatura minima: {:.2f}º".format(temp_min))
	print("Humidade: {}".format(humidade))
	print("Nebulosidade: {}".format(nebulosidade))
	print("Velocidade do vento: {}m/s\nDireção do vento: {}".format(v_speed,v_direc))

else:
	print("Desculpe,não entendi o que você deseja, tente novamente mais tarde")