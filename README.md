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

os: Proporciona funciones para interactuar con el sistema operativo.
csv: Permite leer y escribir archivos en formato CSV.
matplotlib.pyplot: Biblioteca para crear gráficos.

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

#### Función 


