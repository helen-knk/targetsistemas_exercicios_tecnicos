numero = int(input('Digite um número: '))

def numero_pertence_a_sequencia_de_fibonacci(numero):
    primeiro_numero = 0
    segundo_numero = 1
    numero_da_sequencia = 0
    sequencia_fibonacci = [primeiro_numero, segundo_numero]
    
    def calcula_sequencia_de_fibonacci(numero_da_sequencia, primeiro_numero, segundo_numero):
        while numero_da_sequencia < numero:
            numero_da_sequencia = primeiro_numero + segundo_numero
            primeiro_numero = segundo_numero
            segundo_numero = numero_da_sequencia
            sequencia_fibonacci.append(numero_da_sequencia)
    calcula_sequencia_de_fibonacci(numero_da_sequencia, primeiro_numero, segundo_numero)

    def verifica_se_numero_digitado_esta_na_lista(numero, sequencia_fibonacci):
        if numero in sequencia_fibonacci:
            print(f"O número {numero} pertence a sequência de Fibonacci")
        else:
            print(f"O número {numero} não pertence a sequência de Fibonacci")
    verifica_se_numero_digitado_esta_na_lista(numero, sequencia_fibonacci)

numero_pertence_a_sequencia_de_fibonacci(numero)