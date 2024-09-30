import tkinter as tk

def adicionar():
    primeiro_numero = entrada.get()
    global f_num
    global matematica
    matematica = "adicao"
    f_num = float(primeiro_numero)
    entrada.delete(0, tk.END)

def subtrair():
    primeiro_numero = entrada.get()
    global f_num
    global matematica
    matematica = "subtracao"
    f_num = float(primeiro_numero)
    entrada.delete(0, tk.END)

def multiplicar():
    primeiro_numero = entrada.get()
    global f_num
    global matematica
    matematica = "multiplicacao"
    f_num = float(primeiro_numero)
    entrada.delete(0, tk.END)

def dividir():
    primeiro_numero = entrada.get()
    global f_num
    global matematica
    matematica = "divisao"
    f_num = float(primeiro_numero)
    entrada.delete(0, tk.END)

def igual():
    segundo_numero = entrada.get()
    entrada.delete(0, tk.END)
    if matematica == "adicao":
        entrada.insert(0, f_num + float(segundo_numero))
    if matematica == "subtracao":
        entrada.insert(0, f_num - float(segundo_numero))
    if matematica == "multiplicacao":
        entrada.insert(0, f_num * float(segundo_numero))
    if matematica == "divisao":
        entrada.insert(0, f_num / float(segundo_numero))

def botao_click(numero):
    numero_atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, str(numero_atual) + str(numero))

def botao_limpar():
    entrada.delete(0, tk.END)

root = tk.Tk()
root.title("Calculadora")

entrada = tk.Entry(root, width=16, borderwidth=5, font=('Arial', 24))
entrada.grid(row=0, column=0, columnspan=4)

botao_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: botao_click(1))
botao_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: botao_click(2))
botao_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: botao_click(3))
botao_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: botao_click(4))
botao_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: botao_click(5))
botao_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: botao_click(6))
botao_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: botao_click(7))
botao_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: botao_click(8))
botao_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: botao_click(9))
botao_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: botao_click(0))

botao_adicionar = tk.Button(root, text="+", padx=39, pady=20, command=adicionar)
botao_igual = tk.Button(root, text="=", padx=91, pady=20, command=igual)
botao_limpar = tk.Button(root, text="Limpar", padx=79, pady=20, command=botao_limpar)

botao_subtrair = tk.Button(root, text="-", padx=41, pady=20, command=subtrair)
botao_multiplicar = tk.Button(root, text="*", padx=40, pady=20, command=multiplicar)
botao_dividir = tk.Button(root, text="/", padx=41, pady=20, command=dividir)

botao_1.grid(row=3, column=0)
botao_2.grid(row=3, column=1)
botao_3.grid(row=3, column=2)

botao_4.grid(row=2, column=0)
botao_5.grid(row=2, column=1)
botao_6.grid(row=2, column=2)

botao_7.grid(row=1, column=0)
botao_8.grid(row=1, column=1)
botao_9.grid(row=1, column=2)

botao_0.grid(row=4, column=0)

botao_limpar.grid(row=4, column=1, columnspan=2)
botao_adicionar.grid(row=5, column=0)
botao_igual.grid(row=5, column=1, columnspan=2)

botao_subtrair.grid(row=6, column=0)
botao_multiplicar.grid(row=6, column=1)
botao_dividir.grid(row=6, column=2)

root.mainloop()
