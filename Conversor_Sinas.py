import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Conversor Sinas")
root.geometry("500x600")

frase_principal = tk.Label(root, text="Escolha o tipo de conversão", font=("Georgia", 15))
frase_principal.pack(pady=10)

escolha_usuario = tk.StringVar(value="1")

tk.Radiobutton(root, text="Decimal para Binário", variable=escolha_usuario, value="1", font=("Georgia", 15)).pack()
tk.Radiobutton(root, text="Decimal para Octal", variable=escolha_usuario, value="2", font=("Georgia", 15)).pack()
tk.Radiobutton(root, text="Decimal para Hexadecimal", variable=escolha_usuario, value="3", font=("Georgia", 15)).pack()
tk.Radiobutton(root, text="Binário para Octal", variable=escolha_usuario, value="4", font=("Georgia", 15)).pack()
tk.Radiobutton(root, text="Binário para Decimal", variable=escolha_usuario, value="5", font=("Georgia", 15)).pack()
tk.Radiobutton(root, text="Binário para Hexadecimal", variable=escolha_usuario, value="6", font=("Georgia", 15)).pack()
tk.Radiobutton(root, text="Octal para Binário", variable=escolha_usuario, value="7", font=("Georgia", 15)).pack()
tk.Radiobutton(root, text="Octal para Decimal", variable=escolha_usuario, value="8", font=("Georgia", 15)).pack()
tk.Radiobutton(root, text="Octal para Hexadecimal", variable=escolha_usuario, value="9", font=("Georgia", 15)).pack()
tk.Radiobutton(root, text="Hexadecimal para Binário", variable=escolha_usuario, value="10", font=("Georgia", 15)).pack()
tk.Radiobutton(root, text="Hexadecimal para Octal", variable=escolha_usuario, value="11", font=("Georgia", 15)).pack()
tk.Radiobutton(root, text="Hexadecimal para Decimal", variable=escolha_usuario, value="12", font=("Georgia", 15)).pack()

entrada = tk.Entry(root, font=("Arial", 15), width=20)
entrada.pack(pady=10)

def decimal_para_binario(decimal): ## ESCOLHA 1
    try:
        valor_binario = bin(int(decimal))[2:]
        return valor_binario
    except ValueError:
        return None

def decimal_para_octal(decimal): ## ESCOLHA 2
    try:
        valor_octal = oct(decimal)[2:]
        return valor_octal
    except ValueError:
        return None
    
def decimal_para_hexadecimal(decimal): ## ESCOLHA 3
    try:
        decimal = int(decimal)
        valor_hexadecimal = hex(decimal)[2:].upper()
        return valor_hexadecimal
    except ValueError:
        return None

def binario_para_octal(binario): ## ESCOLHA 4
    try:
        valor_decimal = int(binario, 2)
        valor_octal = oct(valor_decimal)[2:]
        return valor_octal
    except ValueError:
        return None

def binario_para_decimal(binario): ## ESCOLHA 5
    try:
        valor_decimal = int(binario, 2)
        return valor_decimal
    except ValueError:
        return None
    
def binario_para_hexadecimal(binario): ## ESCOLHA 6
    try:
        valor_decimal = int(binario, 2)
        valor_hexadecimal = hex(valor_decimal)[2:].upper()
        return valor_hexadecimal
    except ValueError:
        return None

def octal_para_binário(octal): ## ESCOLHA 7
    try:
        valor_decimal = int(octal, 8)
        valor_binario = bin(valor_decimal)[2:]
        return valor_binario
    except ValueError:
        return None

def octal_para_decimal(octal): ## ESCOLHA 8
    try:
        valor_decimal = int(octal, 8)
        return valor_decimal
    except ValueError:
        return None
    
def octal_para_hexadecimal(octal): ## ESCOLHA 9
    try:
        valor_decimal = int(octal, 8)
        valor_hexadecimal = hex(valor_decimal)[2:].upper()
        return valor_hexadecimal
    except ValueError:
        return None

def hexadecimal_para_binario(hexadecimal): ## ESCOLHA 10
    try:    
        valor_decimal = int(hexadecimal, 16)
        valor_binario = bin(valor_decimal)[2:]
        return valor_binario
    except ValueError:
        return None

def hexadecimal_para_octal(hexadecimal): ## ESCOLHA 11
    try:
        valor_decimal = int(hexadecimal, 16)
        valor_octal = oct(valor_decimal)[2:]
        return valor_octal
    except ValueError:
        return None

def hexadecimal_para_decimal(hexadecimal): ## ESCOLHA 12
    try:
        valor_decimal = int(hexadecimal,16)
        return valor_decimal
    except ValueError:
        return None

def conversor():
    numero_inserido = entrada.get()
    
    if escolha_usuario.get() == "1":
        resultado = decimal_para_binario(numero_inserido)
        if resultado is not None:
            messagebox.showinfo("Resultado", f"Valor em Binário: {resultado}")
        else:
            messagebox.showerror("Erro", "Por favor, insira um numero válido")
    
    if escolha_usuario.get() == "2":
        resultado = decimal_para_octal(numero_inserido)
        if resultado is not None:
            messagebox.showinfo("Resultado", f"Valor em Octal: {resultado}")
        else:
            messagebox.showerror("Erro", "Por favor, insira um numero válido")

    if escolha_usuario.get() == "3":
        resultado = decimal_para_hexadecimal(numero_inserido)
        if resultado is not None:
            messagebox.showinfo("Resultado", f"Valor em Hexadecimal: {resultado}")
        else:
            messagebox.showerror("Erro", "Por favor, insira um numero válido")

    elif escolha_usuario.get() == "4":
        resultado = binario_para_octal(numero_inserido)
        if resultado is not None:
            messagebox.showinfo("Resultado", f"Valor em Octal: {resultado}")
        else:
            messagebox.showerror("Erro", "Insira um valor válido!")

    elif escolha_usuario.get() == "5":
        resultado = binario_para_decimal(numero_inserido)
        if resultado is not None:
            messagebox.showinfo("Resultado", f"Valor em decimal: {resultado}")
        else:
            messagebox.showerror("Erro", "Por favor insira um número válido")

    elif escolha_usuario.get() == "6":
        resultado = binario_para_hexadecimal(numero_inserido)
        if resultado is not None:
            messagebox.showinfo("Resultado", f"Valor em Hexadecimal: {resultado}")
        else:
            messagebox.showerror("Erro", "Insira um valor válido!")

    elif escolha_usuario.get() == "7":
        resultado = octal_para_binário(numero_inserido)
        if resultado is not None:
            messagebox.showinfo("Resultado", f"Valor em Binário: {resultado}")
        else:
            messagebox.showerror("Erro", "Insira um valor válido!")
    
    elif escolha_usuario.get() == "8":
        resultado = octal_para_decimal(numero_inserido)
        if resultado is not None:
            messagebox.showinfo("Resultado", f"Valor em Decimal: {resultado}")
        else:
            messagebox.showerror("Erro", "Insira um valor válido!")
    
    elif escolha_usuario.get() == "9":
        resultado = octal_para_hexadecimal(numero_inserido)
        if resultado is not None:
            messagebox.showinfo("Resultado", f"Valor em Hexadecimal: {resultado}")
        else:
            messagebox.showerror("Erro", "Insira um valor válido!")

    elif escolha_usuario.get() == "10":
        resultado = hexadecimal_para_binario(numero_inserido)
        if resultado is not None:
            messagebox.showinfo("Resultado", f"Valor em Binário: {resultado}")
        else:
            messagebox.showerror("Erro", "Insira um valor válido!")

    elif escolha_usuario.get() == "11":
        resultado = hexadecimal_para_octal(numero_inserido)
        if resultado is not None:
            messagebox.showinfo("Resultado", f"Valor em Octal: {resultado}")
        else:
            messagebox.showerror("Erro", "Insira um valor válido!")

    elif escolha_usuario.get() == "12":
        resultado = hexadecimal_para_decimal(numero_inserido)
        if resultado is not None:
            messagebox.showinfo("Resultado", f"Valor em Hexadecimal: {resultado}")
        else:
            messagebox.showerror("Erro", "Insira um valor válido!")

botao = tk.Button(root, text="Converter", command=conversor, font=("Georgia",15), width=15, height=2)
botao.pack(pady=10)

root.mainloop() 