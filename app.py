import tkinter as tk
import funcoes

janela = tk.Tk()

visor = tk.Entry(janela)
visor.pack()

botao1 = tk.Button(
    janela,
    text="1",
    command=lambda: funcoes.clicar(visor, "1")
)

botao1.pack()

janela.mainloop()