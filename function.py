

def restaura(palavra):
    lista_letras = []
    for letra in str(palavra):
        lista_letras.append(letra)
    return lista_letras

def restaura_vetor(vet):
    vetor_ = []
    for pala in vet:
        vetor_.append(pala)
    return vetor_

def lista():
    palavras_sem_space = []
    lista = open('palavras.txt', 'r')
    for item in lista:
        palavras_sem_space.append(item.rstrip())
    return palavras_sem_space

def filtro_tamanho(palavra):
    plvr = []
    plvr = restaura(palavra)
    lista_filtrada = []
    lista_bruta = lista()
    frase = ""
    cont = 0
    for item in lista_bruta:
        frase = ""
        cont = 0
        if (len(item) <= len(plvr)):
            for x in str(item):
                for y in plvr:
                    if (x == y):
                        frase = frase + x
                        cont = cont + 1
                        plvr.remove(x)
                        break
            if (len(item) == cont):
                lista_filtrada.append(frase)
                for volta in str(frase):
                    plvr.append(volta)
            elif (cont > 0):
                for volta in str(frase):
                    plvr.append(volta)
    return lista_filtrada

def montagem (lista_filtrada, palavra):
    lista_montada = []
    lista_a_montar = []
    plvr = restaura(palavra)
    frase = ""
    frase_aux = ""
    cont = 0
    for main_item in lista_filtrada:
        plvr = restaura(palavra)
        frase = ""
        if (len(main_item) == len(plvr)):
            #lista_a_montar.append(main_item)
            print(main_item)
        else:
            for b in str(main_item): #realiza a exclusão das letras contidas do primeiro item da palavra
                for y in plvr:
                    if (b == y):
                        frase = frase + b
                        plvr.remove(b)
                        break
            for item in lista_filtrada:
                if len(plvr) > 0:
                    frase_aux=""
                    cont = 0
                    for j in str(item):
                        for i in plvr:
                            if (j == i):
                                frase_aux = frase_aux + i
                                cont = cont + 1
                                plvr.remove(i)
                                break
                    if cont == len(item):
                        frase = frase + ("-") + frase_aux
                        frase_aux = " "
                    else:
                        for volta in str(frase_aux):
                            plvr.append(volta)
                        frase_aux = ""

            print(frase)
    return lista_a_montar



