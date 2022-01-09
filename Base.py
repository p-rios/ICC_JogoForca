import imgs


def Base():
    print(imgs.bemvindo)
    arrayPalavra = ["c", "a", "c", "h", "o", "r", "r", "o"]

    arrayPrint = []
    for i in arrayPalavra:
        arrayPrint.append("_")

    print(arrayPrint)
    tentativa = input("Digite uma letra: ")
    if ((tentativa in arrayPalavra)):
        print("Acertou!")

        for tentativa in arrayPalavra:
            index = arrayPalavra.index(tentativa)-
            print(index)

        #  string = tentativa.replace(arrayPrint[index], tentativa)
            arrayPrint[index] = tentativa
            arrayPalavra[index:]

#    elif  ((tentativa in arrayPalavra) == 2):

        print(arrayPrint)
    else:
      #  print(imgs.errou)
       #   string = tentativa.replace(arrayPrint[index], tentativa)
        print("ERROOOOOOOOOOU")


Base()
