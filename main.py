import tkinter as tk
from tkinter import messagebox
import random

def aceptar_20():
    messagebox.showinfo("¡Evaluación Exitosa!", "¡Gracias profe! Git dominado, repo subido al 100% y el 20 asegurado. 😎")

def esquivar_boton(event):
    nuevo_x = random.randint(10, 300)
    nuevo_y = random.randint(10, 200)
    btn_no.place(x=nuevo_x, y=nuevo_y)

def click_trampa():
    messagebox.showwarning("Error del Sistema", "Opción 'Desaprobar' no disponible en este momento. Intente con el botón verde.")

ventana = tk.Tk()
ventana.title("Proyecto Lab 05-A - Omar Sebastian")
ventana.geometry("450x300")
ventana.configure(bg="#f0f0f0")

etiqueta = tk.Label(ventana, text="¡Profeee, póngame 20 por favor! 🥺", font=("Arial", 16, "bold"), bg="#f0f0f0")
etiqueta.pack(pady=40)

btn_si = tk.Button(ventana, text="¡Claro que sí, toma tu 20!", bg="lightgreen", font=("Arial", 12), command=aceptar_20)
btn_si.place(x=50, y=120)

btn_no = tk.Button(ventana, text="Mmm, le falta", bg="salmon", font=("Arial", 12), command=click_trampa)
btn_no.place(x=280, y=120)
btn_no.bind("<Enter>", esquivar_boton)

ventana.mainloop()