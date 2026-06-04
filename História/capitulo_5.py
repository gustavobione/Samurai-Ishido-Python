# capitulo_5.py
import layout
import sistemas
import random

# ==========================================
# FUNÇÃO AUXILIAR DE PROVAÇÕES
# ==========================================
def provacao_narrativa(jogador, numero, nome, atributo, dificuldade, dano, texto_intro, texto_sucesso, texto_falha):
    """Executa provações rápidas mantendo a densidade e punindo falhas brutalmente."""
    if jogador["vitalidade"] <= 0: return False
    
    layout.divisoria()
    layout.imprimir_lento(f"[bold]Provação {numero}/13: {nome}[/bold]\n{texto_intro}")
    layout.esperar_enter(f"[dim]Pressione Enter para testar {atributo.capitalize()} (Dificuldade {dificuldade})...[/dim]")
    
    if sistemas.rolar_teste(jogador, atributo, dificuldade):
        layout.imprimir_lento(f"[green]{texto_sucesso}[/green]")
        return True
    else:
        layout.imprimir_lento(f"[red]{texto_falha}[/red]")
        jogador["vitalidade"] -= dano
        layout.console.print(f"[bold red]-{dano} HP.[/bold red]")
        return False

# ==========================================
# ROTA 1: A ALA SANGRENTA (O CAMINHO DA GUERRA)
# Foco: Combates brutais, resistência física e armadilhas de cerco.
# ==========================================
def rota_ala_sangrenta(jogador):
    layout.cabecalho("A ALA SANGRENTA", "O Bastião da Carnificina")
    layout.imprimir_lento(
        "Você arromba os portões da esquerda. O cheiro de ferro e sangue velho é sufocante. "
        "Esta era a antiga ala militar do seu clã, agora transformada num abatedouro contínuo "
        "onde os Ashigarus de Kuroi treinam massacrando prisioneiros. O caminho até o topo será pavimentado em corpos."
    )
    
    # 1. Armadilha de Cerco
    provacao_narrativa(jogador, 1, "O Fosso de Lanças", "destreza", 18, 10,
        "Assim que você pisa no corredor, o chão cede. Lanças de obsidiana emergem do fosso escuro.",
        "Seus reflexos são sobre-humanos. Você pisa na ponta de uma lança ascendente e salta para a borda segura.",
        "Uma das lanças rasga sua coxa antes de você conseguir rolar para fora do fosso!")

    # 2. O Muro de Escudos
    provacao_narrativa(jogador, 2, "A Falange Morta", "kenjutsu", 20, 12,
        "Um esquadrão de esqueletos com escudos de torre bloqueia o corredor, avançando lentamente em formação cerrada.",
        "O Sol Negro derrete os escudos de ferro como manteiga, abrindo caminho em um único giro de Nitoryu.",
        "O impacto com os escudos repele seu ataque, e eles o esmagam com a parede de ferro antes de você recuar!")
        
    if jogador["vitalidade"] <= 0: return jogador

    # 3. Combate 1
    layout.divisoria()
    layout.imprimir_lento("[bold]Provação 3/13: O Capitão Sanguinário[/bold]\nUm demônio de três metros com duas clavas de espinhos surge rindo da escuridão.")
    sistemas.iniciar_combate(jogador, "Capitão Corrompido", hp_inimigo=60, defesa_inimigo=15, min_dano=6, max_dano=12, xp_recompensa=50, fraqueza="Gelo", resistencia="Físico")
    if jogador["vitalidade"] <= 0: return jogador

    # 4. Gás Alucinógeno
    provacao_narrativa(jogador, 4, "A Névoa da Loucura", "conhecimento", 19, 8,
        "Os dutos de ar expelem uma fumaça roxa. O gás ferve o sangue e induz o guerreiro a atacar a si mesmo.",
        "Você prende a respiração e reconhece o padrão do feitiço, meditando em movimento até passar a zona de perigo.",
        "Você inala o gás. As alucinações fazem você cortar o próprio braço em confusão antes de sair do transe!")

    # 5. A Passagem Secreta
    layout.divisoria()
    layout.imprimir_lento("[bold]Provação 5/13: A Passagem Oculta[/bold]")
    layout.imprimir_lento("Para evitar um batalhão inteiro marchando no pátio inferior, você busca uma rota pelas paredes internas.")
    layout.console.print("[white]1 - [Destreza Dificuldade 21][/white] Escalar o poço do elevador de carga.")
    layout.console.print("[white]2 - [Conhecimento Dificuldade 18][/white] Encontrar o tijolo solto da arquitetura antiga Shiro.")
    layout.limpar_buffer_teclado()
    if input("Escolha (1 ou 2): ").strip() == "2":
        if sistemas.rolar_teste(jogador, "conhecimento", 18): layout.imprimir_lento("[green]Você acha o mecanismo escondido e passa ileso.[/green]")
        else: 
            layout.imprimir_lento("[red]Você não acha a passagem e atrai a atenção de patrulheiros![/red]")
            jogador["vitalidade"] -= 10
    else:
        if sistemas.rolar_teste(jogador, "destreza", 21): layout.imprimir_lento("[green]Sua força física o carrega poço acima em silêncio.[/green]")
        else: 
            layout.imprimir_lento("[red]A corda arrebenta e você despenca, machucando a coluna.[/red]")
            jogador["vitalidade"] -= 10
            
    if jogador["vitalidade"] <= 0: return jogador

    # 6 a 11 - A Escadaria Contínua (Combates em horda)
    layout.divisoria()
    layout.imprimir_lento(
        "[bold]Provações 6 a 11: A Escadaria do Triunfo[/bold]\n"
        "Você chega à Espiral Interminável. Aqui, não há furtividade. Não há fuga. "
        "Apenas onda após onda de horrores que descem os degraus para impedi-lo de subir. "
        "A Arte do Eclipse será posta à prova máxima."
    )
    layout.esperar_enter("[dim]Pressione Enter para iniciar a chacina...[/dim]")
    
    sistemas.iniciar_combate(jogador, "Horda de Rastejantes", hp_inimigo=70, defesa_inimigo=13, min_dano=5, max_dano=10, xp_recompensa=40, fraqueza="Gelo", resistencia="Nenhuma")
    if jogador["vitalidade"] <= 0: return jogador
    sistemas.iniciar_combate(jogador, "Samurais Sem Cabeça", hp_inimigo=80, defesa_inimigo=16, min_dano=6, max_dano=11, xp_recompensa=60, fraqueza="Físico", resistencia="Fogo")
    if jogador["vitalidade"] <= 0: return jogador

    # 12. A Ponte Colapsando
    provacao_narrativa(jogador, 12, "O Colapso", "destreza", 22, 15,
        "A batalha destruiu a integridade da escadaria. A ponte que liga aos aposentos reais desaba no abismo!",
        "Você corre contra a gravidade, saltando sobre as pedras em queda livre e fincando a Kagekiri na borda superior!",
        "O chão cede sob seus pés. Você cai dezenas de metros antes de se pendurar por uma bandeira rasgada, deslocando o ombro!")

    if jogador["vitalidade"] <= 0: return jogador

    # 13. O GUARDIÃO REAL
    layout.divisoria()
    layout.imprimir_lento(
        "[bold]Provação 13/13: O Guardião Real[/bold]\n"
        "As portas de ébano se abrem. No Salão do Julgamento aguarda o [bold yellow]Guardião Raiden, o Kensei do Trovão[/bold yellow]. "
        "Seu corpo é puro músculo reforçado com placas de aço. Ele empunha uma alabarda que estala com eletricidade roxa.\n"
        "'Um inseto rastejou longe demais', ele troveja. 'Vou devolver suas cinzas ao vulcão!'"
    )
    sistemas.iniciar_combate(jogador, "Guardião Raiden (CHEFE DA ROTA)", hp_inimigo=120, defesa_inimigo=18, min_dano=8, max_dano=16, xp_recompensa=200, fraqueza="Nenhuma", resistencia="Físico")
    
    return jogador


# ==========================================
# ROTA 2: O JARDIM DAS ILUSÕES (O CAMINHO DA MENTE)
# Foco: Testes de Sabedoria, armadilhas mágicas e Yokais.
# ==========================================
def rota_jardim_ilusoes(jogador):
    layout.cabecalho("O JARDIM DAS ILUSÕES", "O Labirinto da Loucura")
    layout.imprimir_lento(
        "Você segue pelo caminho central, um enorme jardim flutuante dentro da torre. "
        "A gravidade é distorcida. Cachoeiras fluem para o alto. O céu falso é estrelado por "
        "olhos cósmicos. Este é o domínio onde Kuroi enlouquece seus inimigos antes de matá-los."
    )
    
    # 1. A Flor Devoradora
    provacao_narrativa(jogador, 1, "O Aroma da Morte", "conhecimento", 18, 10,
        "Campos de lótus de cristal bloqueiam o caminho. O pólen prateado tenta hipnotizar sua mente e atraí-lo para os dentes das flores.",
        "Você fecha a respiração e foca nas memórias do mestre Kazunari, ignorando o canto hipnótico.",
        "A música entra em sua mente. Você caminha em direção a uma flor e as pétalas se fecham no seu braço, rasgando sua carne!")

    # 2. O Labirinto de Espelhos
    provacao_narrativa(jogador, 2, "Os Clones de Vidro", "conhecimento", 20, 10,
        "Você entra num corredor de espelhos infinitos. Seu próprio reflexo saca a espada e ataca de dentro do vidro!",
        "Você fecha os olhos. Usando apenas o som da respiração, você quebra o espelho mestre, estilhaçando o corredor.",
        "Confuso pela ilusão de ótica, você é golpeado pelas costas pelo seu próprio reflexo espectral!")
        
    if jogador["vitalidade"] <= 0: return jogador

    # 3. Combate 1
    layout.divisoria()
    layout.imprimir_lento("[bold]Provação 3/13: A Aranha das Memórias[/bold]\nUma Jorogumo (Mulher-Aranha) desce do teto falso. O rosto dela é o da sua mãe morta.")
    sistemas.iniciar_combate(jogador, "Jorogumo Espectral", hp_inimigo=55, defesa_inimigo=14, min_dano=5, max_dano=10, xp_recompensa=50, fraqueza="Físico", resistencia="Gelo")
    if jogador["vitalidade"] <= 0: return jogador

    # 4. A Gravidade Invertida
    provacao_narrativa(jogador, 4, "A Queda Para o Céu", "destreza", 20, 12,
        "O feitiço da sala é ativado e a gravidade se inverte. Você cai em direção a um teto repleto de estalactites afiadas!",
        "Você saca o Sol Negro e a Lua Prateada no ar, fatiando as pedras antes do impacto e caindo suavemente.",
        "Você tenta se agarrar a um pilar, mas a força gravitacional o joga contra as pedras, quebrando suas costelas!")

    # 5. A Passagem Mística
    layout.divisoria()
    layout.imprimir_lento("[bold]Provação 5/13: O Selo do Falso Sol[/bold]")
    layout.imprimir_lento("Para cruzar o jardim suspenso, há uma porta com símbolos arcanos rodopiando.")
    layout.console.print("[magenta]1 - [Analisar (Magia)][/magenta] Gastar 10 de Éter para hackear o selo.")
    layout.console.print("[white]2 - [Conhecimento Dificuldade 21][/white] Resolver o quebra-cabeça astrológico.")
    layout.limpar_buffer_teclado()
    if input("Escolha (1 ou 2): ").strip() == "1" and jogador.get("eter", 0) >= 10:
        jogador["eter"] -= 10
        layout.imprimir_lento("[magenta]Você inunda as trancas com Éter. A magia demoníaca se purifica e a porta cede.[/magenta]")
    else:
        if sistemas.rolar_teste(jogador, "conhecimento", 21): layout.imprimir_lento("[green]Você reorganiza as estrelas do selo mentalmente, e a porta se abre.[/green]")
        else: 
            layout.imprimir_lento("[red]A combinação errada explode em chamas gélidas no seu rosto![/red]")
            jogador["vitalidade"] -= 10
            
    if jogador["vitalidade"] <= 0: return jogador

    # 6 a 11 - O Desespero Mágico (Combates e ilusões)
    layout.divisoria()
    layout.imprimir_lento(
        "[bold]Provações 6 a 11: A Purificação do Jardim[/bold]\n"
        "O jardim recusa-se a deixá-lo passar. O ambiente vomita construtos de terra, sombras elementais e "
        "monges necromantes de uma só vez. A magia do Abismo pulsa incessantemente."
    )
    layout.esperar_enter("[dim]Pressione Enter para fatiar as trevas...[/dim]")
    
    sistemas.iniciar_combate(jogador, "Monges do Fogo Fátuo", hp_inimigo=60, defesa_inimigo=15, min_dano=5, max_dano=11, xp_recompensa=45, fraqueza="Gelo", resistencia="Nenhuma")
    if jogador["vitalidade"] <= 0: return jogador
    sistemas.iniciar_combate(jogador, "Gárgulas de Jade", hp_inimigo=75, defesa_inimigo=17, min_dano=7, max_dano=13, xp_recompensa=65, fraqueza="Nenhuma", resistencia="Físico")
    if jogador["vitalidade"] <= 0: return jogador

    # 12. O Enigma do Sacrifício
    provacao_narrativa(jogador, 12, "O Espelho da Alma", "kenjutsu", 22, 15,
        "A última porta é feita de vidro inquebrável. A escritura exige que você corte o próprio reflexo, o que exige técnica perfeita para não rebater o golpe.",
        "O Sol Negro corta o espaço. O golpe atravessa o vidro cristalino cortando apenas o selo, sem feri-lo.",
        "Sua técnica foi imperfeita. O golpe de espada ricocheteia no vidro mágico e atinge seu próprio flanco!")

    if jogador["vitalidade"] <= 0: return jogador

    # 13. O GUARDIÃO REAL
    layout.divisoria()
    layout.imprimir_lento(
        "[bold]Provação 13/13: O Guardião Real[/bold]\n"
        "No Templo de Lótus aguarda a [bold magenta]Guardiã Tsukuyomi, a Senhora das Ilusões[/bold magenta]. "
        "Ela levita sobre o chão, ladeada por orbes de gelo negro e empunhando um leque de lâminas afiadas.\n"
        "'A mente humana é frágil, Ishido. Eu o farei esquecer de por que veio aqui antes de matá-lo!'"
    )
    sistemas.iniciar_combate(jogador, "Guardiã Tsukuyomi (CHEFE DA ROTA)", hp_inimigo=100, defesa_inimigo=19, min_dano=7, max_dano=18, xp_recompensa=200, fraqueza="Físico", resistencia="Gelo")
    
    return jogador


# ==========================================
# ROTA 3: AS CATACUMBAS SUSPENSAS (O CAMINHO DA FURTIVIDADE)
# Foco: Agilidade extrema, abismos, armadilhas mecânicas e venenos.
# ==========================================
def rota_catacumbas_suspensas(jogador):
    layout.cabecalho("AS CATACUMBAS SUSPENSAS", "O Abismo Não Tem Fundo")
    layout.imprimir_lento(
        "Você empurra a porta enferrujada à direita. A luz desaparece. Você se encontra em um abismo formidável. "
        "Correntes grossas como troncos seguram celas enferrujadas e pedaços de alvenaria sobre um vácuo negro. "
        "O vento assobia através dos esqueletos enforcados. O caminho exige destreza impecável."
    )
    
    # 1. A Ponte de Correntes
    provacao_narrativa(jogador, 1, "Os Elos do Medo", "destreza", 19, 10,
        "Para acessar a primeira plataforma, você deve se equilibrar numa corrente bamba coberta de óleo de monstro.",
        "Seu equilíbrio é inabalável. Como uma sombra, você corre sobre o ferro escorregadio até o outro lado.",
        "Seu pé desliza! Você fica pendurado pelo braço, batendo violentamente o corpo contra a lateral de pedra.")

    # 2. Chuva de Viúvas-Negras
    provacao_narrativa(jogador, 2, "A Seda Sufocante", "kenjutsu", 20, 10,
        "O teto está coberto de teias. Ao pisar na plataforma, centenas de aranhas-da-caverna desabam sobre você!",
        "Um furacão de aço. A Lua Prateada cria um escudo giratório, fatiando os insetos antes que o toquem.",
        "A seda prende sua espada! As aranhas mordem seu pescoço e costas, injetando veneno antes de você esmagá-las.")
        
    if jogador["vitalidade"] <= 0: return jogador

    # 3. Combate 1
    layout.divisoria()
    layout.imprimir_lento("[bold]Provação 3/13: O Carcereiro Amaldiçoado[/bold]\nUm monstro cego gigante balança uma âncora acorrentada, patrulhando a ponte de pedra principal.")
    sistemas.iniciar_combate(jogador, "Carcereiro Cego", hp_inimigo=65, defesa_inimigo=13, min_dano=5, max_dano=13, xp_recompensa=50, fraqueza="Nenhuma", resistencia="Nenhuma")
    if jogador["vitalidade"] <= 0: return jogador

    # 4. A Parede Desmoronante
    provacao_narrativa(jogador, 4, "Parkour Mortal", "destreza", 21, 12,
        "O impacto do carcereiro cede a ponte! Você deve correr pelas paredes que estão desabando no abismo infinito.",
        "Numa sequência épica de saltos diagonais pelas pedras em queda, você aterrissa em um terraço alto e seguro.",
        "Uma pedra solta falha sob sua bota. Você cai, precisando usar o Arpéu para se puxar de volta, mas luxando feio o ombro.")

    # 5. A Passagem Secreta
    layout.divisoria()
    layout.imprimir_lento("[bold]Provação 5/13: As Lâminas Pendulares[/bold]")
    layout.imprimir_lento("O túnel à frente é um moedor de carne mecânico. Dezenas de machados pendulam do teto.")
    layout.console.print("[cyan]1 - [Passos Fantasmas][/cyan] Gastar 10 de Éter para dar um dash de invulnerabilidade.")
    layout.console.print("[white]2 - [Destreza Dificuldade 22][/white] Dançar entre a morte calculando o timing de cada pêndulo.")
    layout.limpar_buffer_teclado()
    if input("Escolha (1 ou 2): ").strip() == "1" and jogador.get("eter", 0) >= 10:
        jogador["eter"] -= 10
        layout.imprimir_lento("[cyan]Você pisca através do espaço, passando pelas lâminas intocável como fumaça.[/cyan]")
    else:
        if sistemas.rolar_teste(jogador, "destreza", 22): layout.imprimir_lento("[green]Com precisão cirúrgica, você escorrega e salta milimetricamente entre o aço mortal.[/green]")
        else: 
            layout.imprimir_lento("[red]Um erro de milissegundos! Um machado rasga um corte profundo transversal no seu peito![/red]")
            jogador["vitalidade"] -= 12
            
    if jogador["vitalidade"] <= 0: return jogador

    # 6 a 11 - O Ninho dos Assassinos (Furtividade / Emboscadas)
    layout.divisoria()
    layout.imprimir_lento(
        "[bold]Provações 6 a 11: A Caçada nas Sombras[/bold]\n"
        "As catacumbas se tornam um ninho de assassinos ninja corrompidos. Eles atacam atirando shurikens das trevas, "
        "armando fios-de-tropeço venenosos e despencando do teto. É matar ou morrer na velocidade da luz."
    )
    layout.esperar_enter("[dim]Pressione Enter para enfrentar a guilda morta...[/dim]")
    
    sistemas.iniciar_combate(jogador, "Ninjas Espectrais", hp_inimigo=65, defesa_inimigo=16, min_dano=4, max_dano=9, xp_recompensa=50, fraqueza="Nenhuma", resistencia="Nenhuma")
    if jogador["vitalidade"] <= 0: return jogador
    sistemas.iniciar_combate(jogador, "A Besta das Correntes", hp_inimigo=85, defesa_inimigo=14, min_dano=7, max_dano=14, xp_recompensa=70, fraqueza="Físico", resistencia="Gelo")
    if jogador["vitalidade"] <= 0: return jogador

    # 12. O Último Salto
    provacao_narrativa(jogador, 12, "O Salto da Fé", "destreza", 23, 15,
        "A porta final fica isolada a dez metros de distância, sem pontes. Apenas uma fina corrente vertical pende no meio do vão.",
        "Você salta no vazio, agarra a corrente em pêndulo perfeito, toma impulso e aterrissa na sacada final graciosamente.",
        "Você erra o salto perfeito. Suas mãos escorregam na corrente e você despenca, fincando o Sol Negro na parede para travar a queda dolorosa.")

    if jogador["vitalidade"] <= 0: return jogador

    # 13. O GUARDIÃO REAL
    layout.divisoria()
    layout.imprimir_lento(
        "[bold]Provação 13/13: O Guardião Real[/bold]\n"
        "Nas varandas de mármore branco envoltas em névoa negra repousa o [bold blue]Guardião Shinigami, a Foice de Gelo[/bold blue]. "
        "Um vulto assombroso em mantos rasgados, armado com duas foices encadeadas que emanam frio absoluto.\n"
        "'As sombras me servem, ronin. E hoje, elas devorarão a sua luz!'"
    )
    sistemas.iniciar_combate(jogador, "Guardião Shinigami (CHEFE DA ROTA)", hp_inimigo=110, defesa_inimigo=20, min_dano=7, max_dano=15, xp_recompensa=200, fraqueza="Físico", resistencia="Gelo")
    
    return jogador


# ==========================================
# CENA FINAL: O PORTÃO DO FEITICEIRO
# ==========================================
def cena_transicao_kuroi(jogador):
    if jogador["vitalidade"] <= 0: return jogador
    
    layout.cabecalho("O ÁPICE DO ABISMO", "Frente a Frente com o Destino")

    layout.imprimir_lento(
        "A carcaça do Guardião Real se dissolve no ar. O silêncio que se segue é ensurdecedor.\n\n"
        "Você subiu através do sangue, da lama, do fogo, e da loucura mágica. "
        "Você caminha ensanguentado, os pulmões em chamas, subindo os degraus de obsidiana "
        "que levam à porta mais alta da Torre do Abismo.\n\n"
        "Um portão circular gigantesco, adornado com estrelas e crânios de prata.\n"
        "O Astrolábio Celestial.\n\n"
        "Atrás desta porta está o Mago Kuroi Shin'en, o usurpador que assassinou seu pai, "
        "destruiu seu clã, rasgou o braço de seu mestre Kazunari e transformou Takenoko "
        "num império de cinzas."
    )
    
    layout.imprimir_lento(
        "\nVocê solta o ar lentamente. As mãos repousam com familiaridade mortífera sobre "
        "os cabos do Sol Negro e da Lua Prateada. O Estilo Nitoryu atingiu a perfeição."
    )
    
    layout.esperar_enter("[dim]Você empurra os portões celestiais com os dois braços...[/dim]")

    # Como não temos um acampamento aqui e a luta final começa no próximo capítulo,
    # curamos levemente o jogador para que ele não entre no boss final com 1 HP.
    cura = 30
    jogador["vitalidade"] = min(jogador.get("max_vitalidade", 100), jogador["vitalidade"] + cura)
    layout.imprimir_lento(f"\n[green]A determinação inabalável da sua linhagem restaura seu foco (+{cura} HP).[/green]")

    return jogador


# ==========================================
# GESTOR DO CAPÍTULO 5
# ==========================================
def jogar(jogador):
    layout.cabecalho("CAPÍTULO 5: A TORRE DO ABISMO")

    layout.imprimir_lento(
        "A enorme torre espirala pelos céus corrompidos. Kuroi enclausurou-se no ápice. "
        "A base da torre se divide em três pavilhões colossais, cada um ostentando uma horripilante arquitetura. "
        "Apenas um pode ser escolhido para sua escalada final."
    )

    layout.console.print("\n[bold]Escolha o caminho para o topo da Torre:[/bold]")
    layout.console.print("[white]1 - A Ala Sangrenta[/white] (O caminho da Guerra. Foco em força bruta, hordas pesadas e resistência).")
    layout.console.print("[white]2 - O Jardim das Ilusões[/white] (O caminho da Mente. Foco em sanidade, magia e Yokais místicos).")
    layout.console.print("[white]3 - As Catacumbas Suspensas[/white] (O caminho das Sombras. Foco em furtividade extrema e acrobacias mortais).")

    escolha_caminho = ""
    while escolha_caminho not in ["1", "2", "3"]:
        layout.limpar_buffer_teclado()
        escolha_caminho = input("\nEscolha sua trilha (1, 2 ou 3): ").strip()

    if escolha_caminho == "1":
        jogador = rota_ala_sangrenta(jogador)
    elif escolha_caminho == "2":
        jogador = rota_jardim_ilusoes(jogador)
    elif escolha_caminho == "3":
        jogador = rota_catacumbas_suspensas(jogador)

    if jogador["vitalidade"] <= 0: return jogador
    
    # A transição épica para o Boss Final
    jogador = cena_transicao_kuroi(jogador)
    
    return jogador