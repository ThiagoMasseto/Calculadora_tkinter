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

# Cria um botão com o texto "1"
botao1 = tk.Button( 

    janela,  # Define a janela onde o botão será colocado
    text="1", # Texto exibido no botão
    command=lambda: funcoes.clicar(visor, "1")  # Quando clicar no botão:
                                                # chama a função clicar()
                                                # passando o visor e o número 1
)

botao1.pack() # Exibe o botão na tela

janela.mainloop() # Mantém a janela aberta e esperando eventos
                  # como cliques e teclas