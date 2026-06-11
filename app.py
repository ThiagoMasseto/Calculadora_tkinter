import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")

# largura x altura
janela.geometry("300x400") # 300 pixels de largura
                           # 400 pixels de altura


visor = tk.Entry(
    janela,
    font = ("Arial", 20) # Aumenta o tamanho da letra do visor.
    )

visor.pack(
    padx=10, # Espaçamento horizontal.
    pady=10, # Espaçamento vertical.
    fill="x"
)


janela.mainloop()