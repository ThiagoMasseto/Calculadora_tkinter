import tkinter as tk
# Importa a biblioteca Tkinter
# e dá o apelido de tk
import funcoes
# Importa o arquivo funcoes.py

janela = tk.Tk() # Cria a janela principal da aplicação
janela.title("Calculadora") # Define o título que aparece na barra superior

visor = tk.Entry(janela) # Cria o visor da calculadora
                         # onde os números serão exibidos
visor.pack() # Exibe o visor na tela

# loop de repeticao, para criação dos botões.

linha = 0
coluna = 0
for numero in range(10):
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

    botao.pack() # Exibe o botão na tela

janela.mainloop() # Mantém a janela aberta e esperando eventos
                  # como cliques e teclas