

<center><h1>Pygame Snake Game</h1></center>

# Apresentação

![Tela-Inicial](img-git/tela-inicial.jpg)

O jogo contém uma tela de início simples, podendo ser iniciado ao pressionar _SPACE_ ou _RETURN_ ou até mesmo apertando no botão verde institulado "_Play!_".

![Início](img-git/jogo.jpg)

A geração da maçã é randomizada pela função `randrange()` do módulo `random`, um módulo já presente no python, assim como o player, que se passa por uma cobra verde.

![Cobra-Grande](img-git/jogo-cobra-grande.jpg)

Cada vez que o player consome a maçã, é concedido 1 ponto para o _Score_, o qual demarca a pontuação do jogador

![Score](img-git/score.jpg)

Caso o player encoste nele mesmo, a tela de game over é exibida juntamente com a pontuação final do player. É possivel apertar a tecla "_Q_" para sair, ou a tecla "_R_" para jogar mais uma vez.

![New-Record](img-git/new-record.jpg)

Ao chegar na tela de game over do jogo, ocorre uma verificação na pasta do game procurando pelo arquivo `highscore.txt` o qual contém a pontuação máxima do usuário (em binário). Caso o jogador ultrapasse a pontuação máxima já existente, o arquivo será sobrescrito com um novo valor, quando isso ocorre é mostrado abaixo do _Score_ a mensagem "_New Record!_";

---

![](img-git/game.gif)

<span style="color:#8f8f8f">~~Sim, o developer, no caso eu, é um noob no próprio jogo, acontece...~~</span>

Os comandos são super intuitíveis, utilize" _W_ " , "_A_",  "_S_" , "_D_" para se movimentar, ou, caso prefira, utilize as famosas setinhas; "_Up_arrow_," "_Left_arrow_", "_Down_arrow_", "_Right_arrow_".



O game conta com trihas sonoras que são incríveis