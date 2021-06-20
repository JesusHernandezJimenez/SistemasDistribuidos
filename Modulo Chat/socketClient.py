from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def iniciarSocket():
    # Sockets
    HOST = "localhost"
    PORT = 50000
    if not PORT:
        PORT = 50000
    else:
        PORT = int(PORT)

    ADDR = (HOST, PORT)

    global client_socket 
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(ADDR)

    #receive_thread = Thread(target=recibir(client_socket))
    #receive_thread.start()
    print("se ha iniciado el socket")
    return client_socket

    
def enviarUsuarioPass(entry_user_text, entr_user_password):
    if entry_user_text!= "" and entr_user_password != "":
        msg = "@" + entry_user_text + "@" + entr_user_password
        print(msg)
        client_socket.send(bytes(msg, "utf8"))

def set_name(usuario):  # El evento es pasado por binders
    # Recibir el nombre del remitente
    msg = usuario.get()
    print(msg)
    client_socket.send(bytes(msg, "utf8"))

def recibir():
    # Se maneja la recepción de mensajes
    while True:
        try:
            print("entro el ciclo whiles")
            msg = client_socket.recv(1024).decode("utf8")
            msg_split = msg.split("@")
            if len(msg_split) > 1:
                usuario = msg_split[1]
                
        except OSError:  # Posiblemente el cliente haya abandonado el chat
            print("error")   
            break
    

def send(entry_user_text, entr_user_password):
    # Se maneja el envío de mensajes
    print(entry_user_text, entr_user_password)
    if entry_user_text!= "" and entr_user_password != "":
        msg = "@" + entry_user_text + "@" + entr_user_password
        client_socket.send(bytes(msg, "utf8"))



