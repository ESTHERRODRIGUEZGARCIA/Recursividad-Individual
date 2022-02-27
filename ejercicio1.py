#ejercicio1 : 1. Búsqueda por dicotomía en una tabla ordenada
palabras = ["comida", "baile", "disfrutar", "escalar", "corazón", "albóndigas"]
print(palabras)

class ejercicio():
    def buscar(self, n, tabla):
        
        superior = len(palabras)
        n_medio = (superior)//2
        palabra_buscar = str(input("¿Qué palabra desea buscar?"))
