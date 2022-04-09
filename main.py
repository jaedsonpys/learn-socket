import socket

# definindo o host (IP) e a porta onde o 
# socket irá se conectar ou aguardar conexões.
address = ('127.0.0.1', 5500)

# na função socket.socket(), passamos dois argumentos,
# o primeiro é o tipo do socket, que definimos como AF_INET
# (ou seja, IPv4), o segundo é o protocolo utilizado, usamos
# o SOCK_STREAM (o protocolo TCP, que é utilizado pelo HTTP).
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# agora, passamos o endereço que será aberto ao
# socket.
sock.bind(address)

# e por último, colocamos o servidor em modo
# de escuta, definindo o número o limite de requisições
# de conexão.
sock.listen(5)

print('\033[32mServer ON\033[m')
print(f'Access http://{address[0]}:{address[1]}')

# o servidor já está pronto, agora, devemos
# aceitar as conexões vindas de um cliente.

# para aceitar a conexão de vários clientes,
# usaremos o loop while até que o servidor seja
# interrompido.
try:
    while True:
        # o método sock.accept() ficará aguardando conexões,
        # e quando for recebida, ele retorna o socket do cliente
        # e o endereço dele (ip e porta).
        client_socket, client_addr = sock.accept()
        host, port = client_addr

        # para obter a mensagem que foi enviada
        # pelo cliente, utilize o método
        # client_socket.recv(), definindo o
        # tamanho do buffer:
        client_message = client_socket.recv(1024)

        print('New client:')
        print(f'\tHost: {host}')
        print(f'\tPort: {port}')
        print(f'Message: \n{client_message.decode().strip()}\n')

        # enviando messagem ao cliente (precisa ser codificada em bytes):
        client_socket.send(b'HTTP/1.1 200 OK\n\nHello World!!')

        # e para fechar a conexão com o cliente:
        client_socket.close()
except KeyboardInterrupt:
    # fechando um socket
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
