import threading
import sys
import socket
import pickle
import os

class Cliente():
    #Se inicializan las variables que serán rellenadas por el usuario
	def __init__(self, host=input("Introduzca la Ip dada por el servidor: "), port=int(input("Introduzca el puerto del servidor: ")), nombre=input("Introduzca nombre: ")):
		#Se enlistan los sockets
		self.nombre = nombre
		self.sock = socket.socket()
		self.sock.connect((str(host), int(port)))
		hilo_recv_mensaje = threading.Thread(target=self.recibir)
		#Se lanzan los hilos
		hilo_recv_mensaje.daemon = True
		hilo_recv_mensaje.start()
		#Se muestran los hilos y el pid
		print('Hilo con PID',os.getpid())
		print('Hilos activos', threading.active_count())
        #Se le dice al cliente que escriba texto
		while True:
			msg = input('\nEscriba texto ? ** Enviar = ENTER ** Abandonar Chat = Q \n')
			#Si lo que escribe el cliente no es igual a Q, se envia el mensaje al otro cliente 
			if msg != 'Q' :
				self.enviar(nombre+ ": " + msg)
			else:
			#Si lo que escribe el cliente es igual a Q, se cierra el programa	
				print("Hasta luego")
				self.sock.close()
				sys.exit()
            #Se reciben los datos y se determina el tamaño máximo de los mensajes
	def recibir(self):
		while True:
			try:
				data = self.sock.recv(32)
				if data:
					print(pickle.loads(data))
			except:
				pass
            #Se envian los mensajes
	def enviar(self, msg):
		self.sock.send(pickle.dumps(msg))

arrancar = Cliente()
