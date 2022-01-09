import imgs


def Base():
    print(imgs.bemvindo)
   
    palavra = "cachorro"
    arrayPrint = []
    contador = 4
    arrayLetras = []
    fim = False
    for i in palavra:
        arrayPrint.append("_")
        arraytest = []
    
    print(arrayPrint)
    
    while (fim == False):
     letra = input("Digite uma letra: ")
 
     k = 0
     while (k< len(palavra)):
      if (letra == palavra[k]):
        arrayletras = "".join(letra)
        print(arrayLetras)
            
      else:
        #  a.append("_")
        arrayLetras = "".join("_") 
     k+=1
    print(array)
     

        

Base()