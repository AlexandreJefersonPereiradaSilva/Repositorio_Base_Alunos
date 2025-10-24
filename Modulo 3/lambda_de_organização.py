jogadores = [
    {'nome': 'Ratogamer', 'score': 2000, 'level': 20},
    {'nome': 'Mosquitão', 'score': 1500, 'level': 15},
    {'nome': 'Pedro_Bernadinho', 'score': 950, 'level': 12},
    {'nome': 'Afonsovisk', 'score': 785, 'level': 8},
    {'nome': 'vote_samuel_dezessete', 'score': 650, 'level': 7},
    {'nome': 'Cade_o_Lázaro', 'score': 400, 'level': 5},
]

ranking = sorted(jogadores, key=lambda jogador: jogador['score'], reverse=True)
for jogador in ranking:
    print(jogador)
