#ejercicio2: Análisis de una cadena de caracteres
class palindromos():
    palabra = str(input("Qué palabra desea comprobar si es un palíndromo?"))

    i,j = "áéíóúñÁÉÍÓÚÑ" , "AEIOUÑaeiouñ"
    acento = str. maketrans(i,j)
    palabra = palabra.translate(acento)
    palabra = palabra.lower()
    palabra = palabra.replace(" " , " ")
    lista = list(palabra)
    listafinal= list(reversed(palabra))
    def comprobar(palabra):
        if len(palabra) < 1:
            print(f" {palabra} es un palíndromo")
        else:
            if palabra[0] == palabra [-1]:
                comprobar(palabra[1:-1])
            else:
                print(f"{palabra} no es un palíndromo")
    comprobar(palabra)

    
