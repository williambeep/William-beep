import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        if altura <= 0:
            messagebox.showerror("Error", "La altura debe ser mayor a cero.")
            return
        
        imc = peso / (altura ** 2)

        if imc < 18.5:
            categoria = "Peso bajo"
        elif imc < 25:
            categoria = "Peso normal"
        elif imc < 30:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidad"

        label_resultado.config(text=f"IMC: {imc:.2f} - {categoria}")

    except:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de IMC")
ventana.geometry("300x200")

# Peso
tk.Label(ventana, text="Peso (kg):").pack()
entry_peso = tk.Entry(ventana)
entry_peso.pack()

# Altura
tk.Label(ventana, text="Altura (m):").pack()
entry_altura = tk.Entry(ventana)
entry_altura.pack()

# Botón
boton_calcular = tk.Button(ventana, text="Calcular IMC", command=calcular_imc)
boton_calcular.pack()

# Resultado
label_resultado = tk.Label(ventana, text="", fg="blue")
label_resultado.pack(pady=10)

ventana.mainloop()