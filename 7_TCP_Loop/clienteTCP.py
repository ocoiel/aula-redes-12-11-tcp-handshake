# UNIVERSIDADE FEDERAL DO PARANÁ
# TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
# DISCIPLINA REDES DE COMPUTADORES (DS020)
# AUTOR: PROF. CLAUSIUS DUQUE REIS
#
# SCRIPT: Cliente de sockets TCP modificado para enviar mensagens infinitas ao servidor até digitar "sair" (python 3)
#

# importacao das bibliotecas
from socket import *

# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 61000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

print('Conectado ao servidor. Digite "sair" para encerrar.')
while True:
  sentence = input('Digite o texto: ')
  clientSocket.send(sentence.encode('utf-8')) # envia o texto para o servidor

  # verifica se o usuario digitou "sair"
  if sentence.lower() == 'sair':
    print('Tchau...')
    break

  modifiedSentence = clientSocket.recv(1024) # recebe do servidor a resposta
  print ('O servidor respondeu com: %s' % (modifiedSentence.decode('utf-8')))

clientSocket.close() # encerramento o socket do cliente
