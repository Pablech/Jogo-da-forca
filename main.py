from random import choice as r
import os
import sys

opcoes = [
    'jogos',
    'filmes',
    'desenhos',
    'celebridades_mundiais',
    'celebridades_brasileiras'
]
temas = {
    'jogos': [
        "Minecraft", "Fortnite", "GTA V", "Valorant", "League of Legends",
        "FIFA 25", "Call of Duty", "Cyberpunk 2077", "The Witcher 3", "God of War",
        "Red Dead", "Zelda", "Super Mario", "Pokémon", "Assassin's Creed",
        "Halo", "Doom", "Resident Evil", "Street Fighter", "Mortal Kombat",
        "Tekken", "Among Us", "Fall Guys", "Overwatch 2", "Apex Legends",
        "Genshin Impact", "Free Fire", "PUBG", "Battlefield", "Far Cry",
        "Elder Scrolls", "Diablo IV", "Starcraft II", "World of Warcraft",
        "Counter-Strike 2", "Rocket League", "Ark", "Rust", "Terraria",
        "Starbound", "Hades", "Celeste", "Hollow Knight", "Cuphead",
        "Ori e a Floresta", "Sea of Thieves", "For Honor", "Rainbow Six",
        "Warframe", "Destiny 2", "Borderlands", "Bioshock", "Fallout 4",
        "The Last of Us", "Uncharted", "Horizon Zero", "Spider-Man",
        "God of War Ragnarok", "Elden Ring", "Dark Souls", "Bloodborne",
        "Sekiro", "Persona 5", "Final Fantasy", "Dragon Quest", "Nier Automata",
        "Death Stranding", "Ghost of Tsushima", "Control", "Alan Wake",
        "Max Payne", "Dishonored", "Prey", "Wolfenstein", "Disco Elysium",
        "RimWorld", "Factorio", "Cities Skylines", "Civilization VI",
        "Crusader Kings 3", "Hearts of Iron IV", "Europa Universalis IV",
        "Stellaris", "Mount & Blade II", "Valheim", "Grounded", "Subnautica",
        "Satisfactory", "Astroneer", "No Man's Sky", "Starfield",
        "Baldur's Gate 3", "Divinity Original Sin 2", "Pillars of Eternity",
        "Outer Wilds", "Returnal", "Kena: Bridge of Spirits"
    ],
    'filmes': [
        "A Origem", "Matrix", "O Poderoso Chefão", "Clube da Luta", "Pulp Fiction",
        "Forrest Gump", "A Vida é Bela", "Parasita", "Interestelar", "Gladiador",
        "O Cavaleiro das Trevas", "O Senhor dos Anéis", "Django Livre", "A Chegada",
        "O Grande Lebowski", "Guerra nas Estrelas", "Blade Runner", "O Iluminado",
        "Um Sonho de Liberdade", "A Lista de Schindler", "Alien, o 8º Passageiro",
        "De Volta Para o Futuro", "Psicose", "O Sexto Sentido", "O Silêncio dos Inocentes",
        "Taxi Driver", "Laranja Mecânica", "Brilho Eterno", "Bastardos Inglórios",
        "Amelie Poulain", "Cidade de Deus", "O Fabuloso Destino", "Central do Brasil",
        "Tropa de Elite", "Bacurau", "O Auto da Compadecida", "Vidas Secas",
        "O Pagador de Promessas", "Cinema Paradiso", "A Viagem de Chihiro",
        "Princesa Mononoke", "O Castelo Animado", "Meu Vizinho Totoro", "Akira",
        "A Bruxa", "Hereditário", "Corra!", "Nós", "Um Lugar Silencioso",
        "O Segredo dos Seus Olhos", "Roma", "O Labirinto do Fauno", "Em Busca da Felicidade",
        "O Resgate do Soldado Ryan", "Top Gun", "Rambo", "Indiana Jones", "Mad Max",
        "Exterminador do Futuro", "Rocky", "Robocop", "Duro de Matar", "O Predador",
        "Os Caça-Fantasmas", "Jurassic Park", "Tubarão", "E.T.", "Ghostbusters",
        "Beetlejuice", "Os Goonies", "Edward Mãos de Tesoura", "A Noiva Cadáver",
        "O Estranho Mundo", "Mary e Max", "Wall-E", "Up – Altas Aventuras",
        "Divertidamente", "Toy Story", "Procurando Nemo", "Os Incríveis", "Monstros S.A.",
        "Coco", "Soul", "Encanto", "Raya", "Luca", "Elementos", "Pânico", "O Grito",
        "Invocação do Mal", "Annabelle", "A Freira", "A Maldição da Residência Hill",
        "O Exorcista", "Poltergeist", "O Chamado", "Seven", "Zodíaco", "Garota Exemplar",
        "O Clube da Luta"
    ],
    'desenhos': [
        "os simpsons", "futurama", "south park", "family guy",
        "rick and morty", "bojack horseman", "avatar: a lenda de aang",
        "avatar: a lenda de korra", "a turma da mônica", "o show da luna!",
        "gumball", "apenas um show", "hora de aventura", "steven universo",
        "as meninas superpoderosas", "o laboratório de dexter",
        "samurai jack", "coragem, o cão covarde", "ben 10",
        "jovens titãs em ação!", "jovens titãs", "scooby-doo, cadê você?",
        "tom e jerry", "pernalonga e amigos", "pato donald",
        "mickey mouse", "ursinhos carinhosos", "os smurfs",
        "he-man e os mestres do universo", "she-ra: a princesa do poder",
        "thundercats", "caverna do dragão", "x-men",
        "homem-aranha", "batman", "liga da justiça",
        "dragon ball z", "pokémon", "digimon", "naruto", "one piece",
        "death note", "attack on titan", "fullmetal alchemist: brotherhood",
        "a viagem de chihiro", "princesa mononoke", "meu vizinho totoro",
        "kimi no na wa (your name.)", "a voz do silêncio", "looney tunes",
        "flintstones", "os jetsons", "mr. bean",
        "o inspetor bugiganga", "sonic x", "castlevania", "disenchantment",
        "big mouth", "glitch techs", "kipo e os anjos incríveis",
        "she-ra e as princesas do poder", "voltron: o defensor lendário",
        "trollhunters", "os 3 lá em baixo",
        "caçadores de trolls: contos de arcadia", "os anjinhos",
        "hey arnold!", "rocko's modern life", "ducktales (2017)",
        "gravity falls: um verão de mistérios", "star vs. as forças do mal",
        "amphibia", "the owl house", "shera and the princesses of power",
        "infinity train", "genndy tartakovsky's primal",
        "love, death & robots", "arcane", "cyberpunk: edgerunners",
        "invincible", "os incríveis", "procurando nemo",
        "up: altas aventuras", "divertidamente", "coco", "soul", "encanto",
        "frozen", "moana", "shrek", "madagascar",
        "como treinar seu dragão", "kung fu panda", "a era do gelo",
        "minions", "meu malvado favorito", "o homem-aranha no aranhaverso",
        "ponyo: uma amizade que veio do mar", "contos da terra natal",
        "kim possible", "o segredo além do jardim", "phineas e ferb",
        "garfield e seus amigos", "o fantastico mundo de bob",
        "a família addams (animado)", "o urso pooh"
    ],
    'celebridades_mundiais': [
        "leonardo dicaprio", "jennifer lawrence", "brad pitt",
        "angelina jolie", "beyoncé knowles", "jay-z carter",
        "taylor swift", "rihanna fenty", "dwayne the rock johnson",
        "oprah winfrey", "elon musk", "bill gates", "jeff bezos",
        "mark zuckerberg", "kim kardashian", "kylie jenner",
        "justin bieber", "selena gomez", "ariana grande", "ed sheeran",
        "adele adkins", "chris hemsworth", "chris evans",
        "scarlett johansson", "robert downey jr.", "tom cruise",
        "meryl streep", "tom hanks", "julia roberts", "george clooney",
        "will smith", "cristiano ronaldo", "lionel messi",
        "roger federer", "serena williams", "michael jordan",
        "lebron james", "lady gaga", "bruno mars", "dua lipa",
        "billie eilish", "harry styles", "zendaya coleman",
        "timothée chalamet", "margot robbie", "ryan gosling",
        "emma stone", "ryan reynolds", "blake lively", "gigi hadid",
        "kendall jenner", "bella hadid", "natalie portman",
        "keanu reeves", "sandra bullock", "hugh jackman", "gal gadot",
        "jason momoa", "nicole kidman", "russell crowe", "kate winslet",
        "emma watson", "daniel radcliffe", "rupert grint",
        "anne hathaway", "charlize theron", "chris pratt", "chris pine",
        "ana de armas", "florence pugh", "jeremy renner", "paul rudd",
        "mark ruffalo", "elizabeth olsen", "tom holland",
        "jake gyllenhaal", "hugh grant", "colin firth", "judi dench",
        "ian mckellen", "patrick stewart", "morgan freeman",
        "malala yousafzai", "greta thunberg", "barack obama",
        "michelle obama", "donald trump", "joe biden", "xi jinping",
        "vladimir putin", "angela merkel", "emmanuel macron",
        "justin trudeau", "príncipe harry", "meghan markle",
        "príncipe william", "kate middleton", "rainha camilla",
        "rei charles iii", "papa francisco", "dalai lama",
        "greta gerwig", "christopher nolan", "quentin tarantino",
        "martin scorsese"
    ],
    'celebridades_brasileiras': [
        "gil do vigor", "juliette freire", "anitta", "ivete sangalo",
        "luan santana", "marília mendonça", "gusttavo lima",
        "paulo gustavo", "tata werneck", "fábio porchat",
        "leandro hassum", "fernanda montenegro", "gloria pires",
        "antônio fagundes", "regina duarte", "adriana esteves",
        "cauã reymond", "bruna marquezine", "marina ruy barbosa",
        "isis valverde", "sabrina sato", "eliana", "luciano huck",
        "faustão", "silvio santos", "gugu liberato", "xuxa meneghel",
        "angelica ksyvickis", "pelé", "neymar jr.",
        "marta vieira da silva", "gabriel medina", "ronaldo nazário",
        "ronaldinho gaúcho", "adriano imperador", "fenômeno",
        "daniel alves", "thiago silva", "alisson becker", "casemiro",
        "vini jr.", "gabriel jesus", "roberto carlos", "cafu", "alok",
        "vintage culture", "anavitória", "melim", "tiago iorc", "vitão",
        "luísa sonza", "lexa", "iza", "pabllo vittar", "gloria groove",
        "liniker", "manu gavassi", "bianca andrade",
        "whindersson nunes", "felipe neto", "carlinhos maia",
        "virginia fonseca", "zé felipe", "tirullipa", "tiririca",
        "danilo gentili", "rafinha bastos", "murilo couto",
        "sergio malandro", "dedé santana", "renato aragão", "zacarias",
        "mussum", "didi mocó", "chico anísio", "jô soares",
        "claudia raia", "edson celulari", "cláudia abreu",
        "glória menezes", "tarcísio meira", "fernanda torres",
        "selton mello", "ricardo tozzi", "malvino salvador",
        "isis de oliveira", "josé wilker", "vera holtz", "arlete sales",
        "cássia kiss", "letícia sabatella", "carmo dalla vecchia",
        "alexandre nero", "larissa manoela", "maisa silva",
        "klebber toledo", "camila queiroz", "rafa vitti", "caio castro",
        "marcelo serrado", "rodrigo faro", "cris dias",
        "paolla oliveira", "juliana paes"
    ]
}

nivel = '''
    Ecolha o nível

    Fácil   - 1
    médio   - 2
    Difícil - 3
    Experto - 4
    Ou --sair para sair
'''

tema = '''
    Escolha um tema

    Jogos           - 1
    Filmes          - 2
    Desenhos        - 3
    Celebridades    - 4
    celebridades BR - 5
    Voltar          - 0
    Ou --sair para sair
'''


def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')


def encerra_programa():
    print('Programa encerrado')
    sys.exit(0)


def valida_numerico(val_min, val_max, mensagem):
    while True:
        limpa()
        try:
            entrada_str = input(f'{mensagem}\n>>> ')
            if entrada_str == '--sair':
                encerra_programa()
            entrada = int(entrada_str)
            if val_min <= entrada <= val_max:
                return entrada
            print(f'\aDigite um valor entre {val_min} e {val_max} ou --sair para sair.')
        except KeyboardInterrupt:
            print('\a\nDigite --sair para encerrar o programa')
        except ValueError:
            print('\aDigite apenas números ou --sair para sair.\n')

        input("Pressione Enter para continuar...")


class JogoForca:
    def __init__(self, tema, dificuldade):
        self.__tema = opcoes[tema - 1]
        self.__dificuldade = dificuldade
        self.__palavra_secreta = self.__get_palavra_secreta()
        self.__letras_corretas = set()
        self.__letras_digitadas = set()
        self.__erros = 0
        self.__acertos = 0
        self.__pontos = 0
        self.__sequencia = 0
        self.__boneco = ['\t |', '\t°>°', '\t/', '|', '\\', '\t/', '"', '\\']

    def __get_comprimento_palavra(self):
        if self.__dificuldade == 1:
            return 0, 4
        if self.__dificuldade == 2:
            return 5, 7
        if self.__dificuldade == 3:
            return 8, 10
        if self.__dificuldade == 4:
            return 11, 100
        return 0, 100

    def __get_palavra_secreta(self):
        palavras_tema = temas[self.__tema]
        min_len, max_len = self.__get_comprimento_palavra()

        while True:
            palavra = r(palavras_tema)
            if min_len <= len(palavra) <= max_len:
                return palavra

    def __imprime_tela(self):
        limpa()
        print(f'Tema: {self.__tema.replace("_", " ").title()}')
        print(f'A palavra tem {len(self.__palavra_secreta)} caracteres')
        print(f'Erros: {self.__erros} de 7')
        print(f'Acertos: {self.__acertos} de {len(self.__palavra_secreta)}')
        print(f'Sequência: {self.__sequencia} {'\U0001F629' if self.__sequencia == 0 else '\U0001F60B'}')
        print(f'Pontos: {self.__pontos}')
        print('Digite --sair a qualquer momento para encerrar o programa')

        exibir = [
            letra if letra in self.__letras_corretas else '_'
            for letra in self.__palavra_secreta
        ]
        print()
        print(' '.join(exibir))
        print(''.join(self.__boneco[i] + ('\n' if i not in [2, 3, 5, 6] else '') for i in range(self.__erros + 1)))

    def __processa_jogada(self, letra):
        if letra in self.__palavra_secreta:
            for l in letra:
                for carectere in self.__palavra_secreta:
                    if carectere == l:
                        self.__acertos += 1
                        self.__letras_corretas.add(l)
                        self.__sequencia += 1
                        self.__pontos += (self.__sequencia + 0.5) * 10
        else:
            self.__erros += 1
            self.__sequencia = 0
            self.__pontos -= 10

    def __verifica_vitoria(self):
        return set(self.__palavra_secreta) <= self.__letras_corretas

    def __verifica_fim_do_jogo(self):
        if self.__erros >= 7:
            print(f'Você perdeu a palavra era {self.__palavra_secreta}\nPontos: {self.__pontos}')
            return True
        if self.__verifica_vitoria():
            print(f'Você ganhou a palavra era {self.__palavra_secreta}\nPontos: {self.__pontos}')
            return True
        return False

    @staticmethod
    def __jogar_novamente():
        terminar = input('Jogar novamente (s/n)\n>>> ').lower()
        if terminar == 's':
            main()
        else:
            encerra_programa()

    def jogar(self):
        tamanho_palavra = len(self.__palavra_secreta)
        while True:
            self.__imprime_tela()
            try:
                jogada = input('Digite uma letra\n>>> ')

                if jogada == '--sair':
                    encerra_programa()

                if not jogada:
                    print(f'\aEntrada inválida <{jogada}>')
                    continue

                if 1 < len(jogada) < tamanho_palavra:
                    print('\aDigite apenas uma letra, um caracter\nou tente adivinhar a palavra inteira')
                    continue

                if len(jogada) > tamanho_palavra:
                    print(f'\a{jogada} excede o tamanho da palavra, jogada inválida')
                    continue

                if len(jogada) == tamanho_palavra:
                    self.__processa_jogada(jogada)
                    if self.__verifica_fim_do_jogo():
                        break
                    else:
                        print(f'Você errou, a palavra era {self.__palavra_secreta}')
                        self.__erros = 7
                        break

                if jogada in self.__letras_digitadas:
                    print(f'\aJá digitou a letra {jogada}')
                    continue
                self.__letras_digitadas.add(jogada)
                self.__processa_jogada(jogada)

                if self.__verifica_fim_do_jogo():
                    break
            except KeyboardInterrupt:
                print('\a\nDigite --sair para encerrar o programa')
                continue
        self.__jogar_novamente()


def main():
    while True:
        limpa()
        dificuldade = valida_numerico(val_min=1, val_max=4, mensagem=nivel)
        if dificuldade == 0:
            encerra_programa()
        limpa()
        tema_escolhido = valida_numerico(val_min=0, val_max=5, mensagem=tema)
        if tema_escolhido == 0:
            continue
        limpa()
        jogo = JogoForca(tema_escolhido, dificuldade)
        jogo.jogar()


if __name__ == '__main__':
    main()
