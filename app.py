# cria janela
# cria visor
# cria botões
# posiciona botões

import tkinter as tk
# Importa a biblioteca Tkinter
# e dá o apelido de tk
import funcoes
# Importa o arquivo funcoes.py

janela = tk.Tk() # Cria a janela principal da aplicação
janela.title("Calculadora") # Define o título que aparece na barra superior

visor = tk.Entry(
    janela, # Cria o visor da calculadora onde os números serão exibidos
     font = ("Arial", 20), #Fonte do Texto

     justify = "right" #alinha o texto a direita igual as calculadoras reais        
            
             )

visor.grid( # Posiciona o visor usando o gerenciador de layout grid
    row = 0, # Coloca o visor na linha 0
    column=0, # Coloca o visor na coluna 0
    columnspan=3, # Faz o visor ocupar 3 colunas
    padx = 10, # Adiciona um espaçamento horizontal
    pady = 10 # Adiciona um espaçamento vertical

) # Exibe o visor na tela

# loop de repeticao, para criação dos botões.

numeros = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
    "0"
]
operadores = [
    "+", "-", "*", "/"
]

linha = 1
coluna = 0

for numero in numeros:
    botao = tk.Button(
        janela,
        text=str(numero),
        command=lambda n=numero: funcoes.clicar(visor, str(n))
    
    )
    
    botao.grid(
        row = linha,
        column= coluna
    )
    coluna +=1

    if coluna > 2 :
        coluna = 0
        linha += 1

linha =1

for operador in operadores :
    botao = tk.Button(
        janela,
        text=operador,
        width= 5 ,
        height = 2,
        command = lambda op= operador: funcoes.clicar(visor,op)
    )
    botao.grid(
        row = linha,
        column = 3,
        padx = 2,
        pady = 2
    )
    linha += 1

    botao_igual = tk.Button(
    janela,
    text="=",
    width=5,
    height=2,
    command=lambda: funcoes.calcular(visor)
)

    botao_igual.grid(
    row=5,
    column=3
    )

janela.mainloop() # Mantém a janela aberta e esperando eventos
                  # como cliques e teclas