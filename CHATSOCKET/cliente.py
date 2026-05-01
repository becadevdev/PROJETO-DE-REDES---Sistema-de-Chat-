import socket
 
ip = input("IP do servidor: ")
porta = int(input("Porta: "))

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ip, porta))

print("Conectado ao servidor!")

while True:
    mensagem = input("Você: ")
    cliente.send(mensagem.encode())

    if mensagem.lower() == "tchau":
        print("Conexão encerrada.")
        break

    resposta = cliente.recv(1024).decode()
    print("Servidor:", resposta)

cliente.close()