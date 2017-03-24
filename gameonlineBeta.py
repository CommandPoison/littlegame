#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------
#This game has been created by: CommandPoison
#Please dont removed any 
#Respect the work
#--------------------------------------------------
#The available language of this game is Spanish

import sys
import os
import random
import socket



def servidor():
	#Ponemos la ip del ordenador o del servidor
	ip = raw_input(">>") 
	# creamos el socket
	serversocket    =   socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# usamos esta funcion para mantener en eschucha el puerto que queramos este caso 8000
	serversocket.bind((ip, 8000))
	# mantenemos en escucha el servidor
	serversocket.listen(1)
	# aceptamos la conexion
	print "Esperando conexion"
	clientsocket, clientaddress = serversocket.accept()
	J2Nombre = clientsocket.recv(1024)
	print 'Conexion de: ', J2Nombre # escribimos la ip del cliente
	print "Ip:", clientaddress
	J1Nombre = raw_input("Escriba su nombre de jugador: ")
	clientsocket.send(J1Nombre)
	# mientras estamos conectados hace lo que este dentro del bucle
	print "El J2 esta eliguiendo La raza"
	print "--------------------------------------"
	print "Espere Por favor"
	print "--------------------------------------"
	elegirRaza1 = clientsocket.recv(1024)

 	if elegirRaza1=="1":
 		os.system("clear")
 		Raza1 = "Elfos"
 		Fuerza1 = 30
 		Vida1 = 25
 		
 	if elegirRaza1=="2":
 		os.system("clear")
 		Raza1 = "Elfos de sangre"
 		Fuerza1 = 45
 		Vida1 = 25

 	if elegirRaza1=="3":
 		os.system("clear")
 		Raza1 = "Elfos nocturnos"
 		Fuerza1 = 25
 		Vida1 = 30
 			
 	if elegirRaza1=="4":
 		os.system("clear")
 		Raza1 = "Enanos"
 		Fuerza1 = 30
 		Vida1 = 32

	if elegirRaza1=="5":
 		os.system("clear")
 		Raza1 = "Humanos"
 		Fuerza1 = 30
 		Vida1 = 28

 	if elegirRaza1=="6":
 		os.system("clear")
 		Raza1 = "Trolls"
 		Fuerza1 = 30
 		Vida1 = 40

 	if elegirRaza1=="7":
 		os.system("clear")
 		Raza1 = "Ogros"
 		Fuerza1 = 23
 		Vida1 = 45	

 	if elegirRaza1=="8":
 		os.system("clear")
 		Raza1 = "No-Muertos"
 		Fuerza1 = 48
 		Vida1 = 22

 	if elegirRaza1=="9":
 		os.system("clear")
 		Raza1 = "Tauros"
 		Fuerza1 = 29
 		Vida1 = 46

	if elegirRaza1=="10":
 		os.system("clear")
 		Raza1 = "Wargen"
 		Fuerza1 = 29
 		Vida1 = 38	

 	if elegirRaza1=="11":
 		os.system("clear")
 		Raza1 = "Pandaren"
 		Fuerza1 = 30
 		Vida1 = 37
	print """	
	 ----------------------------------------------------------
	------------------------------------------------------------
	--                                                        --
	-- La batalla a llegado, Con que RAZA desea vivir o morir --
	-- ------------------------------------------------------ --
	--                                                        --
	-- 1. Elfos                                               --
 	-- 2. Elfos de sangre                                     --
 	-- 3. Elfos nocturnos                                     --
 	-- 4. Enanos                                              --
 	-- 5. Humanos                                             --
 	-- 6. Trolls                                              --
 	-- 7. Ogros                                               --
 	-- 8. No-Muertos                                          --
 	-- 9. Tauros                                              --
 	-- 10. Wargen                                             --
 	-- 11. Pandaren                                           --
 	------------------------------------------------------------
 	 ----------------------------------------------------------
 	 """
 	elegirRaza2 = raw_input("Escoje tu RAZA>> ")

 	if elegirRaza2=="1":
 		os.system("clear")
 		Raza2 = "Elfos"
 		Fuerza2 = 30
 		Vida2 = 25
 		
 	if elegirRaza2=="2":
 		os.system("clear")
 		Raza2 = "Elfos de sangre"
 		Fuerza2 = 45
 		Vida2 = 25
 	
 	if elegirRaza2=="3":
 		os.system("clear")
 		Raza2 = "Elfos nocturnos"
 		Fuerza2 = 35
 		Vida2 = 30

 	if elegirRaza2=="4":
 		os.system("clear")
 		Raza2 = "Enanos"
 		Fuerza2 = 30
 		Vida2 = 32

 	if elegirRaza2=="5":
 		os.system("clear")
 		Raza2 = "Humanos"
 		Fuerza2 = 30
 		Vida2 = 28
 		
 	if elegirRaza2=="6":
 		os.system("clear")
 		Raza2 = "Trolls"
 		Fuerza2 = 42
 		Vida2 = 40
 		
 	if elegirRaza2=="7":
 		os.system("clear")
 		Raza2 = "Ogros"
 		Fuerza2 = 23
 		Vida2 = 45

	if elegirRaza2=="8":
 		os.system("clear")
 		Raza2 = "No-Muertos"
 		Fuerza2 = 48
 		Vida2 = 22

 	if elegirRaza2=="9":
 		os.system("clear")
 		Raza2 = "Tauros"
 		Fuerza2 = 29
 		Vida2 = 46

 	if elegirRaza2=="10":
 		os.system("clear")
 		Raza2 = "Wargen"
 		Fuerza2 = 29
 		Vida2 = 38

 	if elegirRaza2=="11":
 		os.system("clear")
 		Raza2 = "Pandaren"
 		Fuerza2 = 30
 		Vida2 = 37
	clientsocket.send(elegirRaza2)
	numeroaleatorio = random.randrange(2)
	if numeroaleatorio==0:
		numerorandom = "0"
		clientsocket.send(numerorandom)
		print "----------------------------------------------"
		print "Empieza J1"
		print "----------------------------------------------"
		print Raza1
		print "vs"
		print Raza2		
		for batalla1 in range(5):
			Vida1 = Vida1 - Fuerza2
			seguir2 = raw_input(">>")			
			if Vida1<=0:
				os.system("clear")
				print "WIN J1"
				print Vida2
				sys.exit()
			print "-------------------------------------------------"
			print "Vida del J2:", Vida1
			print "-------------------------------------------------" 
			seguir2 = raw_input("Seguir>>")			
			Vida2 = Vida2 - Fuerza1
			print "-------------------------------------------------"
			print "Vida del J1:", Vida2
			print "-------------------------------------------------"
			seguir2 = raw_input("Seguir>>")			
			if Vida2<=0:
				os.system("clear")
				print "WINJ2"
				print Vida1
				sys.exit()
	if numeroaleatorio==1:
		numerorandom = "1"	
		clientsocket.send(numerorandom)
		print "----------------------------------------------"
		print "Empieza J2"
		print "----------------------------------------------"
		print Raza1
		print "vs"
		print Raza2
		for batalla1 in range(5):
			Vida2 = Vida2 - Fuerza1
			seguir2 = raw_input(">>")
			if Vida2<=0:
				os.system("clear")
				print "WIN J2"
				print Vida1
				sys.exit()
			print "-------------------------------------------------"
			print "Vida del J1:", Vida2
			print "-------------------------------------------------" 
			seguir2 = raw_input("Seguir>>")			
			Vida1 = Vida1 - Fuerza2
			seguir2 = raw_input("Seguir>>")			
			if Vida1<=0:
				os.system("clear")
				print "WINJ1"
				print Vida2
				sys.exit()
			print "-------------------------------------------------"
			print "Vida del J2:", Vida1
			print "-------------------------------------------------"	
		
			

	
def cliente():
	#Ponemos la ip del servidor
	ip = raw_input("Escribe la ip a la que conectarte>>")
 
	# creamos el socket
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# ahora acemos que se conecte con el servidor
	clientsocket.connect((ip,8000))
	# este bucle hace que mientras este conectado  haga lo que pone en el interior
	print "CONECTADO"
	J2Nombre = raw_input("Escribe Tu nombre de Jugador: ")
	clientsocket.send(J2Nombre)	
	J1Nombre = clientsocket.recv(1024)
	print "Jugando contra:", J1Nombre
	#-------------------------------------------------------------
	print """
	  ----------------------------------------------------------
	 ------------------------------------------------------------
	 --                                                        --
	 -- La batalla a llegado, Con que RAZA desea vivir o morir --
	 -- ------------------------------------------------------ --
	 --                                                        --
	 -- 1. Elfos                                               --
 	 -- 2. Elfos de sangre                                     --
 	 -- 3. Elfos nocturnos                                     --
 	 -- 4. Enanos                                              --
 	 -- 5. Humanos                                             --
 	 -- 6. Trolls                                              --
 	 -- 7. Ogros                                               --
 	 -- 8. No-Muertos                                          --
 	 -- 9. Tauros                                              --
 	 -- 10. Wargen                                             --
 	 -- 11. Pandaren                                           --
 	 ------------------------------------------------------------
 	  ----------------------------------------------------------
 	  """
 	elegirRaza1 = raw_input("Escoje tu RAZA>> ")

 	if elegirRaza1=="1":
 		os.system("clear")
 		Raza1 = "Elfos"
 		Fuerza1 = 30
 		Vida1 = 25
 		
 	if elegirRaza1=="2":
 		os.system("clear")
 		Raza1 = "Elfos de sangre"
 		Fuerza1 = 45
 		Vida1 = 25

 	if elegirRaza1=="3":
 		os.system("clear")
 		Raza1 = "Elfos nocturnos"
 		Fuerza1 = 25
 		Vida1 = 30
 			
 	if elegirRaza1=="4":
 		os.system("clear")
 		Raza1 = "Enanos"
 		Fuerza1 = 30
 		Vida1 = 32

	if elegirRaza1=="5":
 		os.system("clear")
 		Raza1 = "Humanos"
 		Fuerza1 = 30
 		Vida1 = 28

 	if elegirRaza1=="6":
 		os.system("clear")
 		Raza1 = "Trolls"
 		Fuerza1 = 30
 		Vida1 = 40

 	if elegirRaza1=="7":
 		os.system("clear")
 		Raza1 = "Ogros"
 		Fuerza1 = 23
 		Vida1 = 45	

 	if elegirRaza1=="8":
 		os.system("clear")
 		Raza1 = "No-Muertos"
 		Fuerza1 = 48
 		Vida1 = 22

 	if elegirRaza1=="9":
 		os.system("clear")
 		Raza1 = "Tauros"
 		Fuerza1 = 29
 		Vida1 = 46

	if elegirRaza1=="10":
 		os.system("clear")
 		Raza1 = "Wargen"
 		Fuerza1 = 29
 		Vida1 = 38	

 	if elegirRaza1=="11":
 		os.system("clear")
 		Raza1 = "Pandaren"
 		Fuerza1 = 30
 		Vida1 = 37	
	 
	clientsocket.send(elegirRaza1)
	print "El J1 esta eliguiendo La raza"
	print "--------------------------------------"
	print "Espere Por favor"
	print "--------------------------------------"
	elegirRaza2 = clientsocket.recv(1024)

 	if elegirRaza2=="1":
 		os.system("clear")
 		Raza2 = "Elfos"
 		Fuerza2 = 30
 		Vida2 = 25
 		
 	if elegirRaza2=="2":
 		os.system("clear")
 		Raza2 = "Elfos de sangre"
 		Fuerza2 = 45
 		Vida2 = 25
 	
 	if elegirRaza2=="3":
 		os.system("clear")
 		Raza2 = "Elfos nocturnos"
 		Fuerza2 = 35
 		Vida2 = 30

 	if elegirRaza2=="4":
 		os.system("clear")
 		Raza2 = "Enanos"
 		Fuerza2 = 30
 		Vida2 = 32

 	if elegirRaza2=="5":
 		os.system("clear")
 		Raza2 = "Humanos"
 		Fuerza2 = 30
 		Vida2 = 28
 		
 	if elegirRaza2=="6":
 		os.system("clear")
 		Raza2 = "Trolls"
 		Fuerza2 = 42
 		Vida2 = 40
 		
 	if elegirRaza2=="7":
 		os.system("clear")
 		Raza2 = "Ogros"
 		Fuerza2 = 23
 		Vida2 = 45

	if elegirRaza2=="8":
 		os.system("clear")
 		Raza2 = "No-Muertos"
 		Fuerza2 = 48
 		Vida2 = 22

 	if elegirRaza2=="9":
 		os.system("clear")
 		Raza2 = "Tauros"
 		Fuerza2 = 29
 		Vida2 = 46

 	if elegirRaza2=="10":
 		os.system("clear")
 		Raza2 = "Wargen"
 		Fuerza2 = 29
 		Vida2 = 38

 	if elegirRaza2=="11":
 		os.system("clear")
 		Raza2 = "Pandaren"
 		Fuerza2 = 30
 		Vida2 = 37
	numerorandom = clientsocket.recv(1024)	
	if numerorandom=="0":
		print "----------------------------------------------"
		print "Empieza J1"
		print "----------------------------------------------"
		print Raza1
		print "vs"
		print Raza2
		seguir2 = raw_input("Seguir>>")
		for batalla1 in range(5):
			Vida1 = Vida1 - Fuerza2
			if Vida1<=0:
				os.system("clear")
				print "WIN J1"
				print Vida2
				sys.exit()
			print "-------------------------------------------------"
			print "Vida del J2:", Vida1
			print "-------------------------------------------------" 
			seguir2 = raw_input("Seguir>>")			
			Vida2 = Vida2 - Fuerza1
			if Vida2<=0:
				os.system("clear")
				print "WINJ2"
				print Vida1
				sys.exit()
			print "-------------------------------------------------"
			print "Vida del J1:", Vida2
			print "-------------------------------------------------"
			seguir2 = raw_input("Seguir>>")	

	if numerorandom=="1":
		print "----------------------------------------------"
		print "Empieza J2"
		print "----------------------------------------------"
		print Raza1
		print "vs"
		print Raza2
		seguir2 = raw_input("Seguir>>")
		Vida2 = Vida2 - Fuerza1
		if Vida2<=0:
			os.system("clear")
			print "WIN J2"
			print Vida1
			sys.exit()
		print "-------------------------------------------------"
		print "Vida del J1:", Vida2
		print "-------------------------------------------------" 
		seguir2 = raw_input("Seguir>>")		
		Vida1 = Vida1 - Fuerza2
		if Vida1<=0:
			os.system("clear")
			print "WINJ1"
			print Vida2
			sys.exit()	
		print "-------------------------------------------------"
		print "Vida del J2:", Vida1
		print "-------------------------------------------------"
		seguir2 = raw_input("Seguir>>")			
		
def menu():
	print """
          --------------------------------------------
	 ----------------------------------------------
	 --                                          --
         -- 1. Servidor                              --
	 -- 2. Cliente                               --
	 -- 3. Exit                                  --
	 --                                          --
         ----------------------------------------------
          --------------------------------------------
         """
	accion1 = raw_input("Elige una opcion:  ")
	if accion1=="1":
		os.system("clear")	
		servidor()
	elif accion1=="2":
		os.system("clear")		
		cliente()
	elif accion1=="3":
		os.system("clear")
		sys.exit()	
	else:
		menu()

#-------------------------------------------------------------------------
menu()      
