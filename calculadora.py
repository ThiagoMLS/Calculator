# FUNÇÕES
def menu():
    print("-"*10,"CALCULADORA","-"*10)
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (x)")
    print("4 - Divisão (÷)")
    print("0 - Fechar programa")
    print("-"*30)


def soma():
    try:
        print()
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print()
        sum = n1 + n2
        print(f"{n1} + {n2} = {sum}")
    
    except Exception as error:
        print(">>>>> Falha na operação")
        print("Erro: ",error)

    
def subtracao():
    try:
        print()
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print()
        sub = n1 - n2
        print(f"{n1} - {n2} = {sub}")

    except Exception as error:
        print(">>>>> Falha na operação")
        print("Erro: ",error)


def multiplicacao():
    try:
        print()
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print()
        mult = n1 * n2
        print(f"{n1} x {n2} = {mult}")

    except Exception as error:
        print(">>>>> Falha na operação")
        print("Erro: ",error)


def divisao():
    try:
        print()
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print()
        div = n1 / n2
        print(f"{n1} ÷ {n2} = {div}")

    except ZeroDivisionError:
        print(">>>>> Não é possível a divisão por zero (0)")

    except Exception as error:
        print(">>>>> Falha na operação")
        print("Erro: ",error)



# INÍCIO DO PROGRAMA

while True:
    menu()
    opcao = input("Escolha sua opção: ")

    if opcao == "0":
        print(">>>>> Fechando programa...")
        break

    elif opcao == "1":
        soma()

    elif opcao == "2":
        subtracao()

    elif opcao == "3":
        multiplicacao()

    elif opcao == "4":
        divisao()

    else:
        print(">>>>> Opção inválida")
    
