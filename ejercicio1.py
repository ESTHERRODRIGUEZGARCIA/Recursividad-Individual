#ejercicio1 : 1. Búsqueda por dicotomía en una tabla ordenada
palabras = ["comida", "baile", "disfrutar", "escalar", "corazón", "albóndigas"]
print(palabras)

class ejercicio():
    superior = len(palabras)
    n_medio = (superior)//2
    buscar_palabra = str(input("¿Qué palabra desea buscar?"))
    def buscar(n_medio):
        n_tabla = palabras.index(buscar_palabra)
        if n_tabla == n_medio:
            print(f"{buscar_palabra} se encuentra en el índice {n_tabla}")
        elif n_tabla < n_medio:
            buscar(n_medio - 1)
        elif n_tabla > n_medio:
            buscar(n_medio + 1)
    buscar(n_medio)
            
        