# -*- coding: utf-8 -*-

import telebot
import urllib
import urllib2
import sys
import datetime
import random
import os
import commands
import requests
import socket
import requests

API_TOKEN = '' #Token BotFather

bot = telebot.TeleBot(API_TOKEN)

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        cid = m.chat.id # Almacenaremos el ID de la conversación.
        if m.content_type == 'text':
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
 

@bot.message_handler(commands=['start']) #Comando /start muestra lista de comandos
def send_welcome(message):
	try:
		bot.reply_to(message, 
		"""
		Hola, soy tu bot!!!, Pideme lo que quieras :D
		/hola
		envia Usuario/ID
		/clima <ciudad>
		Obtiene clima de ciudad
		/textvoz <texto>
		Convierte Texto a Voz 
		/bip <bip>
		Saldo bip
		/indi   
		Muestra Indicadores Economicos
		/santo
		Muestra Santoral
		/rut <rut>
		Informacion de servel
		/loto
		Resultados Juegos de Azar
		/aire <ciudad>
		Calidad del aire por Ciudad
		/aire lista
		Muestra ciudades disponibles
		/sismos
		Ultimos 3 sismos sobre 3
		/flickr
		Muestra 3 imagenes desde Flickr
		""")
	except Exception,e:
		print e

@bot.message_handler(commands=['temp']) # Muestra la temperatura de la RPI
def command_temp(m):
	try:
		cid = m.chat.id #Almacena el ID 
		if cid == : # Solo acepta la ejecucion para un ID(el propio)
			temp = commands.getoutput('/opt/vc/bin/vcgencmd measure_temp')
			bot.send_message(cid, temp)
		else:
			bot.send_message(cid, "No tiene acceso") # Si el ID es diferente envia este mensaje
	except Exception,e:
		print e

@bot.message_handler(commands=['uptime']) # Muestra el tiempo que lleva encendida la RPI
def uptime(m):
	try:
		cid = m.chat.id #Almacena el ID
		if cid == :# Solo acepta la ejecucion para un ID(el propio)
			uptime = commands.getoutput('uptime')
			bot.send_message(cid, uptime)
		else:
			bot.send_message(cid, "No tiene acceso") # Si el ID es diferente envia este mensaje
	except Exception,e:
		print e

@bot.message_handler(commands=['tamano']) # Muestra el tamaño disponible de la RPI
def tamano(m):
	try:
		cid = m.chat.id #Almacena el ID
		if cid == :# Solo acepta la ejecucion para un ID(el propio)
			tamano = commands.getoutput('df -h')
			bot.send_message(cid, tamano)
		else:
			bot.send_message(cid, "No tiene acceso")# Si el ID es diferente envia este mensaje
	except Exception,e:
		print e

@bot.message_handler(commands=['freqCPU'])# Muestra la frecuencia disponible de la RPI
def command_temp(m):
	try:
		cid = m.chat.id #Almacena el ID
		if cid == :# Solo acepta la ejecucion para un ID(el propio)
			freqCPU = commands.getoutput('cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq')
			bot.send_message(cid, freqCPU)
		else:
			bot.send_message(cid, "No tiene acceso")# Si el ID es diferente envia este mensaje
	except Exception,e:
		print e

@bot.message_handler(commands=['speedtest'])# realiza un test de velocidad de internet desde la RPI
def command_speedtest(m):
	try:
		cid = m.chat.id #Almacena el ID
		if cid == :# Solo acepta la ejecucion para un ID(el propio)
			speedtest = commands.getoutput('speedtest')
			bot.send_message(cid, speedtest)
		else:
			bot.send_message(cid, "No tiene acceso")# Si el ID es diferente envia este mensaje
	except Exception,e:
		print e
		
@bot.message_handler(commands=['scan']))# realiza un escaneo de equipos conectados desde la RPI
def command_scan(m):
	try:
		cid = m.chat.id #Almacena el ID
		if cid == :# Solo acepta la ejecucion para un ID(el propio)
			scan = commands.getoutput('sudo nmap -sP 192.168.1.1-254')
			bot.send_message(cid, scan)
		else:
			bot.send_message(cid, "No tiene acceso") # Si el ID es diferente envia este mensaje
	except Exception,e:
		print e

@bot.message_handler(commands=['ipdata'])# Muestra informacion publica de la ip
def ipdata(m):
	try:
		cid = m.chat.id #Almacena el ID
		if cid == :# Solo acepta la ejecucion para un ID(el propio)
			data = requests.get('http://ip-api.com/json').json()
			isp = data['isp']
			As = data['as']
			query = data['query']
			org = data['org']
			bot.send_message(cid,"Informacion de su Ip Publica: "+isp+", "+As+", "+query+", "+org)
		else:
			bot.send_message(cid,"No tienes permiso") # Si el ID es diferente envia este mensaje
	except Exception,e:
		print e


# Envia un mensaje de respuesta con tu username y tu ID
@bot.message_handler(commands=['hola'])
def hola(m):
	try:
		cid = m.chat.id
		id = m.from_user.id
		Username = m.from_user.username
		First_name = m.from_user.first_name
		bot.send_message(cid, "Hola "+Username+" Tu ID es : "+str(id))
	except Exception,e:
		print e

# Obtiene informacion del clima de una ciudad, a traves de la api de darksky https://darksky.net/dev/docs
@bot.message_handler(commands=['clima'])
def clima(m):
	try:
		cid = m.chat.id
		ciudad = str(m.text)
		ciudad = ciudad[7:]
		results = Geocoder.geocode(ciudad)
		lat = results[0].coordinates[0]
		lon = results[0].coordinates[1]
		data = requests.get('https://api.darksky.net/forecast/API/'+str(lat)+","+str(lon)+'?exclude=minutely,hourly,daily&lang=es&units=auto').json()
			
		ozono = float(data['currently']['ozone'])
		Tempe = float(data['currently']['temperature'])
		icon  = (data['currently']['icon'])
		dewpo = float(data['currently']['dewPoint'])
		hume  = float(data['currently']['humidity']*100)
		nubes = float(data['currently']['cloudCover']*100)
		resumen	= (data['currently']['summary'])
		presion = float(data['currently']['pressure'])
		viento  = float(data['currently']['windSpeed'])
		viento_ = float(data['currently']['windBearing'])
		precipitacion = float(data['currently']['precipIntensity'])
		probabilidad = float(data['currently']['precipProbability'])
		fecha = float(data['currently']['time'])
		fecha = datetime.datetime.fromtimestamp(float(fecha)).strftime("%d-%m-%Y %H:%M:%S")
		
		bot.send_message(cid,"""
		Pronostico para {}, 
		Descripcion : {}
		Ozono : {} Dobson
		Temperatura : {} *C
		Punto de Rocio : {} *C
		Humedad : {}  %
		Nubes : {} %
		Presion : {} milibar
		Velociad Viento : {} m/s, Grado : {}
		Precipitacion {} mm*3
		Probabilidad de Lluvia {} 
		Fecha {}
		""".format(ciudad,resumen,ozono,Tempe,dewpo,hume,nubes,presion,viento,viento_,precipitacion,probabilidad,fecha))
	except Exception,e:
		print e

#Convierte texto en voz usando la api de google gTTS
@bot.message_handler(commands=['textvoz'])
def textvoz(m):
	try:
		cid = m.chat.id
		texto = str(m.text)
		texto = texto[9:]
		tts = gTTS(text=texto, lang='es-es') 
		save = tts.save("test.ogg")
		bot.send_audio(cid, audio=open('test.ogg', 'rb'))
	except Exception,e:
		print e

#Obtiene informacion de saldo de la bip, con unas horas de desfase   
@bot.message_handler(commands=['bip'])
def bip(m):
	try:
		cid = m.chat.id
		bip = str(m.text)
		bip = bip[5:]
		r = requests.get('http://www.psep.cl/api/Bip.php?&numberBip='+str(bip)).json()
		estado = r['Estado de contrato']
		saldo  = r['Saldo  tarjeta']
		fecha  = r['Fecha saldo']
		bot.send_message(cid,estado + "," + saldo + ", "+ fecha)
	except Exception,e:
		print e

#Obtiene informacion de los indicadores economicos 
@bot.message_handler(commands=['indi'])
def indi(m):
	try:		
		cid = m.chat.id
		r = requests.get('http://indicadoresdeldia.cl/webservice/indicadores.json').json()
		ipc = r['indicador']['ipc']
		uf 	= r['indicador']['uf']
		imacec = r['indicador']['imacec']
		utm    = r['indicador']['utm']
		dolar = r['moneda']['dolar']
		euro = r['moneda']['euro']
		fecha = r['date']
		bot.send_message(cid,"IPC: "+ipc+"\n"+"UF: "+uf+"\n"+"IMACEC: "+imacec+"\n"+"UTM:"+utm+"\n"+"Dolar:"+dolar+"\n"+"Euro:"+euro+"\n"+fecha)
	except Exception,e:
		print e

#Obtiene informacion de personas a traves de la pagina de Servel, leyendo etiquetas html
@bot.message_handler(commands=['rut'])
def rut(m):
	try:		
		cid = m.chat.id
		servel = str(m.text)
		rut = servel[5:13]
		dv  = servel[14]
		# Host y archivo
		host = "consulta.servel.cl"
		target = "https://consulta.servel.cl/consulta"
		# cabeceras HTTP usando sintaxis NOMBRE:VALOR
		# si haces un GET, deberias modificar o eliminar la primera cabecera
		headers = {
		"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
		"Content-type": "application/x-www-form-urlencoded",
		"Cookie": "_csrf=tqFB0jNij1hY-MPZvU6Jqplz; __utma=153786282.1116644428.1475803834.1475803834.1475803834.1; __utmb=153786282.2.10.1475803834; __utmc=153786282; __utmz=153786282.1475803834.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
		"Accept": "text/html, */*; q=0.01",
		"Referer": "https://consulta.servel.cl/consulta"
		}

		# parametros POST, si solo quieres una peticion get no hacen falta
		params = urllib.urlencode({'rut': rut,'dv': dv,'_csrf':'UxrJ71Fl-OH1mOHgRK992WbXpxubJuQ45oks'})
		# conectamos con el host remoto
		conn = httplib.HTTPSConnection(host)
		# mandamos la peticion POST con los parametros y las cabeceras anteriores
		# para un get seria lo mismo pero poniendo get y sin parametros
		conn.request("POST", target, params, headers)
		# vemos que narices ha pasado en la peticion
		response = conn.getresponse()
		if response.status == 200 and response.reason == "OK":
			data = json.load(response)
			nombre = data[0]['consulta_datos_json']['nombre'].encode('utf-8')
			rut 	= str(data[0]['consulta_datos_json']['rut']) + "-"+ str(data[0]['consulta_datos_json']['dv'])
			comuna = data[0]['consulta_datos_json']['ncomuna'].encode('utf-8')
			ID 	= data[0]['consulta_datos_json']['idcomuna']
			mesa 	= data[0]['consulta_datos_json']['nmesa']
			region =  data[0]['consulta_datos_json']['noregion'].encode('utf-8')
			circuns=  data[0]['consulta_datos_json']['circuns']
			distri =  data[0]['consulta_datos_json']['iddistrito']
			local 	= data[0]['consulta_datos_json']['locvotacion'].encode('utf-8')
			sexo 	= data[0]['consulta_datos_json']['sexo']
			if sexo == 1:
				sexo = "Masculino"
			else :
				sexo = "Femenino"
			habili =  data[0]['consulta_datos_json']['habilitado']
			if habili == 0:
				habili = "Habilitado Para Votar"
			else:
				habili = "NO Habilitado Para Votar"
			tipomesa= data[0]['consulta_datos_json']['tipomesa']
			provin =  data[0]['consulta_datos_json']['nprovincia'].encode('utf-8')
			dilocal=data[0]['consulta_datos_json']['dirlocvotacion'].encode('utf-8')
			vocal 	= data[0]['consulta_datos_json']['vocal']
			if vocal != "None":
				vocal = "No eres Vocal de Mesa"
			else:
				vocal = "Eres Vocal Mesa"
			bot.send_message(cid,"Nombre = " + nombre + "\n" + "Rut = " + str(rut) + "\n" + "Comuna = " + comuna + "\n" + "Provincia = " + provin + "\n" + "Mesa = " + str(mesa) + "\n" + "Region = " + str(region) + "\n" + "Circunscripcion = " + str(circuns) + "\n" " Distrito = " + str(distri) + "\n" + "Local = " + str(local) + "\n" + "Sexo = " + str(sexo) + "\n" +" Habilitado = " + str(habili) + "\n" + "Tipo Mesa = " + str(tipomesa) + "\n" + "Provincia = " + str(provin) + "\n" + "Vocal = " + str(vocal))
	except Exception,e:
		print e

# Obtiene resultados del loto ---> EN MANTENCION
@bot.message_handler(commands=['loto'])
def loto(m):
	try :
		cid = m.chat.id
		url       = urllib2.urlopen('http://www.polla.cl/cache/dgLastResultsForGame/es/Loto/1.xml')
		contents  = url.read()
		parse=BeautifulSoup(contents , "lxml")
		fecha = parse.find("resulttime").text
		loto = parse.findAll("mainvalues")
		fecha = fecha[:10]
		Loto = loto[0].text
		Revancha = loto[1].text
		Desquite = loto[2].text
		AhoraSiqueSi = loto[4].text
		Jubilazo = loto[5].text
		bot.send_message(cid,"""
		Resultados Juegos de Azar {}
		Loto 		: {}
		revancha    : {}
		Desquite    : {}
		Ahora si que Si : {}
		Jubilazo    : {}
		""".format(fecha,Loto,Revancha,Desquite,AhoraSiqueSi,Jubilazo))
	except Exception, e:
		print e 		


# Obtiene informacion de la calidad del aire a travez de https://api.openaq.org
@bot.message_handler(commands=['aire'])
def aire(m):
	try :
		cid = m.chat.id
		ciudad = str(m.text)
		ciudad = ciudad[6:]
		if ciudad == "lista":
			archivo = open("/home/pi/Python/Bot/ciudad.txt", "r") #Archivo con lista de todas las ciudades
			contenido = archivo.read()
			archivo.close()
			bot.send_message(cid,"Lista de Ciudades \n" + contenido )
      
		ahora = time.strftime("%Y/%m/%d")
		data = requests.get('https://api.openaq.org/v1/measurements?city='+ciudad+'&parameter=pm25&parameter=pm10&parameter=so2&parameter=no2&parameter=o3&parameter=co&parameter=bc&limit=30&date_from='+str(ahora)).json()
		if len(data['results']) == 0:
			bot.send_message(cid,"No Exinten Datos Para la Ciudad Consultada")
		hora = (data['results'][0]['date']['local'][11:])
		Ciudad = data['results'][0]['city']
		Ubicacion = data['results'][0]['location']
		Latitud = data['results'][0]['coordinates']['latitude']
		Longitud = data['results'][0]['coordinates']['longitude']
		archivo = open("aire.txt", "a")
		for i in range(0,30):
			if hora == data['results'][i]['date']['local'][11:]:
				if  data['results'][i]['city'] == data['results'][i]['city'] :
					archivo.write(data['results'][i]['parameter'] + " = " + str(data['results'][i]['value'])+ "  microgramos/metro cubico"+ "\n")
					#Parametros = str(data['results'][i]['parameter']), str(data['results'][i]['value']), data['results'][i]['unit']
		archivo.close()
		archivo = open("aire.txt", "r") 
		datos = archivo.read()
		archivo.close()
		Fecha = data['results'][0]['date']['local']
		bot.send_message(cid,"Calidad del Aire = "+ Ciudad+"\n"+"Ubicacion = "+Ubicacion+"\n"+"Latitud = " + str(Latitud)+"\n" + "Longitud = "+ str(Longitud)+"\n"+"Parametros : "+"\n"+datos + "\n" + "Fecha = "+Fecha )
		os.system("rm aire.txt")
	except Exception, e:
		print e

# Muestra informacion de los ultimos sismos
@bot.message_handler(commands=['sismos'])
def sismos(m):
	try :
		cid = m.chat.id
		link     = requests.get("https://www.sismos.cl/xml_data.xml")
		data     = link.text
		html     = BeautifulSoup(data,"lxml")
		entradas = html.find_all('marker', limit=3) #Cambiar este numero para mas resultados

		for message in entradas:
			msg_attrs   = dict(message.attrs)
			fecha       = msg_attrs['name'].split(",")
			locacion    = msg_attrs['address'].encode('utf-8').strip().replace("ü","u")
			magnitud    = msg_attrs['magnitud'].encode('utf-8').strip()
			profundidad = msg_attrs['profundidad'].encode('utf-8').strip()
			latitud     = msg_attrs['lat'].encode('utf-8').strip()
			longitud    = msg_attrs['lng'].encode('utf-8').strip()

		bot.send_message(cid,"Locacion : "+ locacion + "\n" + "Magnitud : "+magnitud+ "\n"+ "Profundidad : "+profundidad + "Km\n"+ "Fecha : "+ fecha[1])
	except Exception, e:
		print e

# Descarga imagenes desde flickr
@bot.message_handler(commands=['flickr'])
def flickr(m):
	try:
		cid = m.chat.id
	
		# funcion para separar el link de la imagen
		def limpiar(contenido):
			imagen = contenido.split("background-image: url(//")
			quitar = imagen[1].split(')">')
			return quitar[0]

		def ejecutar():
			conexion  = requests.get('https://www.flickr.com/explore')
			contenido = conexion.content
			html      = BeautifulSoup(contenido,"html5lib")
			entradas  = html.find_all('div',{"class":"view photo-list-photo-view requiredToShowOnServer awake"},limit=3)

			for imagen in entradas:
				img = limpiar(str(imagen))
				filename = wget.download("http://"+img)
				a = os.system("mv "+ filename + " img.jpg")
				bot.send_photo(cid, photo=open("img.jpg", 'rb'))
				os.system("rm img.jpg")
		# ejecutar el script
		if __name__ == '__main__':
			ejecutar()
	except Exception,e:
		print e

	
bot.polling(none_stop=True)
bot.set_update_listener(listener)

while True: #Infinite loop
	
	pass
