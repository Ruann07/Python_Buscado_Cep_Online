import pycep_correios
import socket
import time, os

sites_testes = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']

def Busca_cep():
    while True:
        cCep = input('Informe o seu CEP: ')
        try:
            endereco = pycep_correios.consultar_cep(cCep)
            print('UF: ' + endereco['uf'] )
            print('Cidade: ' + endereco['cidade'] )
            print('Bairro: ' + endereco['bairro'] )
            print('Endereço: ' + endereco['end'] )
            break
        except:
            print('Cep Invalido')

def testa_conexao():
    global sites_testes
    for host in sites_testes:
        a = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        a.settimeout(.5)
        try:
            b = a.connect_ex((host, 80))
            if b == 0:
                return True
        except:
            a.close()
            return False
    
bNet = testa_conexao()
if bNet:
    while True:
        Busca_cep()
        time.sleep(3.2)
        os.system('clear')
        Res = input('Deseja repetir a operação ? (S)SIM ou (N)NÃO: ')
        Res = Res.upper()
        if Res == 'N' or Res == 'NAO' or Res == 'NÃO':
            os.system('clear')
            break
        else:
            os.system('clear')
else:
    print('Você esta sem aceso a internet')
    print('Tente Novamento mais tarte')

