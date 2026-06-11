import tkinter as tk
import funcoes

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Tamanho inicial da janela
janela.geometry("400x400")

# Faz a única célula da janela expandir
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

# Frame que conterá toda a calculadora
frame = tk.Frame(janela)

# Centraliza o frame na janela
frame.grid(row=0, column=0)

# ==========================
# VISOR
# ==========================

visor = tk.Entry(
    frame,
    font=("Arial", 20),
    justify="right"
)

visor.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=10,
    sticky="ew"
)

# ==========================
# BOTÕES NUMÉRICOS
# ==========================

numeros = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
    "0"
]

linha = 1
coluna = 0

for numero in numeros:

    botao = tk.Button(
        frame,
        text=numero,
        width=5,
        height=2,
        command=lambda n=numero: funcoes.clicar(visor, n)
    )

    botao.grid(
        row=linha,
        column=coluna,
        padx=2,
        pady=2
    )

    coluna += 1

    if coluna > 2:
        coluna = 0
        linha += 1

# ==========================
# OPERADORES
# ==========================

operadores = ["+", "-", "*", "/"]

linha = 1

for operador in operadores:

    botao = tk.Button(
        frame,
        text=operador,
        width=5,
        height=2,
        command=lambda op=operador: funcoes.clicar(visor, op)
    )

    botao.grid(
        row=linha,
        column=3,
        padx=2,
        pady=2
    )

    linha += 1

# ==========================
# BOTÃO IGUAL
# ==========================

botao_igual = tk.Button(
    frame,
    text="=",
    width=5,
    height=2,
    command=lambda: funcoes.calcular(visor)
)

botao_igual.grid(
    row=5,
    column=3,
    padx=2,
    pady=2
)

janela.mainloop()