import socket

ip = input("IP do servidor: ")
porta = int(input("Porta: "))

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((ip, porta))
servidor.listen(1)

print("Aguardando cliente...")

conexao, endereco = servidor.accept()
print("Conectado com:", endereco)

while True:
    mensagem = conexao.recv(1024).decode()

    if mensagem.lower() == "tchau":
        print("Cliente encerrou a conexão.")
        break

    print("Cliente:", mensagem)

    resposta = input("Servidor: ")
    conexao.send(resposta.encode())

conexao.close()
servidor.close()

print("Servidor encerrado.")