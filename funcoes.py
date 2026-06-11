# Função responsável por adicionar um número
# ou operador no visor da calculadora
def clicar(visor, numero):
    visor.insert("end", numero)

def limpar(visor):
    visor.delete(0, "end")

def calcular(visor):
    conta = visor.get()

    try:
        resultado = eval(conta)

        visor.delete(0, "end")
        visor.insert("end", resultado)

    except:
        visor.delete(0, "end")
        visor.insert("end", "Erro")