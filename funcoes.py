# Adiciona números e operadores ao visor
def clicar(visor, valor):

    visor.insert("end", valor)


# Limpa completamente o visor
def limpar(visor):

    visor.delete(0, "end")


# Realiza o cálculo da expressão digitada
def calcular(visor):

    conta = visor.get()

    try:

        resultado = eval(conta)

        visor.delete(0, "end")

        visor.insert("end", resultado)

    except:

        visor.delete(0, "end")

        visor.insert("end", "Erro")
