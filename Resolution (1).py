import requests
import xmltodict
import dicttoxml
from xml.etree import ElementTree as elements

URL = "https://storage.googleapis.com/psel-2021/soleng%26backoffice/Psel2021.xml"

data = requests.get(url = URL)
database = xmltodict.parse(data.content)
xmlData = dicttoxml.dicttoxml(database)

#Funcao Validar CPF =/ de coordenador casado

def validaFormatoCPF(text):
    CPF: r'\d{3}\.\d{3}\.\d{3}-\d{2}'
    if d{1}*10 + d{2}*9 + d{3}*8 + d{4}*7 + d{5}*6 + d{6}*5 + d{7}*4 + d{8}*3 + d{9}*2/11 == 0:
        d{10} = 0
    elif d{1}*10 + d{2}*9 + d{3}*8 + d{4}*7 + d{5}*6 + d{6}*5 + d{7}*4 + d{8}*3 + d{9}*2/11 != 0:
        d{10} =d{1}*10 + d{2}*9 + d{3}*8 + d{4}*7 + d{5}*6 + d{6}*5 + d{7}*4 + d{8}*3 + d{9}*2/11 == 0
    elif d{1}*11 + d{2}*10 + d{3}*9 + d{4}*8 + d{5}*7 + d{6}*6 + d{7}*5 + d{8}*4 + d{9}*3 + d{10} *2 /11 == 0 or d{1}*11 + d{2}*10 + d{3}*9 + d{4}*8 + d{5}*7 + d{6}*6 + d{7}*5 + d{8}*4 + d{9}*3 + d{10} *2 /11 == 1:
        d{11} = 0
    elif d{1}*11 + d{2}*10 + d{3}*9 + d{4}*8 + d{5}*7 + d{6}*6 + d{7}*5 + d{8}*4 + d{9}*3 + d{10} *2 /11 != 0 or d{1}*11 + d{2}*10 + d{3}*9 + d{4}*8 + d{5}*7 + d{6}*6 + d{7}*5 + d{8}*4 + d{9}*3 + d{10} *2 /11 != 1:
        d{11} = d{1}*11 + d{2}*10 + d{3}*9 + d{4}*8 + d{5}*7 + d{6}*6 + d{7}*5 + d{8}*4 + d{9}*3 + d{10} *2 /11

validaFormatoCPF = True

root = elements.fromstring(dadosxml)
raiz = root.findall('.//employee')
    for level in raiz:
        position = level.find('position').text
        marital_status = level.find('marital_status').text
        if (validaFormatoCPF == True):
            print(name)
            print(marital_status)
                

#Percorrer XML - All employee - pegar salary - laço de repetição e ordenar  sort reverse
root = elements.fromstring(dadosxml)
raiz = root.findall('.//employee')
for level in raiz:
    salary = level.find('salary').text
    sorted(salary, key=int, reverse=true)
    print(salary)


#Percorrer XML - Listar funcionários - If cargoFuncionário == cargoDesejado = incrementa 1
analistacont = 0
coordenadorcont = 0
gerentecont = 0
diretorcont = 0
root = elements.fromstring(dadosxml)
raiz = root.findall('.//employee')
for level in raiz:
    position = level.find('position').text
    if (position == 'COORDENADOR'):
        print(name)
        coordenadorcont ++
    elif (position == 'Analista')
        print(name)
        analistacont ++
    elif (position == 'GERENTE')
        print(name)
        gerentecont ++
    elif (position == 'DIRETOR')
        print(name)
        diretorcont ++
    
print("Número de Analistas: ", analistacont)
print("Número de Coordenadores: ", coordenadorcont)
print("Número de Gerentes: ", gerentecont)
print("Número de Diretores", diretorcont)

#Percorrer XML - Coordenador - position = Coordenador - pegar valores de salary - sort reverse - laço while num < 5 - cada salary incrementa até os 5
num = 0
root = elements.fromstring(dadosxml)
raiz = root.findall('.//employee')
for level in raiz:
    position = level.find('position').text
    if (position == 'COORDENADOR'):
        salary = level.find('salary').text
        sorted(salary, key=int, reverse=true)
        while (num <= 5)
            print(salary)

#Percorrer XML - Analísta - position = Analista - pegar valor salary de Analistas e somar
root = elements.fromstring(dadosxml)
raiz = root.findall('.//employee')
for level in raiz:
    position = level.find('position').text
    if (position == 'ANALISTA'):
        salary = level.find('salary').text
        salaryfin = salary + salary2