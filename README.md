# Exercício 1 :

* O código está apresentado na linguagem de programação Python, 
calculando a soma do número 1 ao 13, 
sendo que no próximo número, soma-se ao anterior,
parando a soma quando chega ao número 13.


# Exercício 2 :

* Importei o módulo math para utilizar a função sqrt(), onde me daria uma
  resposta de ter um número com quadrado perfeito;
* Fiz 2 variáveis referentes ao valor a e ao valor b,
  para não ter repetição de calculo.

# Exercício 3 :

* Criei o arquivo JSON com a lista de faturamento diário;
* Pedi para abrir o arquivo em modo leitura e carregar os dados contidos, criando uma variável,
  para fácil acesso durante o desenvolvimento do código;
* Através da função json.load(), transformei o texto obtido no arquivo para Python
  para fácil manipulação;
* Usei a condição  if dia["valor"] > 0 para o código não acrescentar os
  dias em que o faturamento fosse 0;
* Com as funções min() e max() foi calculado a média de ambos, no total mensal;
* Usei a expressão sum(1 for valor in faturamento_diario if valor > media_faturamento)
  para mostrar quantos dias o faturamento ficou acima da média;
* E por fim, pedi para imprimir todos os resultados, retirando as casas decimais
  após a vírgula.


# Exercício 4 :

  * Precisando calcular o faturamento com a porcentagem de cada estado,
    usei um código simples e direto;
  * E mais uma vez para imprimir, fiz a retirada das casas decimais,
    através do .format.


# Exercício 5 :

  * Utilizei a função reversed() para inverter os caracteres;
  * E na hora de imprimir, usei 2 prints para visualizar a string em estado normal
    e outro invertida.
