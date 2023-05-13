import os
import csv
import tkinter as tk
from tkinter import filedialog

#Utilizar Python 3.11 o superior

def browse_files():
    #Abre una ventana para que el usuario seleccione los archivos a buscar.
    files = filedialog.askopenfilenames()
    return list(files)

def browse_folder():
    #Abre una ventana para que el usuario seleccione la carpeta donde se encuentran los archiv'os.
    folder = filedialog.askdirectory()
    return folder

def search_csv(keyword, files, folder):
    # Abre el archivo resultados.csv para escritura y crea un escritor CSV
    with open(os.path.join(folder, 'resultadosCeldaExacta.csv'), 'w', newline='') as results_file:
        writer = csv.writer(results_file)
        
        # Lee la primera fila del primer archivo CSV y la agrega al archivo resultados.csv
        for file in files:
            if file.endswith('.csv'):
                with open(os.path.join(folder, file), newline='') as csv_file:
                    reader = csv.reader(csv_file)
                    for row_index, row in enumerate(reader):
                        if row_index == 0 and files.index(file) == 0:
                            writer.writerow(row)
                        # Comienza a buscar la palabra clave entre cada archivo
                        for column_index, cell in enumerate(row):
                            if keyword.lower() == cell.lower():
                                writer.writerow(row)

def search_csv2(keyword, files, folder):
    # Abre el archivo resultados.csv para escritura y crea un escritor CSV
    with open(os.path.join(folder, 'resultados.csv'), 'w', newline='') as results_file:
        writer = csv.writer(results_file)
        
        # Lee la primera fila del primer archivo CSV y la agrega al archivo resultados.csv
        for file in files:
            if file.endswith('.csv'):
                with open(os.path.join(folder, file), newline='') as csv_file:
                    reader = csv.reader(csv_file)
                    for row_index, row in enumerate(reader):
                        if row_index == 0 and files.index(file) == 0:
                            writer.writerow(row)
                        # Comienza a buscar la palabra clave entre cada archivo
                        for column_index, cell in enumerate(row):
                            if keyword.lower() in cell.lower():
                                writer.writerow(row)

def button1_clicked():
    search_label.config(text="Opción palabra en general seleccionada")
    #Ejecuta la búsqueda de la palabra clave en los archivos seleccionados.
    keyword = keyword_entry.get()
    files = browse_files()
    folder = browse_folder()
    search_csv(keyword, files, folder)
    search_label.config(text='Búsqueda completada. Resultados guardados en resultadosCeldaExacta.csv')

def button2_clicked():
    search_label.config(text="Opción palabra exacta seleccionada")
    #Ejecuta la búsqueda de la palabra clave en los archivos seleccionados.
    keyword = keyword_entry.get()
    files = browse_files()
    folder = browse_folder()
    search_csv2(keyword, files, folder)
    search_label.config(text='Búsqueda completada. Resultados guardados en resultados.csv')
                                                      
def search():
    # Crea la ventana principal
    window = tk.Tk()
    window.title("Opciones")
    window.geometry('250x100')
    option_label = tk.Label(window, text='Elige metodo de busqueda: ', padx=5, pady=5)
    option_label.pack()

    # Crea los botones y los agrega a la ventana
    button1 = tk.Button(window, text="Palabra exacta", command=button1_clicked, border=3, foreground="gray18").pack()

    button2 = tk.Button(window, text="La palabra esta en la celda", command=button2_clicked, border=3, foreground="gray18").pack()

    
# Crear la interfaz de usuario
root = tk.Tk()
root.title('Búsqueda de palabras clave en archivos CSV')
root.geometry('400x200')


# Etiqueta y entrada de la palabra a buscar por fila
keyword_label = tk.Label(root, text='Introduce la palabra a buscar por fila:', padx=15,pady=15)
keyword_label.pack()
keyword_entry = tk.Entry(root, border=3,width=30)
keyword_entry.pack()

# Botón de búsqueda
search_button = tk.Button(root, text='Buscar', command=search, border=3, foreground="gray18").pack()

# Etiqueta de resultados
search_label = tk.Label(root, text='')
search_label.pack()

root.mainloop()
