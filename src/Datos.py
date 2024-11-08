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
def main():
    #Tu código va aquí. Mantén la indentación
    pass # borra esta línea cuando con inicies tu código


if __name__ == "__main__":
    main()
