Port Scanner em Python

Sobre o projeto

Essa atividade foi desenvolvida em Python com o objetivo de entender melhor como funciona a análise de portas em uma rede.

Foram criados dois códigos:

- O primeiro verifica apenas uma porta específica informada pelo usuário.
- O segundo faz uma varredura em várias portas, por exemplo da porta 1 até a 100, mostrando quais estão abertas.

Para realizar os testes, foi utilizada uma máquina virtual vulnerável chamada metasploitable 2, usada apenas em ambiente de laboratório para fins de aprendizado.

Tecnologias utilizadas
- Python
- Biblioteca `socket`
- Máquina virtual Metasploitable

Como funciona

Código 1 - Verificação de uma única porta
O usuário informa o IP do alvo e uma porta específica. O programa verifica se a porta está aberta ou fechada.

Código 2 - Scanner de múltiplas portas
O usuário informa o IP, a porta inicial e a final. O programa faz a varredura e mostra apenas as portas abertas encontradas.

Objetivo
O objetivo dessa atividade foi praticar Python, entender melhor o funcionamento das portas de rede e aprender um pouco sobre enumeração em um ambiente controlado.

Aviso
Projeto desenvolvido apenas para fins educacionais e testes em laboratório.
