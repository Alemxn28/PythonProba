#librerias
from tkinter import *
from tkinter import messagebox
from operaciones import *
#funciones
def combinacion_grafico():
    resultado_combinacion.set(combinacion(n_combinacion.get(), k_combinacion.get()))
    messagebox.showwarning("Advertencia", "Recuerda que n debe ser mayor que k")
def permutacion_sin_repeticion_grafico():
    resultado_permutacion.set(permutacion_sin_repeticion(n_permutacion.get(), k_permutacion.get()))
    messagebox.showwarning("Advertencia", "Recuerda que n debe ser mayor que k")

def permutacion_con_permutacion():
    lista = lista_permutacion.get().split(',')
    lista_numerica = list(map(int, lista))
    resultado_permutacion_con_repeticion.set(permutacion_con_repeticion(lista_numerica))



root = Tk()
root.resizable(False, False)
root.config(bd=15)
root['bg'] = '#49A'
root.title("Combinaciones y Permutaciones")
#Variables
n_combinacion = IntVar()
k_combinacion = IntVar()
resultado_combinacion = IntVar()

n_permutacion = IntVar()
k_permutacion = IntVar()
resultado_permutacion = IntVar()

lista_permutacion = StringVar()
resultado_permutacion_con_repeticion = IntVar()

#configuracion interfaz
Label(root, text="Combinacion",bg='#49A',fg="white",font="Times 15 bold").pack()
Label(root, text="",bg='#49A',fg="white",font="Times").pack()
Label(root, text="Ingresar numero n",bg='#49A',fg="white",font="Times").pack()
Entry(root, justify="center", textvariable=n_combinacion).pack()
Label(root, text="Ingresar numero k",bg='#49A',fg="white",font="Times").pack()
Entry(root, justify="center", textvariable=k_combinacion).pack()
Label(root, text="Resultado",bg='#49A',fg="white",font="Times").pack()
Entry(root, justify="center", textvariable=resultado_combinacion, state=DISABLED).pack()
Button(root, text="Calcular", command=combinacion_grafico,fg="white",bg='#49A',font="Times").pack()

Label(root, text="",bg='#49A',fg="white",font="Times").pack()
Label(root, text="",bg='#49A',fg="white",font="Times").pack()

Label(root, text="Permutacion sin repeticion",bg='#49A',fg="white",font="Times 15 bold").pack()
Label(root, text="",bg='#49A',fg="white",font="Times").pack()
Label(root, text="Ingresar numero n",bg='#49A',fg="white",font="Times").pack()
Entry(root, justify="center", textvariable=n_permutacion).pack()
Label(root, text="Ingresar numero k",bg='#49A',fg="white",font="Times").pack()
Entry(root, justify="center", textvariable=k_permutacion).pack()
Label(root, text="Resultado",bg='#49A',fg="white",font="Times").pack()
Entry(root, justify="center", textvariable=resultado_permutacion, state=DISABLED).pack()
Button(root, text="Calcular", command=permutacion_sin_repeticion_grafico,fg="white",bg='#49A',font="Times").pack()

Label(root, text="",bg='#49A',fg="white").pack()
Label(root, text="",bg='#49A',fg="white").pack()

Label(root, text="Permutacion con repeticion",bg='#49A',fg="white",font="Times 15 bold").pack()
Label(root, text="",bg='#49A',fg="white").pack()
Label(root, text="Ingresa tus datos delimitados por comas",bg='#49A',fg="white",font="Times").pack()
Entry(root, justify="center", textvariable=lista_permutacion).pack()
Label(root, text="Resultado",bg='#49A',fg="white",font="Times").pack()


Entry(root, justify="center", textvariable=resultado_permutacion_con_repeticion, state=DISABLED).pack()
Button(root, text="Calcular", command=permutacion_con_permutacion,fg="white",bg='#49A',font="Times").pack()
root.mainloop()