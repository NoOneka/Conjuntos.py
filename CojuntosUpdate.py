def menuConj(array1):
    array1.clear()

    for i in range(4):

       while True:
            try:
                elemento = int(input(f"Digite o elemento {i + 1} do array: "))
                if elemento in array1:
                    raise ValueError("Elemento duplicado. Digite um elemento diferente")
                array1.append(elemento)
                break

            except ValueError:
                print("Operação não permitida.Tente digitar um número.")

    return array1

conjunto1 = []
conjunto2 = []

def interseccção(array1, array2):
    conj1 = set(array1)
    conj2 = set(array2)
    a = conj1.intersection(conj2)
    return sorted(list(a))


def ops():
    menuConj(conjunto1)
    menuConj(conjunto2)

    diferença = lambda x, y: sorted(list(set(x) - set(y)))
    resultadoDiferença = diferença(conjunto1, conjunto2)

    uniao = lambda x, y: sorted(list(set(x) | set(y)))
    resultadoUniao = uniao(conjunto1, conjunto2)

    resultadoIntersec = interseccção(conjunto1, conjunto2)
    return resultadoIntersec, resultadoUniao,resultadoDiferença

def main():
    resultadoIntersec, resultadoDiferença, resultadoUniao = ops()
    print("Conjuntos preenchidos: ")
    print(conjunto1)
    print(conjunto2)

    op = input("Qual operação deseja realizar entre os conjuntos? 1 - Interseccção / 2 - Diferença / 3 - União: ")
    if op == "1":
        print("Resultado é da intersecção entre os conjuntos é: ", resultadoIntersec)
    elif op == "2":
        print("Resultado da diferença entre os conjuntos é: ", resultadoDiferença)
    elif op == "3":
        print("Resultado da união entre os conjuntos é:", resultadoUniao)

    while True:
        try:
            repetir = int(input("Deseja repetir? 1 - Sim / 2 - Não"))
            if repetir == 2:
                print("Saindo...")
                break
            elif repetir == 1:
                return main()
            else:
                print("Operação invalida. Tente novamente...")
        except ValueError:
            print("Operação inválida. Tente novamente...")


if __name__ == "__main__":
    main()
