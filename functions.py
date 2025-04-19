import time

Ia_existentes = {}
Publicacoes_das_ias = {}

def CreateIa():

    while True:
        TempIaName = input("\nPor favor informe o nome da IA ao qual deseja criar/cadastrar: ")

        if TempIaName in Ia_existentes:
            print("\nEsse nome se encontra em uso, por favor informe um novo nome valido!!")
        elif TempIaName not in Ia_existentes:
            Ia_existentes[TempIaName] ={
                "nome_da_ia": TempIaName,
                "data_do_cadastro": str(time.strftime("%d/%m/%y")),
                "publicacoes": 0,
                "curtidas_recebidas": 0
            }
            RepeatRegisterOfIa = input("\nDeseja criar mais uma IA ? (S/N)")
        
        if RepeatRegisterOfIa.lower() == "n":
            return False

def CreatePublication():
    while True:
        TempPubliName = input("\nInforme o nome da sua publicação: ")

        TempTextPubli = input("\nPor favor informe o texto ao qual deseja colocar na publicação: ")

        print("\nPor favor escolha uma IA para realizar a postagem!")
        
        for id, ia in Ia_existentes.items(): 
            print(f"{ia['nome_da_ia']}")

        TempIaAssignment = str(input("\nIforme sua escolha a seguir: "))

        Publicacoes_das_ias[TempPubliName] = {
            "nome_publi": TempPubliName, 
            "texto_publi": TempTextPubli, 
            "ia_responsavel": TempIaAssignment.lower(),
            "curtidas": 0
            }
        
        Ia_existentes[TempIaAssignment]['publicacoes'] += 1
        
        if input("\nDeseja criar mais alguma publicação ? (S/N)") == "n":
            return False

def LikePublication():
    while True:
        print("\nEscolha uma das publicações a seguir para curtir: ")

        for name_publi,publi in Publicacoes_das_ias.items(): 
                print(f"{name_publi} - {publi["texto_publi"]}")
        
        TempLikePublication = input("\nInforme o nome da publicação ao qual deseja curtir: ")

        for name_publi, publi in Publicacoes_das_ias.items(): 
            if publi["nome_publi"] == TempLikePublication:
                Publicacoes_das_ias[name_publi]["curtidas"] +=1
                Ia_existentes[publi['ia_responsavel']]['curtidas_recebidas'] += 1
                return False
            elif TempLikePublication not in publi["nome_publi"]:
                print("\nPublicação não encontrada!!")

def DeletePublication():
    print("hello world")#em desenvolvimento (deletar uma publicação)

def EditPublication():
    print('hello world')#em desenvolvimento (editar uma publicação)

def DeleteIa():
    print("hello world")#em desenvolvimento (deletar uma ia)

def EditIa():
    print('hello world')#em desenvolvimento (editar uma ia)

def ShowIa():
    print("\nSegue a lista de todas as IA cadastradas na aplicação: ")
    for id, ias in Ia_existentes.items():
            print(f"\nNome da IA: {ias['nome_da_ia']} \nData da Criação: {ias['data_do_cadastro']} \nTotal de publicações: {ias['publicacoes']} \nTotal de curtidas: {ias['curtidas_recebidas']}")

def ShowPublications():
    if Publicacoes_das_ias.__len__() == 0:
        print("\nVocê não tem uma publicação criada ainda!")

    elif Publicacoes_das_ias.__len__() > 0: 
        print("\nAqui estão todas a publicações criadas ao decorrer do funcionamento da aplicação: ")

        for name_publi, publi in Publicacoes_das_ias.items():
            print(f"\nNome da Publicação: {publi["nome_publi"]} \nTexto da Publicação: {publi["texto_publi"]} \nIA responsavel pela publicação: {publi["ia_responsavel"]} \nCurtidas: {publi["curtidas"]}")

def OptionsZeroIa():
    print("\nBem vindo a Software de publicações e cadastro de Ia!!")
    print("Para desbloquear mais opções, primeiro cadastre uma IA!")
    print("Por favor selecione uma das opções a seguir: ")

    print("\n1-Cadastrar IAS")
    print("6-Sair")

    chooseOption = int(input("Informe sua escolha aqui: "))

    if chooseOption == 1:
        CreateIa()
    elif chooseOption == 6:
        return 6

def OptionsOneMoreIa():
   while True :
        print("Por favor selecione uma das opções a seguir: ")

        print("\nSelecione uma opção: ")
        print("\n1-Cadastrar IAS")
        print("2-Cadastrar Publicações")
        print("3-Curtir uma Publicação")
        print("4-Mostrar IAS cadastradas")
        print("5-Mostrar Publicações criadas")
        print("6-Sair da aplicação")

        chooseOption = int(input("Informe sua escolha aqui: "))

        if chooseOption == 1:
            CreateIa()
        elif chooseOption == 2:
            CreatePublication()
        elif chooseOption == 3:
            LikePublication()
        elif chooseOption == 4:
            ShowIa()
            time.sleep(3)
        elif chooseOption == 5:
            ShowPublications()
            time.sleep(3)
        elif chooseOption == 6:
            return 6  

def MenuSoftware():
    while True: 
        if Ia_existentes.__len__() == 0:
            if OptionsZeroIa() == 6:
                break
        elif Ia_existentes.__len__() > 0:
            if OptionsOneMoreIa() == 6:
                break