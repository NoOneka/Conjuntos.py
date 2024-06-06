conjunto1 = []
conjunto2 = []

#Funções para as operações entre os conjuntos
def menuConj():
    array1 = []
    array2 = []

    while True:
        try:
            for i in range(4):
                elemento = int(input(f"Digite o elemento {i + 1} do array: "))
                array1.append(elemento)
                continue

            for i in range(4):
                elemento = int(input(f"Digite o elemento {i + 1} do array2: "))
                array2.append(elemento)
                continue
        except:
            print("Operação não permitida.Tente digitar um número.")
            continue
        finally:
            print(" ")
        break

    return array1, array2

def interseccção(array1, array2):
    conj1 = set(array1)
    conj2 = set(array2)
    a = conj1.intersection(conj2)
    return sorted(list(a))

def main():

    conjunto1, conjunto2 = menuConj()

    diferença= lambda x, y: sorted(list(set(x) - set(y)))
    resultadoDiferença = diferença(conjunto1, conjunto2)

    uniao = lambda x, y: sorted(list(set(x) | set (y)))
    resultadoUniao = uniao(conjunto1,conjunto2)

    resultadoIntersec = interseccção(conjunto1, conjunto2)

    #Finalização do codigo
    print("Conjuntos preenchidos: ")
    print(conjunto1)
    print(conjunto2)

    op = input("Qual operação deseja realizar entre os conjuntos? 1 - Interseccção / 2 - Diferença / 3 - União: ")
    if op == "1" : print("Resultado é da intersecção entre os conjuntos é: ", resultadoIntersec)
    elif op == "2" : print("Resultado da diferença entre os conjuntos é: ", resultadoDiferença)
    elif op == "3" : print("Resultado da união entre os conjuntos é:" , resultadoUniao)

    while True:
        try:
            repetir = int(input("Deseja repetir? 1 - Sim / 2 - Não"))
            if repetir == 2:
                print("Saindo...")
                break
            elif repetir == 1 :
                print(main())
            else:
                print("Operação invalida. Tente novamente...")
        except ValueError:
            print("Operação inválida. Tente novamente...")



if __name__=="__main__":
    ProgramaMain = main()

