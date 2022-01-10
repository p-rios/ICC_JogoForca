import imgs


def Base():

    print(imgs.bemvindo)

    arrayPalavra = ["c", "a", "c", "h", "o", "r", "r", "o"]
    arrayPrint = []
    contador = 4
    arrayLetra = []
    fim = False

    for i in arrayPalavra:
        arrayPrint.append("_")

    print(arrayPrint)

    while fim == False:

        print(f"Voce tem : {contador} chances")

        letra = input("Digite uma letra: ")

        if (len(letra) != 1):
            print("Opa, vc ñ digitou um caractere e afim de manter integridade do jogo estamos encerrando, contamos com a sua compreensão, a gerência")
            break

        k = 0

        while (k < len(arrayPalavra)):
            if ((letra == arrayPalavra[k])):
                arrayPrint[k] = letra

            k += 1

        print(arrayPrint)

        if (letra not in arrayPalavra):
            contador -= 1

        if (contador == 0):
            fim = True

            print(
                "         YOU DIED \n OPA JOGO ERRADO, QUIS DIZER \n      >>GAME OVER<<")

        if (arrayPrint == arrayPalavra):
            fim = True
            print("Parabéns vc venceu, brabo dmais!!!")


Base()
