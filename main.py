#cia = '\033[1;36m'
cl = '\033[0m'
az = '\033[1;94m'
cia = '\033[1;36m'

import requests
import os
from sys import argv, executable
import base64


def restart():
    os.execl(executable, executable, *argv)

def Enter():
    input("Pressione ENTER para continuar")
    
    restart()

def clear():
    os.system('cls||clear')
    

def opcoes():
    print('{}MILICIA PIKA DE MEL\033[0m'.format(cia))
    print(' ')
    print('\033[4;37mCRIADO POR: SWAG,MRDINIZ,SPYWARE,INTACTOX\033[0;0m')
    print('\033[4;37mGITHUB: Swag666baby // Spyware0 // mrdiniz88\033[m')
    print('ZAP: 556295598220')
    print(' ')
    print('ESCOLHA UM NÚMERO:')
    print(' ')
    print('{}[{}1{}]{} CONSULTA DE CEP'.format(cl,cia,cl,cia))
    print('{}[{}2{}]{} CONSULTA DE IP'.format(cl,cia,cl,cia))
    print('{}[{}3{}]{} CONSULTA DE CNPJ'.format(cl,cia,cl,cia))
    print('{}[{}4{}]{} CONSULTA DE PLACA'.format(cl,cia,cl,cia))
    opc = input('>>>  {}'.format(cl))

    if opc == '1':
    	Cep()

    elif opc == '2':
    	Ip()

    elif opc == '3':
    	Cnpj()
    	
    elif opc == '4':
    	placa()
    	
    else:
        restart()


def Ip():
    clear()

    ip = input('DIGITE O IP: ')
 
    r = requests.get(f'https://ipwhois.app/json/{ip}')
    data = r.json()
    clear()
    print(f'IP: {data["ip"]}')
    print(f'CONTINENTE: {data ["continent"]}')
    print(f'PAIS: {data ["country"]}')
    print(f'CAPITAL: {data ["country_capital"]}')
    print(f'CODIGO DE AREA: {data ["country_phone"]}')
    print(f'ESTADO: {data ["region"]}')
    print(f'LATITUDE: {data ["latitude"]}')
    print(f'LONGITUDEDE: {data ["longitude"]}')
    print(f'PROVEDOR: {data ["asn"]}')
    Enter()


def Cep():
    clear()

    cep = input('DIGITE O CEP: ')
    a = requests.get(f'https://viacep.com.br/ws/{cep}/json')
    cp = a.json()
    clear()
    print(f'cep: {cp["cep"]}')
    print(f'logradouro: {cp["logradouro"]}')
    print(f'complemento: {cp["complemento"]}')
    print(f'bairro: {cp["bairro"]}')
    print(f'localidade: {cp["localidade"]}')
    print(f'uf: {cp["uf"]}')
    print(f'ibgd: {cp["ibge"]}')
    print(f'gia: {cp["gia"]}')
    print(f'ddd: {cp["ddd"]}')
    print(f'siafi: {cp["siafi"]}')
    Enter()

def Cnpj():
    clear()
    cnpj = input('DIGITE O CNPJ: ')
	
    b = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')
	
    pj = b.json()
    
    clear()
	
    print(f'NOME: {pj["nome"]}')
    print(f'COMPLEMENTO : {pj["complemento"]}')
    print(f'ATUALIZACAO CADASTRAL: {pj["data_situacao"]}')
    print(f'TIPO: {pj["tipo"]}')
    print(f'TELEFONE: {pj["telefone"]}')
    print(f'EMAIL: {pj["email"]}')

def placa():
    clear()
    placa = input('DIGITE A PLACA: ')
	
    u = requests.get(f'https://apicarros.com/v1/consulta/{placa}/json', verify=False)
	
    pj = u.json()
    
    clear()

    
    print(f'ANO: {pj["ano"]}')
    print(f'ANO MODELO: {pj["anoModelo"]}')
    print(f'CHASSI: {pj["chassi"]}')
    print(f'CODIGO DE RETORNO: {pj["codigoRetorno"]}')
    print(f'CODIGO DE SITUACAO: {pj["codigoSituacao"]}')
    print(f'DATA: {pj["data"]}')
    print(f'DATA FURTO: {pj["dataAtualizacaoRouboFurto"]}')
    print(f'MARCA: {pj["marca"]}')
    print(f'MODELO: {pj["modelo"]}')
    print(f'LOCALIDADE: {pj["uf"]}')
    print(f'PLACA: {pj["placa"]}')
    print(f'SITUACAO: {pj["situacao"]}')
    print(f'MUNICIPIO: {pj["municipio"]}')
    print(f'RETORNO: {pj["mensagemRetorno"]}')
    Enter()

clear()

opcoes()
