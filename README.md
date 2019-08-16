# Monty Hall
Simulação do problema de Monty Hall. Desenvolvido em python.


## Problema

Monty Hall, um apresentador canadense, apresentava em seu show 'Let's Make a Deal' três portas aos participantes. Em uma das portas estava o prêmio e, nas outras duas, cabras.

- Na 1.ª etapa o concorrente escolhe uma das três portas, que ainda não é aberta
- Na 2.ª etapa, Monty abre uma das outras duas portas, sem o prêmio, que o concorrente não escolheu
- Na 3.ª etapa Monty pergunta ao concorrente se ele deseja permanecer com a porta que escolheu ou trocar para a outra porta que ainda não foi aberta.

Qual é a estratégia mais lógica? Ficar com a porta escolhida inicialmente ou mudar de porta?

Link explicativo: https://pt.wikipedia.org/wiki/Problema_de_Monty_Hall


## Solução

Embora a resposta intuitiva ao problema seja que, com a porta eliminada pelo apresentador, as chances de ganhar ao trocar ficariam em 1/2 (ou seja, não faria diferença trocar) e, portanto, o apresentador teria ajudado o participante, a porta que o apresentador abre depende da porta que o concorrente escolheu inicialmente.

Além do apresentador saber onde está o prêmio e nunca eliminar essa porta, ao abrir uma porta não premiada, ele não está criando um jogo novo, mas dando informações sobre a localização do prêmio definida no jogo inicial. Desse modo, as chances são de 2/3 e não 1/2 ao trocar de porta.


## Método

Randomizou-se a escolha inicial da porta do participante. Depois atribuiu-se, também de forma randomizada, às portas o prêmio e as cabras, de modo que apenas uma contenha a premiação. Então eliminamos uma das duas portas que não foram escolhidas pelo participante, de maneira que a porta eliminada não contenha o prêmio (no caso do participante não escolher a porta premiada).
Desse ponto, temos a escolha inicial do participante e a porta não foi eliminada, então simulamos os dois resultados possíveis, permanecer e trocar de porta, e contabilizamos os resultados.

**ALGORITHM**
```
GET randomly user's chosen door
SET values for the 3 doors (one of them has the prize)
ELIMINATE one of the two remained doors (the goat one)
ITERATE both choices (change door or keep it)
SAVE results
```


## Resultados

Conforme o número de jogos aumenta, verifica-se o aumento de 1/3 para 2/3 na quantidade de prêmios ganhos, respeitando a lei dos grandes números.

![Resultados](https://raw.githubusercontent.com/gui-h-and/montyhall/master/Results.png)


