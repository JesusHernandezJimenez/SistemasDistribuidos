from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def aceptar_conexiones():
    # ciclo infinito para todos los posibles clientes
    while True:
        client, client_address = SERVER.accept()
        enderecos[client] = client_address 
        Thread(target=administrar_cliente, args=(client,)).start()

def administrar_cliente(client):  # Recibe el socket del cliente como argumento
    name = client.recv(1024).decode("utf8")
    client.send(bytes(name + " esta en línea", "utf8"))
    msg = "%s entró al chat" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name  # almacena el nombre del cliente en el diccionario de nombres (clientes)

    while True:
        # cliclo de comunicación infinito
        msg = client.recv(1024)  # recibir un mensaje del cliente
        # si un mensaje no contiene instrucciones de salida, simplemente se transmite el mensaje a otros clientes conectados 
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name + "")
        else:   # mensaje con instrucción de salida
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s dejo la conversación" % name, "utf8"))
            break

def broadcast(msg, prefix=""):  # El prefijo es para la identificación del nombre
   # Envía el mensaje a todos los clientes conectados, el prefijo es para identificar el remitente del mensaje
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)

clients = {}    # Diccionario de clientes
enderecos = {}  # Diccionario de direcciones

# Creando el nombre de Host (el que recibirá los pedidos del cliente)
HOST = "localhost"

# Número de puerto
PORT = 50000

# Constante que almacena la dirección y número de puerto
ADDR = (HOST, PORT)

# Creando el socket
SERVER = socket(AF_INET, SOCK_STREAM)

# Vinculando el objeto a una dirección y puerto
SERVER.bind(ADDR)

# Iniciar el servidor y aceptar solicitudes
if __name__ == "__main__":
    SERVER.listen(5)
    print("Esperando conexiones...")
    ACCEPT_THREAD = Thread(target=aceptar_conexiones)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
SERVER.close()