# Target sistemas - Teste técnico (etapa 2)

## Questões
1. Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
    
    > _IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;_

    [Solução](https://github.com/helen-knk/targetsistemas_exercicios_tecnicos/blob/master/01_sequencia_de_fibonacci/main.py)

---

2. Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

    > _IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;_

    [Solução](https://github.com/helen-knk/targetsistemas_exercicios_tecnicos/blob/master/02_verifica_a_existencia_da_letra_na_palavra_digitada/main.py)

---

3. Observe o trecho de código abaixo: 
```
int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
```

Ao final do processamento, qual será o valor da variável SOMA? <br>
_R:_ O resultado final será 77. O código executado em python [encontra-se aqui.](https://github.com/helen-knk/targetsistemas_exercicios_tecnicos/blob/master/03_soma_valores_na_variavel/main.py)

---

4. Descubra a lógica e complete o próximo elemento: <br>
    > _Observação: Essa etapa do teste, não possui código desenvolvido por conta que está baseado em raciocínio lógico._<br>

    a. 1, 3, 5, 7, ___ <br>
    _R:_ Lógica de obter somente os números impares, sendo o último número da listagem igual a 9. 

    b. 2, 4, 8, 16, 32, 64, ____ <br>
    _R:_ Lógica de multiplicar o número por 2, obtendo o próximo número da listagem. O último número da listagem é 128.

    c. 0, 1, 4, 9, 16, 25, 36, ____ <br>
    _R:_ Soma o número da sequência pelo próximo número ímpar, sendo o último número da listagem igual a 49.

    d. 4, 16, 36, 64, ____
    _R:_ Para obter o próximo número da sequência, o número par é elevado ao quadrado, sendo o último número da sequência é 100.

    e. 1, 1, 2, 3, 5, 8, ____ <br>
    _R:_ Lógica de Fibonacci, pois somando o elemento anterior, 1, com 1, é possível obter o próximo número sendo 2. E assim sucessivamente, o último número da listagem é 13.
 
    f. 2, 10, 12, 16, 17, 18, 19, ____ <br>
    _R:_ Todos os números da sequência começam com a letra D, o prócimo número é 200 (Duzentos).

---

5. Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

    > _Observação: Essa etapa do teste, não possui código desenvolvido por conta que está baseado em raciocínio lógico._<br>

    _R:_ Na sala onde estão os três interruptores, ligamos o interruptor 1 por 15 minutos, e desligamos, e em seguida ligamos o interruptor 2 e vamos até as salas. A lâmpada que estiver acesa corresponde ao interruptor 2, a que estiver quente ao interruptor 1, e a lâmpada que resta é a do interruptor 3.