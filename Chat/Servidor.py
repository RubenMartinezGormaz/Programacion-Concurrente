import socket
import threading
import sys
import pickle
import os

class Servidor():
 #Se inicializan las variables que serán rellenadas por el usuario
	def __init__(self, host=socket.gethostname(), port=int(input("Introduce un puerto: "))):
		self.clientes = []
		#Se dice la ip del servidor mediante el gethostname y el puerto que es el que escribió el usuario antes
		print("\n Su IP es: ",socket.gethostbyname(host))
		print("\n Su puerto es: ", port)
		#Se enlistan los sockets
		self.sock = socket.socket()
		self.sock.bind((str(host), int(port)))
		self.sock.listen(20)
		self.sock.setblocking(False)
        #Hilos
		aceptar = threading.Thread(target=self.aceptarC)
		procesar = threading.Thread(target=self.procesarC)
        #Se lanzan los hilos
		aceptar.daemon = True
		aceptar.start()

		procesar.daemon = True
		procesar.start()
        #Se escribe siempre la opción de salir y el usuario puede responder
		while True:
			msg = input("SALIR = Q\n")
		#Si la respuesta es Q, se sale del programa con un mensaje	
			if msg == 'Q':
				print("Adioos")
				self.sock.close()
				sys.exit()
			else:
				pass
        #Se activa el broadcast para los clientes
	def broadcast(self, msg, cliente):
		for c in self.clientes:
			try:
				if c != cliente:
					c.send(msg)
                    
			except:
				self.clientes.remove(c)
        #Se acepta la conexión con el cliente
	def aceptarC(self):
		while True:
			try:
				conn, addr = self.sock.accept()
				print(f"\nConexion aceptada via {conn}\n")
				conn.setblocking(False)
				self.clientes.append(conn)
			except:
				pass
        #Se procesan los mesajes y se determina el tamaño máximo de los mensajes
	def procesarC(self):
		print("Procesamiento de mensajes iniciado")
		while True:
			if len(self.clientes) > 0:
				for c in self.clientes:
					try:
						data = c.recv(32)
						if data:
                            #Se crea un .txt y se escriben los mensajes en su interior y luego se cierra
							f = open("u22037408.txt", "a")
							f.write(pickle.loads(data) + "\n")
							f.close()
							self.broadcast(data,c)
					except:
						pass

                    

    
arrancar = Servidor()