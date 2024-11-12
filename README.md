[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WQjBwS08)
# Unidad 3
---
## Documentación del proyecto
## Nombre:  Lawrence Barrientos M - Felipe Gomez P 
## ID:  000311633 - 000511279
---

## Explicacion del codigo:

### 1. Importación de Módulos 

    import os
    import csv
    import matplotlib.pyplot as plt

- **os:** Proporciona funciones para interactuar con el sistema operativo.

- **csv:** Permite leer y escribir archivos en formato CSV.

- **matplotlib.pyplot:** Biblioteca para crear gráficos.

---

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

---

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


- **Opción 1: Listar archivos en el directorio actual**

        if option == 1:
            list_files()

Llama a la función *list_files()*, que imprime una lista de archivos en el directorio actual.


- **Opción 2: Operaciones en archivos de texto**

        elif option == 2:
            filename = input("Ingrese el nombre del archivo (.txt):  ")
            print("\n1. Contar numero de palabras")
            print("2. Reemplazar una palabra por otra")
            print("3. Contar el numero de caracteres")
            option2 = int(input("Por favor seleccione una opcion:  "))

Solicita el nombre de un archivo de texto.
Muestra un submenú específico para archivos de texto con tres opciones:

- Contar el número de palabras.

- Reemplazar una palabra por otra.

- Contar el número de caracteres.

Dependiendo de la selección, el programa llama a una de las funciones correspondientes:

#### 1. Contar Palabras:

    if option2 == 1:
        count_words(filename)

Llama a *count_words(filename)*, que cuenta las palabras y las imprime.

#### 2. Reemplazar Palabras:

    elif option2 == 2:
        palabra1 = input("Por favor escriba la palabra que desea reemplazar:  ")
        palabra2 = input("Por favor escriba la palabra por la que quiere reemplazar:  ")
        replace_word(filename, palabra1, palabra2)

Solicita la palabra que se desea reemplazar (palabra1) y la palabra nueva (palabra2).

Llama a *replace_word(filename, palabra1, palabra2)*, que realiza el reemplazo y muestra el contenido actualizado.

#### 3. Contar Caracteres:

    elif option2 == 3:
        count_chars(filename)

Llama a *count_chars(filename)*, que cuenta el número de caracteres y muestra el resultado.

#### 4. Opción Inválida:

    else:
        print("Opcion no valida")

Muestra un mensaje si la opción no es válida.


- **Opción 3: Operaciones en archivos CSV**

        elif option == 3:
            filename = input("Ingrese el nombre del archivo (.csv):  ")
            print("\n1. Ver las primeras 15 filas del archivo")
            print("2. Calcular estadisticas")
            print("3. Graficar una columna completa de los datos")
            option3 = int(input("Por favor seleccione una opcion:  "))

Solicita el nombre de un archivo CSV.

Muestra un submenú específico para archivos CSV con tres opciones:
- Ver las primeras 15 filas del archivo.
- Calcular estadísticas de una columna.
- Graficar los datos de una columna.

Dependiendo de la selección, el programa llama a una de las funciones correspondientes:

#### 1. Ver Primeras 15 Filas:

        if option3 == 1:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for i in range(15):
                    print(next(reader))

Abre el archivo CSV y muestra las primeras 15 filas.

#### 2. Calcular Estadísticas:

        elif option3 == 2:
            columna = input("Por favor escriba el nombre de la columna que desea seleccionar:  ")
            calcular_estadisticas(filename, columna)


Solicita el nombre de una columna.

Llama a *calcular_estadisticas(filename, columna)*, que calcula y muestra el promedio, máximo y mínimo de la columna.

#### 3. Graficar Columna:

        elif option3 == 3:
            columna = input("Por favor escriba el nombre de la columna que desea graficar:  ")
            graficar_columna(filename, columna)

Solicita el nombre de la columna.

Llama a *graficar_columna(filename, columna)*, que grafica los datos de la columna.


#### 4. Opción Inválida:

        else:
            print("Opcion no valida")

Muestra un mensaje si la opción no es válida.


**Opción 4: Salir del Programa**

    elif option == 4:
        break

Termina el bucle while y, por ende, finaliza el programa.

---

### 4. Ejecución del Programa

    if __name__ == "__main__":
        main()


Verifica que el archivo se ejecute directamente y llama a main() para iniciar el programa.


***Esta es una explicacion detallada de cada parte del codigo, explicando su funcion y que usa para cumplir dicha funcion.***

*https://upbeduco-my.sharepoint.com/:v:/g/personal/lawrence_barrientosm_col_upb_edu_co/EdUui8WCR-pGjKuuxvHotr0BaQb9O-SzbBA4_tip4nNkKQ?e=YBPtbZ&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D*

Este es el link del video en el que se evidencia el funcionamiento del código 
