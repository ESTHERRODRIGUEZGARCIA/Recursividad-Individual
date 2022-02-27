#ejercicio2: Análisis de una cadena de caracteres
class palindromos():
    palabra = str(input("Qué palabra desea comprobar si es un palíndromo?"))

    i,j = "áéíóúñÁÉÍÓÚÑ" , "AEIOUÑaeiouñ"
    acento = str. maketrans(i,j)
    palabra = palabra.translate(acento)
    palabra = palabra.lower()
    
