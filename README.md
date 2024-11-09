[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WQjBwS08)
# Unidad 3
---
## Documentación del proyecto
Nombre:  Lawrence Barrientos M - Felipe Gomez P 
ID:  000311633 - 000511279
---

## Explicacion del codigo:

### 1. Importación de Módulos 

    import os
    import csv
    import matplotlib.pyplot as plt

**os:** Proporciona funciones para interactuar con el sistema operativo.

**csv:** Permite leer y escribir archivos en formato CSV.

**matplotlib.pyplot:** Biblioteca para crear gráficos.

### 2. Funciones del Programa

#### Función *list_files()*

    def list_files():
        print(os.listdir())

Esta función imprime una lista de archivos en el directorio actual usando *os.listdir()*.

#### Función *count_words(filename)*

    def count_words(filename):
        with open(filename, 'r') as file:
            palabras = file.read().split()
            print(len(palabras))

Abre un archivo de texto, cuenta las palabras dividiendo el contenido en una lista, y muestra la cantidad de palabras.

#### Función *replace_word(filename, palabra1, palabra2)*

    def replace_word(filename, palabra1, palabra2):
        with open(filename, 'r') as file:
            data = file.read()
            data = data.replace(palabra1, palabra2)
        with open(filename, 'w') as file:
            file.write(data)
        with open(filename, 'r') as file:
            print(file.read())

Reemplaza *palabra1* por *palabra2* en el archivo *filename* y muestra el contenido actualizado.

#### Función *count_chars(filename)*

    def count_chars(filename):
        with open(filename, 'r') as file:
            text = file.read().strip()
            print(len(text))

Cuenta y muestra el número de caracteres en el archivo *filename*.

#### Función *calcular_estadisticas(filename, columna)*

    def calcular_estadisticas(filename, columna):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            index = headers.index(columna)
            data = [float(row[index]) for row in reader]
            print('Promedio:', sum(data) / len(data))
            print('Maximo:', max(data))
            print('Minimo:', min(data))

Lee el archivo CSV, obtiene la columna **columna** y muestra el promedio, máximo y mínimo de esa columna.

#### Función graficar_columna(filename, columna)

    def graficar_columna(filename, columna):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            index = headers.index(columna)
            data = [float(row[index]) for row in reader]
            plt.plot(data)
            plt.show()

Lee la columna **columna** de un archivo CSV y la grafica usando *matplotlib*.


### 3. Función Principal *main()* Menu o intefaz del programa:

#### 1. Bucle Principal
    
    def main():
        while True:
            print("Bienvenido!")
            print("\n1. Ver archivos en la ruta actual")
            print("2. Archivo de texto (.txt)")
            print("3. Archivo CSV (.csv)")
            print("4. Salirse del programa")
            option = int(input("Por favor seleccione una opcion:"))

El bucle while True asegura que el programa continúe ejecutándose hasta que el usuario elija la opción de salir (opción 4).

#### 2. Manejo de Opciones
El programa utiliza *if*, *elif*, y *else* para manejar la opción seleccionada por el usuario.

**Opción 1: Listar archivos en el directorio actual**

    if option == 1:
        list_files()

Llama a la función *list_files()*, que imprime una lista de archivos en el directorio actual.

**Opción 2: Operaciones en archivos de texto**

    elif option == 2:
        filename = input("Ingrese el nombre del archivo (.txt):  ")
        print("\n1. Contar numero de palabras")
        print("2. Reemplazar una palabra por otra")
        print("3. Contar el numero de caracteres")
        option2 = int(input("Por favor seleccione una opcion:  "))

