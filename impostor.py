import random

cartas = [
    # 1 de Elixir
    "Espírito de Fogo",
    "Espírito de Gelo",
    "Espírito Elétrico",
    "Espírito Curativo",
    "larrys",
    

    # 2 de Elixir
    "Goblins",
    "goblins lanceiros",
    "Morcegos",
    "Bombardeiro",
    "Zap",
    "Barril de Bárbaro",
    "bola de neve",
    "berseker",
    "golen de gelo",
    "tronco",
    "destuidor de muros",
    "furia",
    "maldição goblin",
    "arbusto",


    # 3 de Elixir
    "Cavaleiro",
    "arqueiras",
    "servos",
    "flechas",
    "lapide",
    "canhão",
    "megaservo",
    "barril de goblins",
    "vinhas",
    "barril de esqueletos",
    "princessa",
    "mineiro",
    "pirocatecnica",
    "terremoto",
    "mago de gelo",
    "fantasma real",
    "bandida",
    "encomenda real",
    "golem de elixir",
    "vacuo",
    "pescador",
    "pequeno principe",
    "Goblin com Dardo",
    "Gangue de Goblins",
    "Guardas",
    "Exército de Esqueletos",
    "Clone",
    "tornado",
    
    

    # 4 de Elixir
    "Valquíria",
    "Mini P.E.K.K.A",
    "Mosqueteira",
    "Máquina Voadora",
    "Corredor",
    "Caçador",
    "Tesla",
    "cabana de goblins",
    "P. diddy",
    "bola de fogo",
    "ariete",
    "dragao esqueleto",
    "torre bombas",
    "morteiro",
    "bebe dragao",
    "principe das trevas",
    "curadora",
    "gelo",
    "gigante das runas",
    "veneno",
    "eletrocuutadores",
    "fornalha",
    "dragao infernal",
    "mago eletrico",
    "goblin demolidor",
    "fenix",
    "arqueiro magico",
    "escavadeira de goblins",
    "lenhador",
    "bruxa sombria",
    "bruxa mâe",
    "rei esqueleto",
    "cavaleiro dourado",
    "mineiro bombado",


    # 5 de Elixir
    "Mago",
    "barbaros",
    "porcos reais",
    "horda de servos",
    "domadora",
    "dragão eletrico",
    "patifes",
    "lançador",
    "executor",
    "Bruxa",
    "Balão",
    "Gigante",
    "Príncipe",
    "Canhão com Rodas",
    "Cemitério",
    "Torre Inferno",
    "maquina goblin",
    "rainha arqueira",
    "monge",
    "goblinstein",


    # 6 de Elixir
    "Gigante Real",
    "Esqueleto Gigante",
    "Relâmpago",
    "foguete",
    "cabana de barbaros",
    "goblin gigante",
    "barbaros de elite",
    "xbesta",
    "sparky",
    "coletor de elixir",
    "imperatriz espiritual",
    "bandida lider",


    # 7 de Elixir
    "P.E.K.K.A",
    "Megacavaleiro",
    "recrutas reais",
    "gigante eletrico",
    "lava hound",

    # 8+ de Elixir
    "golem",
    "3 mosqueteira",
    "espelho",
]


carta = random.choice(cartas)

teste = 1
numero = int(input("Digite o número de jogadores: "))

impostor = random.randint(1, numero)

print(input("Pressione ENTER para começar"))

while teste <= numero:
    input(f"Jogador {teste}, aperte ENTER para ver sua carta")

    if teste == impostor:
        print("🔥 VOCÊ É O IMPOSTOR 🔥")
    else:
    
        print("🃏 Sua carta é:", carta)

    input("Pressione ENTER para passar para o próximo jogador")
    print("\n" * 50)  # limpa a tela (gambiarra)
    teste += 1

começar = random.randint(1, numero)

teste = 1

while teste <= numero:
    if teste == começar:
        print("o jogador", teste, "começará a rodada")
        teste += 1
        
    else:
        teste = teste + 1
        
    