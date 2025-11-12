# UNIVERSIDADE FEDERAL DO PARANÁ
# TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
# DISCIPLINA REDES DE COMPUTADORES (DS020)
# AUTOR: PROF. CLAUSIUS DUQUE REIS
#
# SCRIPT: Servidor de sockets TCP modificado para receber texto do cliente e enviar com "Boa noite" na frente (python 3)
#

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  print ('Conexao estabelecida com cliente %s' % (addr,))

  while True:
    sentence = connectionSocket.recv(1024) # recebe dados do cliente
    if not sentence:
      break
    sentence = sentence.decode('utf-8')

    # verifica se o cliente enviou "sair"
    if sentence.lower() == 'sair':
      print ('Cliente %s enviou "sair". Encerrando conexao...' % (addr,))
      break

    modifiedSentence = 'Boa noite ' + sentence # adiciona "Boa noite" na frente
    print ('Cliente %s enviou: %s, respondendo com: %s' % (addr, sentence, modifiedSentence))
    connectionSocket.send(modifiedSentence.encode('utf-8')) # envia para o cliente o texto transformado

  connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor
