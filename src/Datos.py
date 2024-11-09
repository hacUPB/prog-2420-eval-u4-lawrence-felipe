def main():

 import os
 import csv
 import matplotlib.pyplot as plt
  
 def list_files():
     print(os.listdir()) 
 
 def count_words(filename): 
     with open(filename,'r') as file: 
         palabras = file.read().split()  
         print(len(palabras)) 
 
 def replace_word(filename, palabra1, palabra2):
     with open(filename,'r') as file:
         data = file.read() 
         data = data.replace(palabra1, palabra2) 
     
     with open(filename,'w') as file: 
         file.write(data) 
     
     with open(filename,'r') as file:
         print(file.read())
 
 def count_chars(filename): 
     with open(filename,'r') as file: 
         text = file.read().strip()  
         print(len(text)) 
 
 def calcular_estadisticas(filename, columna): 
     with open(filename,'r') as file: 
         reader = csv.reader(file) 
         headers = next(reader) 
         index = headers.index(columna) 
         data = [] 
         for row in reader: 
             data.append(float(row[index])) 
         print('Promedio:', sum(data)/len(data))
         print('Maximo:', max(data)) 
         print('Minimo:', min(data))
 
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
             
 pass 
 

if __name__ == "__main__":
    main()
