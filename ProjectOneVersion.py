# 1 parte

def formatacaoNumero(numero): #função que vai fazer as validações e a formatação
    DDI = "+55"
    DDD = [{"BA": ["71", "73","74", "75", "77"]}, #lista de DDD
           {"SP": ["11", "12", "13", "14", "15", "16", "17", "18", "19"]},
           {"MG": ["31", "32", "33", "34", "35", "37", "38"]},
           {"ES": ["27", "28"]},
           {"RJ": ["21", "22", "24"]}
           ]

    if numero.startswith(DDI): #verifica se a inicial dos números iniciam ou não com +55
        num = numero
        print(f"DDI {DDI} encontrado!")
    else:
        num = DDI + numero
        print(f"DDI {DDI} adicionado!")

    prefixo = num[3:5] #pego apenas os dois números que indicam o DDD

    for item in DDD: #laço que vai passar por todos os DDD da lista
        for estado, codigo in item.items(): #laço que captura a chave e o valor do dicionario
            if prefixo in codigo: # verifica se o prefixo está incluído na lista de ddd
                print(f"Seu número é: {num}  Estado: {estado}") #printa o resultado
                return True


    return False





#ESCOPO PRINCIPAL

numero = ["11923456789", "71923456789", "+5571923456788" ]
for num in numero:
    funcao = formatacaoNumero(num)