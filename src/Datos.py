def main():

 import os
 import csv
 import matplotlib.pyplot as plt
  
 def list_files():
     print(os.listdir()) #imprime una lista de los archivos contenidos en el directorio actual
 
 def count_words(filename): #funcion que toma como argumento el nombre del archivo
     with open(filename,'r') as file: #abre el archivo como solo lectura
         palabras = file.read().split()  #lee todo el archivo y lo divide en palabras como una lista
         print(len(palabras)) #cuenta el numero de palabras en la lista y lo imprime
 
 def replace_word(filename, palabra1, palabra2):  #-funcion que toma como argumento el nombre del archivo y dos palabras
     with open(filename,'r') as file: #abre el archivo como solo lectura
         data = file.read() #lee todo el archivo y lo guarda en la variable data
         data = data.replace(palabra1, palabra2) #reemplaza la palabra1 por la palabra2 con la funcion replace()
     
     with open(filename,'w') as file: #abre el archivo para sobreescribirlo
         file.write(data) #escribe el contenido de la variable data en el archivo
     
     with open(filename,'r') as file: #abre el archivo como solo lectura
         print(file.read()) #-imprime el contenido del archivo con la palabra cambiada
 
 def count_chars(filename): #funcion que toma como argumento el nombre del archivo
     with open(filename,'r') as file: #abre el archivo como solo lectura
         text = file.read().strip()  #lee todo el archivo y le quita los espacios blancos 
         print(len(text)) #cuenta el numero de caracteres en el archivo y lo imprime
 
 def calcular_estadisticas(filename, columna): #-funcion que toma como argumento el nombre del archivo y el nombre de la columna
     with open(filename,'r') as file: #abre el archivo como solo lectura
         reader = csv.reader(file) #lee el archivo como un archivo csv
         headers = next(reader) #guarda la primera fila del archivo en la variable headers
         index = headers.index(columna) #busca el indice de la columna en la lista headers
         data = [] #crea una lista vacia
         for row in reader: #itera sobre las filas del archivo
             data.append(float(row[index])) #agrega el valor de la columna a la lista data
         print('Promedio:', sum(data)/len(data)) #imprime el promedio de los valores de la lista data
         print('Maximo:', max(data)) #imprime el valor maximo de la lista data
         print('Minimo:', min(data)) #-imprime el valor minimo de la lista data
 
 def graficar_columna(filename, columna): 
     with open(filename,'r') as file: 
         reader = csv.reader(file) 
         headers = next(reader) 
         index = headers.index(columna) 
         data = [] 
         for row in reader: 
             data.append(float(row[index])) 
        
         plt.plot(data) 
         plt.show() 

 
 def main():
     while True:
         print('Bienvenido!')
         print('\n')
         print('1. Ver archivos en la ruta actual')
         print('2. Archivo de texto (.txt)')
         print('3. Archivo CSV (.csv)')
         print('4. Salirse del programa')
         option = int(input('Por favor seleccione una opcion:'))
 
         if option == 1:
             list_files()
         elif option == 2:
             filename = input('Ingrese el nombre del archivo (.txt):  ')
             print('\n')
             print('1. Contar numero de palabras')
             print('2. Reemplazar una palabra por otra')
             print('3. Contar el numero de caracteres')
             option2 = int(input('Por favor seleccione una opcion:  '))
 
             if option2 == 1:
                 count_words(filename)
             elif option2 == 2:
                 palabra1 = input('Por favor escriba la palabra que desea reemplazar:  ')
                 palabra2 = input('Por favor escriba la palabra por la que quiere reemplazar:  ')
                 replace_word(filename, palabra1, palabra2)
             elif option2 == 3:
                 count_chars(filename)
             else:
                 print('Opcion no valida')
 
         elif option == 3:
             filename = input('Ingrese el nombre del archivo (.csv):  ')
             print('\n')
             print('1. Ver las primeras 15 filas del archivo')
             print('2. Calcular estadisticas')
             print('3. Graficar una columna completa de los datos')
             option3 = int(input('Por favor seleccione una opcion:  '))
             
             if option3 == 1:
                 with open(filename,'r') as file:
                     reader = csv.reader(file)
                     for i in range(15):
                         print(next(reader))
 
             elif option3 == 2:
                 columna = input('Por favor escriba el nombre de la columna que desea seleccionar:  ')
                 calcular_estadisticas(filename, columna)
                 
             elif option3 == 3:
                 columna = input('Por favor escriba el nombre de la columna que desea graficar:  ')
                 graficar_columna(filename, columna)
             
             else:
                 print('Opcion no valida')
         
         elif option == 4:
             break
         else:
             print('Opcion no valida')

if __name__ == "__main__":
    main()
