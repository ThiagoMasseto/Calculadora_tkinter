import tkinter as tk
import customtkinter as ctk
import funcoes

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

COR_AZUL = "#29B6F6"

# Cria a janela principal
janela = ctk.CTk()
janela.title("Calculadora")

# Tamanho inicial da janela
janela.geometry("400x400")

# Faz a única célula da janela expandir
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

# Frame que conterá toda a calculadora
frame = ctk.CTkFrame(
    janela,
    corner_radius = 15
    )

# Centraliza o frame na janela
frame.grid(row=0, column=0)

# ==========================
# Título
# ==========================

titulo = ctk.CTkLabel(
    frame,
    text="Calculadora do Masseto 🎰",
    font=("Arial", 30, "bold"),
    text_color=COR_AZUL
)

titulo.grid(
    row=0,
    column=0,
    columnspan = 4,
    pady = (20, 10)
)

# ==========================
# VISOR
# ==========================

visor = ctk.CTkEntry(
    frame,
    font=("Arial", 20),
    justify="right",
    width=420
)

visor.grid(
    row=1,
    column=0,
    columnspan=4,
    padx=20,
    pady=20,
    sticky="ew"
    
)

# Dá foco ao visor após a janela ser carregada
janela.after(100, lambda: visor.focus_set())

# ==========================
# BOTÕES NUMÉRICOS
# ==========================

numeros = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
    "0"
]

linha = 2
coluna = 0

for numero in numeros:

    botao = ctk.CTkButton(
    frame,
    text=numero,
    width=80,
    height=60,

    corner_radius=15,

    fg_color="transparent",
    border_width=2,
    border_color=COR_AZUL,

    text_color=COR_AZUL,

    command=lambda n=numero: funcoes.clicar(visor, n)
)

    botao.grid(
        row=linha,
        column=coluna,
        padx=4,
        pady=4
    )

    coluna += 1

    if coluna > 2:
        coluna = 0
        linha += 1

# ==========================
# OPERADORES
# ==========================

operadores = ["+", "-", "*", "/"]

linha = 3

for operador in operadores:

    botao = ctk.CTkButton(
    frame,
    text=operador,
    width=80,
    height=60,

    corner_radius=15,

    fg_color=COR_AZUL,

    text_color="white",

    command=lambda op=operador: funcoes.clicar(visor, op)
)

    botao.grid(
        row=linha,
        column=3,
        padx=4,
        pady=4
    )

    linha += 1

# ==========================
# BOTÃO IGUAL
# ==========================

botao_igual = ctk.CTkButton(
    frame,
    text="=",
    width=80,
    height=60,

    corner_radius=15,

    fg_color=COR_AZUL,
    hover_color="#0288D1",

    command=lambda: funcoes.calcular(visor)
)

botao_igual.grid(
    row=6,
    column=3,
    padx=4,
    pady=4
)

janela.bind(
    "<Return>",
    lambda evento: funcoes.calcular(visor)
)

janela.bind(
    "<Escape>",
    lambda evento: funcoes.limpar(visor)
)

# ==========================
# BOTÃO AC
# ==========================

botao_ac = ctk.CTkButton(
    frame,
    text="AC",
    width=80,
    height=60,

    corner_radius=15,

    fg_color="#EF5350",
    hover_color="#E53935",

    command=lambda: funcoes.limpar(visor)
)

botao_ac.grid(
    row=2,
    column=0,
    padx=4,
    pady=4
)

janela.mainloop()