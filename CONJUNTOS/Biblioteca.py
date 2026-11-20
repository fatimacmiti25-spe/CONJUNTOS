# Diccionario de libros
libros = {
    1: "Matematicas",
    2: "Programacion",
    3: "Historia",
    4: "Ingles",
    5: "Fisica"
}

# Conjuntos de libros
matematicas = {1, 5}
tecnologia = {2, 5}
prestados = {2, 4}

# Union
union = matematicas | tecnologia
print("Union:", union)

# Interseccion
interseccion = matematicas & tecnologia
print("Interseccion:", interseccion)

# Diferencia
disponibles = set(libros) - prestados
print("Libros disponibles:", disponibles)

# Mostrar libros disponibles
for id_libro in sorted(disponibles):
    print(libros[id_libro])

# Buscar un libro
buscar = int(input("Ingresa el ID del libro: "))

if buscar in libros:
    print("Libro encontrado:", libros[buscar])
else:
    print("Libro no encontrado")