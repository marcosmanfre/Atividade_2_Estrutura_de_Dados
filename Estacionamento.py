estacionamentoA = Stack()
estacionamentoB = Queue()

from Queue import Queue
from Stack import Stack

menuPrincipal = 0
menuEstacionamento = 0
menuSaida = 0
menuVerifica = 0

#Funções
def estacionarA():
    while True:
        r = 'S'
        while r == 'S':                                                 
            print('Cadastre o veiculo estacionado')
            placaDigitada = str(input('Digite a placa do veiculo: '))
            estacionamentoA.push(placaDigitada)
            r = str(input('quer continuar? [S/N] ')).upper()
        break

def estacionarB():
    while True:
        r = 'S'
        while r == 'S':                                                 
            print('Cadastre o veiculo estacionado')
            placaDigitada = str(input('Digite a placa do veiculo: '))
            estacionamentoB.push(placaDigitada)
            r = str(input('quer continuar? [S/N] ')).upper()
        break

def retirarA():
    while True:
        r = 'S'
        while r == 'S':                                                 
            print('Registre a saída do veiculo estacionado')
            r = str(input('Deseja realmente registrar a saída do veículo? [S/N] ')).upper()
            if r != 'S':
              estacionamentoA.pop()
        break

def retirarB():
    while True:
        r = 'S'
        while r == 'S':                                                 
            print('Registre a saída do veiculo estacionado: ')
            r = str(input('Deseja realmente registrar a saída do veículo? [S/N] ')).upper()
            if r != 'S':
              estacionamentoB.pop()
        break

def carros_estacionadosA():
    while True:
        print("Lista de carros estacionados")
        print(estacionamentoA)
        print("Proximo carro a ser retirado: " )
        print(estacionamentoA.peek())
        break


def carros_estacionadosB():
    while True:
        print("Lista de carros estacionados")
        print(estacionamentoB)
        print("Proximo carro a ser retirado: " )
        print(estacionamentoB.peek())
        break

        
              
#Início do Programa


while True:
    print("\n---------------------------------------------")
    print('Sistema de Gerenciamento de Estacionamento')
    print("\n---------------------------------------------")
    menuPrincipal = (input("1. Registrar Entrada \n2. Registrar Saída\n3. Veiculos Estacionados\n4. Sair do Programa\n\nDigite uma opção: "))
    print("\n------------------------")


    if(menuPrincipal == "1"):
        while True:
            print('Selecionar Estacionamento: ')
            menuCadastrar = (input("1. Estacionamento A\n2. Estacionamento B\n3. Retornar ao Menu Inicial\nDigite uma opção: "))
            print("\n")

    
#MENU CADASTRAR
            if (menuCadastrar == "1"):
                estacionarA()

                print(estacionamentoA)


            if (menuCadastrar == "2"):
                estacionarB()              

                print(estacionamentoB)
                            

            elif (menuCadastrar == "3"):
              menuCadastrar = 0
              break    


    elif(menuPrincipal == "2"):
      while True:
            print('Selecionar Estacionamento: ')
            menuSaida = (input("1. Estacionamento A\n2. Estacionamento B\n3. Retornar ao Menu Inicial\nDigite uma opção: "))
            print("\n")

#MENU DE SAÍDA
            if (menuSaida == "1"):
                retirarA()             
                print(estacionamentoA)

            if (menuSaida == "2"):
                retirarB()                  
                print(estacionamentoB)

            
            elif (menuSaida == "3"):
              menuSaida = 0
              break    


    elif(menuPrincipal == "3"):
      while True:
            print('Selecionar Estacionamento: ')
            menuVerifica = (input("1. Estacionamento A\n2. Estacionamento B\n3. Retornar ao Menu Inicial\nDigite uma opção: "))
            print("\n")

#MENU DE VERIFICAÇÃO
            if (menuVerifica == "1"):
              carros_estacionadosA()
                                    
            if (menuVerifica == "2"):
              carros_estacionadosB()
                     
            elif (menuVerifica == "3"):
              menuVerifica = 0
              break    
     

    elif(menuPrincipal == "4"):
        print("Obrigado por utilizar nosso programa!!! ")
        print("\n------------------------")
        break   