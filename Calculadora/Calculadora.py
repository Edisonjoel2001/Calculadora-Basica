#Deber creacion de una calculadora basica 
   #Edison Cabezas
     #Tercer Semestre Carrera Desarrollo de Software
        #Realizar una calculadora basica

import tkinter as tk    # Creación de librerías para mostrar la interfaz gráfica
from tkinter import messagebox

# Creación de la clase calculadora
class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Básica")
        self.root.geometry("370x430")
        self.root.resizable(False, False)
        self.root.configure(bg="black")  # Fondo negro
        
        self.expresion = ""
        
        # Pantalla de resultados
        self.resultado_var = tk.StringVar()
        self.resultado_var.set("0")
        self.pantalla = tk.Entry(
            root, textvariable=self.resultado_var, font=("Castellar", 20), bd=10, insertwidth=2, 
            width=14, justify="right", bg="black", fg="white"
        )
        self.pantalla.grid(row=0, column=0, columnspan=4, pady=10)
        
        # Creación de los botones
        botones = [
            "7", "8", "9", "÷",
            "4", "5", "6", "×",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]
        
        fila = 1
        columna = 0
        
        for boton in botones:
            comando = lambda x=boton: self.on_click(x)
            color_fondo = "red" if boton in "÷×-+=C" else "black"  # Operadores y "C" en rojo
            color_texto = "white" if boton in "÷×-+=C" else "white"  # Texto blanco en todos
            
            tk.Button(
                root, text=boton, padx=20, pady=20, font=("Castellar", 15), 
                bg=color_fondo, fg=color_texto, command=comando, bd=2
            ).grid(row=fila, column=columna, padx=5, pady=5)
            
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1
    
    def on_click(self, boton):
        if boton.isdigit() or boton in "÷×-+":
            if self.expresion == "0" and boton.isdigit():
                self.expresion = boton
            else:
                self.expresion += boton.replace("÷", "/").replace("×", "*")
            self.resultado_var.set(self.expresion)
        elif boton == "=":
            try:
                resultado = eval(self.expresion)
                self.resultado_var.set(str(round(resultado, 10)))
                self.expresion = str(resultado)
            except ZeroDivisionError:
                messagebox.showerror("Error", "No puedes dividir entre 0")
                self.resultado_var.set("0")
                self.expresion = ""
            except Exception:
                messagebox.showerror("Error", "Número inválido")
                self.resultado_var.set("0")
                self.expresion = ""
        elif boton == "C":
            self.expresion = ""
            self.resultado_var.set("0")

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()

