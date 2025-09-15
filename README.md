Forca em Python

Um simples jogo de forca criado em Python. O jogador pode escolher entre diferentes temas e níveis de dificuldade para adivinhar a palavra secreta.

Funcionalidades

    Vários Temas: Escolha entre jogos, filmes, desenhos, celebridades mundiais e brasileiras.

    Níveis de Dificuldade: Jogue nos modos Fácil, Médio, Difícil ou Experto, que ajustam o comprimento da palavra a ser adivinhada.

    Pontuação e Sequência: O jogo acompanha sua pontuação e uma sequência de acertos.

    Interface de Linha de Comando: Totalmente jogável no terminal.

    Sair a Qualquer Momento: Digite --sair para encerrar o programa a qualquer momento.

Como Jogar

    Requisitos: Você só precisa ter o Python 3 instalado no seu sistema.

    Executar o Script: Abra seu terminal ou prompt de comando, navegue até o diretório onde o arquivo está salvo e execute o seguinte comando:
    Bash

    python nome_do_arquivo.py

    (Substitua nome_do_arquivo.py pelo nome que você salvou o script).

    Escolha o Nível e o Tema: O jogo irá pedir para você escolher um nível de dificuldade e um tema.

    Adivinhe a Palavra: Digite uma letra por vez ou a palavra inteira para tentar adivinhar a palavra secreta.

Comandos Especiais

    --sair: Encerra o jogo a qualquer momento.

Estrutura do Código

    opcoes e temas: Listas e dicionários que contêm os temas e as palavras.

    limpa(): Uma função para limpar a tela do terminal, mantendo a interface organizada.

    valida_numerico(): Uma função que garante que a entrada do usuário seja um número dentro de um intervalo válido.

    JogoForca (Classe): A classe principal do jogo, que lida com toda a lógica:

        __init__: Inicializa o jogo com o tema e a dificuldade escolhidos.

        __get_palavra_secreta(): Seleciona uma palavra aleatória com base no tema e na dificuldade.

        __imprime_tela(): Desenha a forca e exibe o estado atual do jogo.

        __processa_jogada(): Lida com a entrada do usuário e atualiza o estado do jogo.

        __verifica_vitoria() e __verifica_fim_do_jogo(): Verifica se o jogador ganhou ou perdeu.

        jogar(): O loop principal do jogo.

    main(): A função principal que inicia o jogo e gerencia a seleção de tema e dificuldade.
