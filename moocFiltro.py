import os
import csv
import tkinter as tk
from tkinter import filedialog
from collections import defaultdict

def browse_files():
    # Abre una ventana para que el usuario seleccione los archivos a buscar.
    files = filedialog.askopenfilenames(filetypes=[("CSV files", "*.csv")])
    return list(files)

def browse_folder():
    # Abre una ventana para que el usuario seleccione la carpeta donde se guardará el archivo resultados.csv.
    folder = filedialog.askdirectory()
    return folder

def search_csv(files, folder):
    # Diccionario para almacenar qué debe cada persona junto con su fecha de entrada y correo
    pendientes = defaultdict(lambda: {'cursos': [], 'fecha': '', 'email': ''})
    
    # Itera sobre cada archivo seleccionado
    for file in files:
        if file.endswith('.csv'):
            with open(file, newline='') as csv_file:
                reader = csv.DictReader(csv_file)  # Leer CSV como diccionario para acceder por nombre de columna
                curso_name = os.path.basename(file).replace('.csv', '')  # Usar el nombre del archivo como nombre del curso
                
                for row in reader:
                    # Filtrar por 'Not Completed' o 'Open'
                    if row.get('Completion Status', row.get('declaration_status', '')).lower() in ['not completed', 'open']:  
                        
                        # Verificar si existe la columna 'Name' o 'employee_name' y asignar
                        empleado = row.get('Name', row.get('employee_name', ''))  # Usar 'Name' o 'employee_name'

                        # Obtener la fecha de entrada y el email
                        fecha_entrada = row.get('Entry Date', row.get('creation_date', ''))   # Cambiar por el nombre real de la columna
                        email = row.get('Email', row.get('employee_email', ''))# Cambiar por el nombre real de la columna

                        # Si la fecha de entrada no está ya guardada, se guarda
                        if pendientes[empleado]['fecha'] == '':
                            pendientes[empleado]['fecha'] = fecha_entrada
                        
                        # Si el correo no está ya guardado, se guarda
                        if pendientes[empleado]['email'] == '':
                            pendientes[empleado]['email'] = email
                        
                        pendientes[empleado]['cursos'].append(curso_name)

    # Guardar los resultados en un archivo CSV
    with open(os.path.join(folder, 'resultados.csv'), 'w', newline='') as results_file:
        writer = csv.writer(results_file)
        writer.writerow(['Empleado', 'Email', 'Fecha de Entrada', 'Cursos pendientes'])
        
        # Escribir los resultados
        for empleado, info in pendientes.items():
            writer.writerow([empleado, info['email'], info['fecha'], ', '.join(info['cursos'])])

def button1_clicked():
    search_label.config(text="Iniciando búsqueda de pendientes...")
    files = browse_files()
    folder = browse_folder()
    search_csv(files, folder)
    search_label.config(text='Búsqueda completada. Resultados guardados en resultados.csv')

def search():
    # Crea la ventana principal
    window = tk.Tk()
    window.title("Opciones")
    window.geometry('250x100')
    option_label = tk.Label(window, text='Búsqueda de pendientes: ', padx=5, pady=5)
    option_label.pack()

    # Crea los botones y los agrega a la ventana
    button1 = tk.Button(window, text="Iniciar búsqueda", command=button1_clicked, border=3, foreground="gray18").pack()

# Crear la interfaz de usuario
root = tk.Tk()
root.title('Búsqueda de MOOCs y ECOI pendientes en archivos CSV')
root.geometry('400x200')

# Etiqueta de resultados
search_label = tk.Label(root, text='')
search_label.pack()

# Botón de búsqueda
search_button = tk.Button(root, text='Buscar pendientes', command=search, border=3, foreground="gray18").pack()

root.mainloop()


