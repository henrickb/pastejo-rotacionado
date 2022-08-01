import os

bancoFazenda = list()
bancoAnimais = list()
filtrados = list()

def area():

    local = str(input("Informe a área: "))
    for item in bancoFazenda:
        if item.get('nomeLocal') == local:
            print("*"* 50)
            print("Esta área já exite no banco de dados")
            os.system("pause")
            menu()
            
    quantidade = int(input("Informe a quantidade máxima de animais: "))
    gmd = float(input("Informe o GMD da área: "))
    bancoFazenda.append({'quantidade_maxima':quantidade,'gmd_area':gmd,'local':[],'nomeLocal':local })
 
    menu()

def brinco():
    
    numBrinco = str(input("Informe o Brinco do animal: "))
    for item in bancoAnimais:
        if item.get('brinco') == numBrinco:
            print("*"* 50)
            print("Este animal já consta no banco de dados")
            os.system("pause")
            menu()
    
    peso = float(input(f"Informe o peso do animal{numBrinco}:"))
    bancoAnimais.append({'brinco':numBrinco, 'kg':peso})
    menu()

def rotacao():
    
    brincoAnimal = str(input("Informe o Brinco do animal: "))
    local = str(input("Informe a área: "))
    dia = int(input("Informe quantos dias ele vai passar nesta determinada área: "))
    animalEncontrado = ''
    localEncontrado = ''   
    for animal in bancoAnimais:
        if(animal.get('brinco') == brincoAnimal):
            animalEncontrado = animal
            
    for localizar in bancoFazenda:
        if(localizar.get('nomeLocal') == local):
            localEncontrado = localizar
    if localEncontrado == '' or animalEncontrado == '':
        print("animal ou local não encontrado")
        os.system("pause")
        menu()

    verificandoCapacidade(animalEncontrado, localEncontrado, dia)
    
def verificandoCapacidade(animalEncontrado, localEncontrado, dia):

    if localEncontrado.get('quantidade_maxima') > len(localEncontrado.get('local')):
        
        pesoAtual = ((dia*localEncontrado.get('gmd_area')) + animalEncontrado.get('kg'))
        peso = {'kg':pesoAtual}
        animalEncontrado.update(peso)
        rota:list = localEncontrado.get('local')
        removendoAnimal(animalEncontrado)
        rota.append(animalEncontrado)
        menu()
    else:
        print("Não existe espaço para esse animal nesta área")
        os.system("pause")
        menu()

def removendoAnimal(animalEncontrado):
    for area in bancoFazenda:
        for animal in area.get('local'):

            if animal.get('brinco') == animalEncontrado.get('brinco'):
                
                area.get('local').remove(animalEncontrado)

def listagem(banco):

    for animal in banco:
        print(f"O animal: {animal.get('brinco')} tem o peso: {animal.get('kg')} ")
    
    if bancoAnimais == []:
        print("Não existe animais neste banco de dados")
    
    os.system("pause")    
    menu()
def procurando():
    animalProcurado = ''
    boolean = True
    print("Informe o Brinco do animal para fazer a pesquisa \n se não digite 'exit' para devolver a lista")
    
    while boolean != False:
        busca = str(input("Informe o animal que você estar procupando: "))
    
        if busca == 'exit':
            if filtrados == []:
                print("Você não específicou nenhum animal existente")
                os.system("pause")
                menu()
            else:

                listagem(filtrados)
                boolean = False

        for animal in bancoAnimais:
            
            if animal.get('brinco') == busca:

                animalProcurado = animal
                filtrados.append(animal)                
                
        if animalProcurado == '':
            
            print("Animal não encontrado no banco de dados")
            os.system("pause")
            os.system("cls")
            procurando()

def menu():

    os.system("cls")

    print(
    "Menu" 
    "\n1-Adicionar área" 
    "\n2-Adicionar Animal" 
    "\n3-Rotacionar Animal" 
    "\n4-Mostrar todos os animais" 
    "\n5-Procurar animais" 
    "\n6-Sair")
    
    op = str(input("Escolha uma opção: "))

    
    if op == '1':
        area()

    elif op == '2':
        brinco()

    elif op == '3':
        rotacao()

    elif op == '4':
        listagem(bancoAnimais)
    
    elif op == '5':
        procurando()
    
    elif op == '6':
        os.system("cls")
        print("Você saiu do Software\nObrigado por ultilizar nosso Software!")
        os.system("pause")
        os.system("exit")

    else:
        os.system("cls")
        print("Escolha um número relacionado ao menu")
        os.system("pause")
        menu()

menu()