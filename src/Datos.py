import os
import csv
import matplotlib.pyplot as plt
 
def list_files():
    print(os.listdir()) 

def count_words(filename): 
    with open(filename,'r') as file: 
        palabras = file.read().split()  
        print(len(palabras)) 

def main():
    #Tu código va aquí. Mantén la indentación
    pass # borra esta línea cuando con inicies tu código


if __name__ == "__main__":
    main()
