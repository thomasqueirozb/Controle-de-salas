# else if elif for with while await assert global not nonlocal continue del pass print in import as raise try except finally class lambda:
# TEMP TODO REVIEW QUESTION OPTIMIZE NOTE IDEA FIXME COMBAK BUG HACK WARNING XXX

from tempo import *
from bs4 import BeautifulSoup
import urllib.request

print_result = True
get_from_web = False
save_to_xml  = False

if get_from_web:
    URL = "http://insper.edu.br/agenda/xml/ExibeCalendario.xml"

    # Pegar o arquivo .XML
    request = urllib.request.Request(URL)
    response = urllib.request.urlopen(request)

    # Ler o arquivo
    content = BeautifulSoup(response.read(), features = "lxml")

    if save_to_xml:
        # Salvar em um xml
        f = open('varios.xml', "w")
        f.write(content.prettify())
        f.close()

else:
    # Ler o xml
    f = open('varios.xml', "r")
    response = ''.join(f.readlines())
    content = BeautifulSoup(response, features = "lxml")
    f.close()


# Pegar todos os eventos
eventos = content.findAll('calendarioevento')


# Pega o tempo agora em formato datetime
agora = datetime.datetime.now()

# Pega o ano, mês e dia e transforma em string
data = f'{format(agora.day, "02d")}/{format(agora.month, "02d")}/{agora.year}'

# Transforma em um formato time
agora = time(agora.hour,agora.minute,agora.second)

#    WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING
agora = time(8,30) # WARNING WARNING WARNING WARNING WARNING WARNING WARNING
#    WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING

from collections import defaultdict as ddict
salas = ddict(list)

salas_all = []
with open('salas.txt','r') as salas_text:
    for linha in salas_text:
        salas_all.append(linha.replace('\n',''))

for sala in salas_all:
    salas[sala] = []


for evento in eventos:
    # Verificar se a data do evento é igual a data de hoje
    if evento.find('data').text == data or True: # WARNING WARNING WARNING WARNING

        # Converter hora de início e fim em um objeto time
        tempo = [evento.find('horainicio').text.split(':'), evento.find('horatermino').text.split(':')]
        tempo = [time(int(i[0]), int(i[1])) for i in tempo]

        # Aulas que já passaram não precisam ser analisadas
        if not passou(tempo,agora):
            sala = evento.find('sala').text

            # if sala not in salas_all: print(sala)
            sala = sala.replace('\n','').strip()# WARNING WARNING WARNING

            # Retirando salas do nono andar
            if sala[:1] != '9' and sala !='':
                salas[sala].append(tempo)

                # if len(salas[sala]) == 1:
                #     salas[sala][0] = tempo[1]


# Salas livres todo o dia
todo_dia = []
for i in list(salas.keys()):
    if salas[i] == []:
        todo_dia.append(i)
        del salas[i]

def sort_time(l):
    ''' Reordena a lista em ordem crescente de tempo '''
    ret = []

    while len(l) != 0:
        # Valor inicial para o menor valor; usar float('-inf') provavelmente não
        # funciona, pois os elementos da lista são objetos time, não floats.
        min = l[0]
        index = 0

        # Pegar menor valor
        for k in range(len(l)):
            if min[1] > l[k][0]:
                min = l[k]
                index = k

        # Tirar o menor tempo da lista
        ret.append(l.pop(index))

    return ret

def join(l, min_time = time(0,15,0)):
    ret = []
    # print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    # print(l)

    repeat = True
    while repeat:
        repeat = False
        i = len(l) - 1
        while i > 1:
            diff = time_difference(l[i][0], l[i-1][1])
            if min_time >= diff and False:
                # repeat = True
                if l[i][0]> l[i-1][1]:
                    print('Arrow função join')

                ret.append([l[i-1][0], l[i][1]])
            else:
                ret.append(l[i])
                ret.append(l[i-1])
            i -= 1
    # print(list(reversed(ret)))
    return reversed(ret)

# Salas ocupadas
for sala in salas:
    salas[sala] = sort_time(salas[sala])
    join(salas[sala])

    # .append([time(23,59,59)])
    #
    # for k in range(len(new)-1):
    #     salas[sala].append([new[k][1], new[k + 1][0]])

if print_result:
    for sala in list(salas.keys()):
        if time_in_range(salas[sala][-1],agora):
            todo_dia.append(sala)
            del salas[sala]


    if len(todo_dia) > 0:
        print("Salas livres até o fim do dia:\n")
        print("\n".join(sorted(todo_dia)))


    print("\n\n")
    for i in salas:
        print('=============')
        print(i)
        for k in salas[i]:
            print(k[0].isoformat()[:-3] + ' - ',end='')
            print(k[1].isoformat()[:-3] if k[1].isoformat()[:-3] != '23:59' else 'Fim do dia')
    print('=============')
