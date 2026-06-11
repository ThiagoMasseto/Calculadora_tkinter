# Função responsável por adicionar um número
# ou operador no visor da calculadora

def clicar(visor, numero):
    visor.insert("end", numero)

    # Insere o valor recebido no final do texto
    # que já existe no visor

def limpar(visor):
    visor.delete(0, "end")
    # Função para limpar completamente o visor
    # Apaga do primeiro caractere (posição 0)
    # até o final do conteúdo

def calcular(visor): # Função responsável por realizar o cálculo
    conta = visor.get()
     # Obtém o texto que está escrito no visor

    try:
        resultado = eval(conta)
        # eval() interpreta a string como uma expressão matemática
        # Exemplo: "5+5" vira 10

        visor.delete(0, "end") # Limpa o visor antes de mostrar o resultado
        visor.insert("end", resultado) # Exibe o resultado encontrado

    except:
        # Caso aconteça algum erro
        # Exemplo: "5++" ou divisão inválida
        
        visor.delete(0, "end") # Limpa o visor
        
        visor.insert("end", "Erro") # Mostra a mensagem de erro

def calcular(visor): #Realiza o calculo da expressão digitada

    # Obtém o conteúdo do visor
    conta = visor.get()

    try: 
        #executa a expressão matemática
        resultado = eval(conta)

        #Limpa o visor
        visor.delete(0, "end")

        #Exibe o resultado
        visor.insert("end", resultado)

    except:

        #Se ocorrer algum erro
        visor.delete(0, "end")
        visor.insert("end", "Erro")