import random,  sys

class Monster():
    def __init__(self, name, type, atk, defesa, hp):
        self.name = name
        self.type = type
        self.ataque = int(atk)
        self.defesa = int(defesa)
        self.hp = int(hp)
        self.atacante = False
        self.defensor = False
        self.mode = ''

    def show_statistics(self):
        x = ' '
        print(f"{f'Nome: {self.name}': ^{window_size}}")
        print(f"{f'HP: {self.hp}': ^{window_size}}")
        print(f"{f'Ataque: {self.ataque}': ^{window_size}}")
        print(f"{f'Defesa: {self.defesa}': ^{window_size}}")
        print(f"{f'Tipo: {self.type}': ^{window_size}}")
        print(f"{'----------': ^{window_size}}")

    def terreno(self, tipo_do_terreno):
        self.terreno_type = tipo_do_terreno
        if self.terreno_type == 'Vulcão':
            if self.type == 'fogo':
                self.ataque += 100
        if self.terreno_type == 'Lago':
            if self.type == 'água':
                self.ataque += 100
        if self.terreno_type == 'Floresta':
            if self.type == 'planta':
                self.ataque += 100
        if self.terreno_type == 'Templo celestial':
            if self.type == 'luz':
                self.ataque += 100
        if self.terreno_type == 'Domínio do caos':
            if self.type == 'trevaz':
                self.ataque += 100
        if self.terreno_type == 'Terra dos ventos':
            if self.type == 'ar':
                self.ataque += 100
        if self.terreno_type == 'Tempestade':
            if self.type == 'elétrico':
                self.ataque += 100
        if self.terreno_type == 'Montanhas valentes':
            if self.type == 'terra':
                self.ataque += 100


    def update(self):
        self.show_statistics()

blaster = Monster('Blaster', 'fogo', 1200, 1300, 5000)
infernape = Monster('Infernape', 'fogo', 1500, 1600, 5000)
blastoise = Monster('Blastoise', 'planta', 1700, 1400, 5000)
m1 = Monster('m1', 'luz', 1500, 1300, 5000)
m2 = Monster('m2', 'água', 1500, 1000, 5000)

players_list = []
players_namelist = []
players_list.extend([blaster, infernape, blastoise, m1, m2])
players_namelist.extend(['Blaster', 'Infernape', 'Blastoise', 'm1', 'm2'])

vida = 1
dano = 0
terreno_e = '23232'
window_size = 60
x = ' '
y = '-'
linhas_tela = y * window_size
espaço_tela = x * window_size
voltar = True

def show_monstros():
    show_monsters = False
    activate_sm = input('Deseja ver a lista de monstros? (s/n): ')
    if activate_sm == 's':
        blaster.show_statistics()
        infernape.show_statistics()
        blastoise.show_statistics()
        m1.show_statistics()
        m2.show_statistics()
    elif activate_sm == 'n':
        pass
    else:
        pass
    return show_monsters

def terreno():
    global terreno_e
    terreno_lista = ['Vulcão','Floresta','Lago','Templo celestial','Domínio do caos','Terra dos ventos','Tempestade','Montanhas valentes']
    escolha = random.randint(0, len(terreno_lista) - 1)
    terreno_e = terreno_lista[escolha]
    # terreno_e = 'Lago'
    print(x)
    print(linhas_tela)
    print(f"{f'O terreno foi mudado para {terreno_e}': ^{window_size}}")
    match terreno_e:
        case 'Vulcão': print(f"{'Os ataques dos monstros de tipo fogo foram aumentados': ^{window_size}}")

        case 'Floresta': print(f"{'Os ataques dos monstros de tipo planta foram aumentados': ^{window_size}}")
        case 'Lago': print(f"{'Os ataques dos monstros de tipo água foram aumentados': ^{window_size}}")
    print(linhas_tela)
    return terreno_lista, escolha

def escolha_monstros():
    global p1, p2, batalha_l, players_namelist, player_in_battle_list
    print(f"{'-----ESCOLHA DE MONSTROS-----': ^{window_size}}")
    print(linhas_tela)
    p1 = input('Escolha o primeiro player 1: ')

    if players_namelist.count(p1) >= 1:
        p2 = input('Escolha o primeiro player 2: ')
        if players_namelist.count(p2) >= 1:
            # print('\n', '--------', '\n')
            print(f"{'--------': ^{window_size}},'\n'")
            player_in_battle_list = [p1, p2]
            batalha_l = 'on'
        else:
            print(f"{'Monstro não existente, escolha novamente ataca': ^{window_size}}")
            batalha_l = 'off'
    else:
        print(f"{'Monstro não existente, escolha novamente ataca': ^{window_size}}")
        batalha_l = 'off'
    print(linhas_tela)

def escolha_ad():
    global p_ataca, p_defende
    print(linhas_tela)
    p_ataca = input('Quem irá atacar? ')
    p_defende = input('Quem irá defender? ')

def escolha_modo():
    global p_ataca, p_defende, player, players_list, pname, player_atacante, player_defensor, escolha_errada, voltar

    for player in players_list:
        pname = player.name
        if pname == p_ataca:
            print('Player atacante: ', player.name)
            player_atacante = player
            if player_atacante == player:
                voltar = False
            else:
                voltar = True
        if pname == p_defende:
            print('Player defensor: ', player.name)
            player_defensor = player
            if player_defensor == player:
                voltar = False
            else:
                voltar = True


    print(linhas_tela)

def c_efetivo(dano, player_atacante, player_defensor, window_size):
    #checa se o tioo e efetivo
    if player_atacante.ataque > player_defensor.defesa:
        dano += (player_atacante.ataque - player_defensor.defesa) * 4
        player_defensor.hp -= dano
        print(f"{'ATAQUE SUPER EFETIVO': ^{window_size}}", '\n')

    elif player_atacante.ataque < player_defensor.defesa:
        dano += abs(player_atacante.ataque - player_defensor.defesa) / 100
        if dano >= 5000:
            dano += 50
        elif dano >= 4000:
            dano += 60
        elif dano >= 3000:
            dano += 70
        elif dano >= 2000:
            dano += 80
        elif dano >= 1000:
            dano += 90
        elif dano > 0:
            dano += 100
        player_defensor.defesa -= dano
        player_atacante.ataque -= dano
        print('Ataque efetivo surtiu efeito na defesa do oponente', '\n')

    elif player_atacante.ataque == player_defensor.defesa:
        dano += 100
        player_defensor.defesa -= dano
        print('Ataque efetivo surtiu efeito na defesa do oponente', '\n')

def c_igual(dano, player_atacante, player_defensor, window_size):
    if player_atacante.ataque > player_defensor.defesa:
        dano += (player_atacante.ataque - player_defensor.defesa) / 4
        player_defensor.hp -= int(dano)
        player_defensor.ataque += 50
        print(f"{'ATAQUE POUCO EFETIVO': ^{window_size}}", '\n')
        print(f"{'O ATAQUE DO OPONENTE FOI AUMENTADO': ^{window_size}}", '\n')
    elif player_atacante.ataque < player_defensor.defesa:
        dano += 50
        player_atacante.defesa -= dano
        player_defensor.ataque += 50
        print('Defesa do atacante foi diminuída')
        print('Ataque do oponente foi aumentado', '\n')
    elif player_atacante.ataque == player_defensor.defesa:
         dano += 25
         player_defensor.defesa -= dano
         player_defensor.ataque += dano
         print('Defesa do oponente foi diminuída', '\n')
         print('Ataque do oponente foi aumentado', '\n')

    return dano, player_atacante, player_defensor, window_size

def c_diferente(dano, player_atacante, player_defensor, window_size):
    if player_atacante.ataque > player_defensor.defesa:
        dano += (player_atacante.ataque - player_defensor.defesa)
        player_defensor.hp -= dano
        print(f"{'ATAQUE SURTIU EFEITO': ^{window_size}}", '\n')

    elif player_atacante.ataque < player_defensor.defesa:
        dano += abs(player_atacante.ataque - player_defensor.defesa) / 100
        if dano >= 5000:
            dano += 25
        elif dano >= 4000:
            dano += 30
        elif dano >= 3000:
            dano += 35
        elif dano >= 2000:
            dano += 40
        elif dano >= 1000:
            dano += 45
        elif dano > 0:
            dano += 50
        player_defensor.defesa -= int(dano)
        player_atacante.ataque -= int(dano)
        print('Ataque surtiu efeito na defesa do oponente', '\n')

    elif player_atacante.ataque == player_defensor.defesa:
        dano += 50
        player_defensor.defesa -= dano
        print('Ataque surtiu efeito na defesa do oponente', '\n')

def batalha():
    global vida, dano

    print(linhas_tela)
    #cheque para ataque maior que defesa
    if player_atacante.ataque > player_defensor.defesa:
        match player_atacante.type:
            #vantagens e desvantagens do fogo
            case 'fogo':
                match player_defensor.type:
                    case 'fogo':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'trevaz':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'planta':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens de planata
            case 'planta':
                match player_defensor.type:
                    case 'planta':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'água':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'luz':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'terra':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens do água
            case 'água':
                match player_defensor.type:
                    case 'água':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'fogo':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens de luz
            case 'luz':
                match player_defensor.type:
                    case 'luz':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'trevaz':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens do trevaz
            case 'trevaz':
                match player_defensor.type:
                    case 'trevaz':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'planta':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens do ar
            case 'ar':
                match player_defensor.type:
                    case 'ar':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'fogo':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens do elétrico
            case 'elétrico':
                match player_defensor.type:
                    case 'elétrico':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'água':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'trevaz':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens da terra
            case 'terra':
                match player_defensor.type:
                    case 'terra':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'ar':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'elétrico':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)

    #cheque para ataque menor que defesa
    elif player_atacante.ataque < player_defensor.defesa:
        match player_atacante.type:
            # vantagens e desvantagens do fogo
            case 'fogo':
                match player_defensor.type:
                    case 'fogo':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'trevaz':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'planta':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens de planata
            case 'planta':
                match player_defensor.type:
                    case 'planta':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'água':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'luz':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'terra':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens do água
            case 'água':
                match player_defensor.type:
                    case 'água':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'fogo':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens de luz
            case 'luz':
                match player_defensor.type:
                    case 'luz':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'trevaz':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens do trevaz
            case 'trevaz':
                match player_defensor.type:
                    case 'trevaz':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'planta':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens do ar
            case 'ar':
                match player_defensor.type:
                    case 'ar':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'fogo':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens do elétrico
            case 'elétrico':
                match player_defensor.type:
                    case 'elétrico':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'água':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'trevaz':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens da terra
            case 'terra':
                match player_defensor.type:
                    case 'terra':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'ar':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'elétrico':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)


    #cheque para ataque igual a defesa
    elif player_atacante.ataque == player_defensor.defesa:
        match player_atacante.type:
            # vantagens e desvantagens do fogo
            case 'fogo':
                match player_defensor.type:
                    case 'fogo':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'trevaz':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'planta':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens de planata
            case 'planta':
                match player_defensor.type:
                    case 'planta':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'água':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'luz':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'terra':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens do água
            case 'água':
                match player_defensor.type:
                    case 'água':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'fogo':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens de luz
            case 'luz':
                match player_defensor.type:
                    case 'luz':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'trevaz':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens do trevaz
            case 'trevaz':
                match player_defensor.type:
                    case 'trevaz':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'planta':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens do ar
            case 'ar':
                match player_defensor.type:
                    case 'ar':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'fogo':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens do elétrico
            case 'elétrico':
                match player_defensor.type:
                    case 'elétrico':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'água':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'trevaz':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)
            # vantagens e desvantagens da terra
            case 'terra':
                match player_defensor.type:
                    case 'terra':
                        c_igual(dano, player_atacante, player_defensor, window_size)
                    case 'ar':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case 'elétrico':
                        c_efetivo(dano, player_atacante, player_defensor, window_size)
                    case other:
                        c_diferente(dano, player_atacante, player_defensor, window_size)


    #checa se o hp chegou a zero
    if player_defensor.hp <= 0 or player_atacante.hp <= 0:
        vida == 0
        player_defensor.hp = 0
        vida -= 1
        print('Player', player_defensor.name, 'derrotado')
        print('Player', player_atacante.name, 'VENCEU!!')

    print(linhas_tela)
    print('Estatisticas dos monstros')
    player_atacante.show_statistics()
    player_defensor.show_statistics()
    print(linhas_tela)
    dano = 0
    return player_defensor, player_atacante

t_escolhido = ''
batalha_l = 'else'
run = True
while run:

    if batalha_l == 'else':
        show_monstros()
        terreno()
        batalha_l = 'off'
    if vida > 0:
        if batalha_l == 'off':
            escolha_monstros()
        if batalha_l == 'on':
            for player in players_list:
                pname = player.name
                if pname == p1:
                    player.terreno(terreno_e)
                    player.show_statistics()
                if pname == p2:
                    player.terreno(terreno_e)
                    player.show_statistics()
            while vida >= 1:
                escolha_ad()
                escolha_modo()
                if voltar:
                    escolha_ad()
                    escolha_modo()
                else:
                    print('False', voltar)
                    player_atacante.terreno(terreno_e)
                    player_defensor.terreno(terreno_e)
                    print('Estatisticas dos monstros')
                    player_atacante.show_statistics()
                    player_defensor.show_statistics()
                    batalha()
    elif vida <= 0:
        run == False


print('\n', '---FIM---', '\n')