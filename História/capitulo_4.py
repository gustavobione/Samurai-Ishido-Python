# capitulo_4.py
import layout
import sistemas

# ==========================================
# CENA 1: A VULNERABILIDADE NAS ÁGUAS DE MIZU
# ==========================================
def cena_sobrevivencia_mizu(jogador):
    layout.cabecalho("AS ÁGUAS DO LAMENTO", "O Samurai Quebrado")

    layout.imprimir_lento(
        "A Província de Mizu é um cemitério afogado. Campos de arroz putrefatos se estendem "
        "até onde os olhos podem ver, engolidos por uma neblina perpétua que cheira a sal e sangue. "
        "Sem a Kagekiri, a escuridão parece pressionar o seu corpo. Você sente a ausência da "
        "sua lâmina não apenas na mão, mas na alma."
    )
    
    if not jogador.get("penalidade_espada_aplicada"):
        jogador["kenjutsu"] -= 10
        jogador["penalidade_espada_aplicada"] = True
        layout.console.print("\n[bold red]" + "!"*60)
        layout.console.print(" [Aviso: Sem uma lâmina para aparar golpes e atacar, seu Kenjutsu despencou em -10!]")
        layout.console.print(" [Sua Defesa passiva foi reduzida. O combate frontal agora é suicídio.]")
        layout.console.print("!"*60 + "[/bold red]\n")
    
    layout.esperar_enter()

    # --- DESAFIO 1: Os Juncos Afogados ---
    layout.divisoria()
    layout.imprimir_lento(
        "Para adentrar a província, você precisa atravessar um pântano de juncos gigantescos. "
        "A água escura oculta raízes espinhosas e sanguessugas abissais do tamanho de serpentes."
    )
    layout.console.print("\n[bold]Desafio 1: A Travessia Silenciosa[/bold]")
    layout.console.print("[white]1 - [Destreza Dificuldade 16][/white] Mover-se lentamente, sentindo o lodo e evitando fazer barulho.")
    layout.console.print("[cyan]2 - [Passos Fantasmas][/cyan] Gastar 10 de Éter para flutuar sobre a água turva.")
    
    layout.limpar_buffer_teclado()
    esc1 = input("\nComo você avança? (1 ou 2): ").strip()
    
    if esc1 == "2" and jogador.get("eter", 0) >= 10:
        jogador["eter"] -= 10
        jogador.setdefault("atributos_usados", set()).add("eter")
        layout.imprimir_lento("\n[cyan]Seu corpo vira névoa azul, deslizando intocável sobre os horrores submersos.[/cyan]")
    else:
        if esc1 == "2": layout.imprimir_lento("\n[red]Éter insuficiente para a travessia completa.[/red]")
        if sistemas.rolar_teste(jogador, "destreza", 16):
            layout.imprimir_lento("\n[green]Com passos de garça, você cruza o pântano sem agitar a água, escapando ileso.[/green]")
        else:
            layout.imprimir_lento("\n[red]Você tropeça em uma raiz! O mergulho atrai as sanguessugas, que rasgam sua perna antes de você alcançar a margem![/red]")
            jogador["vitalidade"] -= 5
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 2: A Patrulha dos Afogados ---
    layout.divisoria()
    layout.imprimir_lento(
        "Adiante, o rio se estreita. Três Ashigarus (soldados) de Kuroi, com armaduras enferrujadas e "
        "corpos inchados pela magia da água, patrulham a única ponte de pedra."
    )
    layout.console.print("\n[bold]Desafio 2: Os Olhos Corrompidos[/bold]")
    layout.console.print("[white]1 - [Conhecimento Dificuldade 15][/white] Estudar a rota de patrulha e jogar uma pedra para distraí-los.")
    layout.console.print("[white]2 - [Destreza Dificuldade 17][/white] Mergulhar no rio e prender a respiração, passando por baixo da ponte.")
    
    layout.limpar_buffer_teclado()
    esc2 = input("\nSua escolha (1 ou 2): ").strip()
    
    if esc2 == "1":
        if sistemas.rolar_teste(jogador, "conhecimento", 15):
            layout.imprimir_lento("\n[green]Os guardas investigam o som nos juncos enquanto você cruza a ponte como uma sombra.[/green]")
        else:
            layout.imprimir_lento("\n[red]Eles não se deixam enganar e atiram lanças na direção do barulho! Uma raspa seu braço![/red]")
            jogador["vitalidade"] -= 4
    else:
        if sistemas.rolar_teste(jogador, "destreza", 17):
            layout.imprimir_lento("\n[green]Você afunda no silêncio da água podre e emerge seguro do outro lado.[/green]")
        else:
            layout.imprimir_lento("\n[red]A correnteza o atira contra a pilastra da ponte, machucando suas costelas e alertando os guardas, forçando uma fuga desesperada![/red]")
            jogador["vitalidade"] -= 6
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 3: O Nevoeiro Ilusório ---
    layout.divisoria()
    layout.imprimir_lento(
        "O caminho o leva a um vilarejo abandonado coberto por um nevoeiro luminescente. "
        "Fantasmas de aldeões choram e tentam agarrar suas roupas, sugando seu calor."
    )
    if sistemas.rolar_teste(jogador, "conhecimento", 16):
        layout.imprimir_lento("\n[green]Você recita um mantra mental, blindando sua alma contra as ilusões. Os fantasmas não conseguem tocá-lo.[/green]")
    else:
        layout.imprimir_lento("\n[red]A dor e o frio dos espectros invadem seu peito. A tristeza gela seu sangue![/red]")
        jogador["vitalidade"] -= 5
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 4: Luta com os Punhos ---
    layout.divisoria()
    layout.imprimir_lento(
        "Ao sair do nevoeiro, um Saqueador Desesperado armado com um machado enferrujado salta "
        "de um telhado desabado. Ele está faminto e não vai deixar você passar. Sem sua espada, "
        "você terá que lutar com os punhos e o que restou do seu Kenjutsu!"
    )
    # Luta forçada com punhos
    resultado = sistemas.iniciar_combate(jogador, "Saqueador Faminto", hp_inimigo=20, defesa_inimigo=10, min_dano=2, max_dano=5, xp_recompensa=20, fraqueza="Físico", resistencia="Nenhuma")
    if resultado == "morte": return jogador
    layout.esperar_enter()

    # --- DESAFIO 5: O Rio Furioso ---
    layout.divisoria()
    layout.imprimir_lento(
        "O saqueador morto cai em um rio de corredeiras furiosas. Você precisa nadar contra a "
        "correnteza para alcançar a montanha de pedra onde as lendas dizem que o ferreiro se esconde."
    )
    if sistemas.rolar_teste(jogador, "destreza", 15):
        layout.imprimir_lento("\n[green]Seus braços cortam a água barrenta com perfeição, alcançando a rocha vulcânica ileso.[/green]")
    else:
        layout.imprimir_lento("\n[red]A correnteza é forte demais! Você engole água suja e é jogado brutalmente contra as pedras antes de conseguir subir.[/red]")
        jogador["vitalidade"] -= 6
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    return jogador

# ==========================================
# CENA 2: O MESTRE E A BUSCA
# ==========================================
def cena_encontro_ferreiro(jogador):
    # --- DESAFIO 6: O Selo do Artesão ---
    layout.cabecalho("O EXILADO DA FORJA", "O Chamado do Aço")
    layout.imprimir_lento(
        "No topo das pedras, há uma caverna escondida atrás de uma cachoeira. A entrada, no entanto, "
        "está selada por um mecanismo de engrenagens ancestrais coberto de ferrugem e magia xintoísta."
    )
    layout.console.print("\n[bold]Desafio 6: O Enigma da Porta[/bold]")
    layout.console.print("[white]1 - [Conhecimento Dificuldade 18][/white] Desvendar o padrão astrológico das engrenagens para abrir a porta suavemente.")
    layout.console.print("[magenta]2 - [Analisar (Magia)][/magenta] Gastar 5 de Éter para enxergar o fluxo de energia e alinhar as trancas.")
    
    layout.limpar_buffer_teclado()
    esc6 = input("\nComo você abre? (1 ou 2): ").strip()
    
    if esc6 == "2" and jogador.get("eter", 0) >= 5:
        jogador["eter"] -= 5
        jogador.setdefault("atributos_usados", set()).add("conhecimento")
        layout.imprimir_lento("\n[magenta]Focando o Éter nos olhos, as trancas ocultas brilham. Você gira o painel e a porta se abre com um ronco de pedra.[/magenta]")
    else:
        if esc6 == "2": layout.imprimir_lento("\n[red]Éter insuficiente.[/red]")
        if sistemas.rolar_teste(jogador, "conhecimento", 18):
            layout.imprimir_lento("\n[green]Você decifra os kanjis antigos. As engrenagens se alinham e o selo se desfaz.[/green]")
        else:
            layout.imprimir_lento("\n[red]Você força a engrenagem errada! Um choque mágico violento o arremessa para trás antes da porta se escancarar lentamente.[/red]")
            jogador["vitalidade"] -= 5
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()
    
    # O Diálogo com Kajiya
    layout.divisoria()
    layout.imprimir_lento(
        "A caverna irradia um calor reconfortante. Um homem idoso, cego e com braços repletos de "
        "cicatrizes de fogo, golpeia uma bigorna de jade.\n\n"
        "'A respiração... O leve cheiro de aço meteorítico.' O Mestre Kajiya vira seu rosto sem olhos para você.\n"
        "'O sangue Shiro vive. E sua lâmina se partiu no magma, como eu avisei seu mestre Kazunari há tantos anos.'\n\n"
        "Você deposita os estilhaços da Kagekiri na bigorna.\n"
        "'A Kagekiri original cortava almas. Mas ela estava incompleta. O meteorito de onde ela veio tinha dois "
        "metais: um que canaliza o gelo, e outro que corta o próprio vazio.'\n"
    )
    
    layout.imprimir_lento(
        "Mestre Kajiya se levanta. 'Eu posso reforjar seu destino, Ishido. Mas precisarei de dois catalisadores "
        "destas terras malditas para suportar o calor do meu forno celestial: A Lótus Abissal e a Pérola do Rio.'\n"
        "Sua missão é clara. Retornar ao pântano e recuperar os ingredientes."
    )
    layout.esperar_enter()

    # --- DESAFIO 7: A Lótus Abissal ---
    layout.divisoria()
    layout.imprimir_lento(
        "No leste de Mizu, a Lótus Abissal cresce no centro de uma bacia de ácido venenoso, "
        "cercada por sapos mutantes que cospem bile corrosiva."
    )
    if sistemas.rolar_teste(jogador, "destreza", 18):
        layout.imprimir_lento("\n[green]Ágil como o vento, você salta sobre as pedras, arranca a flor negra e recua antes que os sapos o alcancem.[/green]")
    else:
        layout.imprimir_lento("\n[red]Um sapo cospe ácido nas pedras! Você escorrega, queima a perna no ácido e foge desesperado com a flor nas mãos![/red]")
        jogador["vitalidade"] -= 7
    if jogador["vitalidade"] <= 0: return jogador
    jogador.setdefault("inventario", []).append("Lótus Abissal")
    layout.esperar_enter()

    # --- DESAFIO 8: A Pérola do Rio ---
    layout.divisoria()
    layout.imprimir_lento(
        "No oeste, submerso nas ruínas de um templo, repousa a Pérola do Rio. Para pegá-la, "
        "você precisa mergulhar profundamente, prender a respiração por minutos e desviar das armadilhas subaquáticas."
    )
    if sistemas.rolar_teste(jogador, "conhecimento", 17):
        layout.imprimir_lento("\n[green]Você entende a arquitetura antiga. Evitando os fios de armadilha submersos, você pega a Pérola e emerge triunfante.[/green]")
    else:
        layout.imprimir_lento("\n[red]Você esbarra numa corrente! Dardos são disparados na água, perfurando seu ombro enquanto você nada de volta à superfície com a Pérola.[/red]")
        jogador["vitalidade"] -= 6
    if jogador["vitalidade"] <= 0: return jogador
    jogador.setdefault("inventario", []).append("Pérola do Rio")
    layout.esperar_enter()

    # --- DESAFIO 9: A Emboscada dos Ronins ---
    layout.divisoria()
    layout.imprimir_lento(
        "Retornando com os ingredientes, três Ronins Assassinos de Kuroi interceptam você. "
        "Eles notam que você está desarmado e sorriem cruelmente."
    )
    layout.console.print("\n[bold]Desafio 9: Sobrevivência Pura[/bold]")
    layout.console.print("[white]1 - [Destreza Dificuldade 19][/white] Chutar areia, usar as árvores para parkour e fugir como um raio.")
    layout.console.print("[yellow]2 - [Honra e Combate][/yellow] 'Um samurai não foge'. Lutar com os punhos até quebrar os rostos deles! (-2 Honra pela brutalidade desmedida, mas prova sua força).")
    
    layout.limpar_buffer_teclado()
    esc9 = input("\nSua escolha (1 ou 2): ").strip()
    
    if esc9 == "1":
        if sistemas.rolar_teste(jogador, "destreza", 19):
            layout.imprimir_lento("\n[green]Eles tentam cortar o vento. Você desaparece entre as folhagens, deixando-os confusos para trás.[/green]")
        else:
            layout.imprimir_lento("\n[red]Um deles é mais rápido e o acerta com a bainha da espada! Você rola na lama e consegue fugir, mas sangrando e machucado.[/red]")
            jogador["vitalidade"] -= 8
    else:
        jogador["honra"] -= 2
        resultado = sistemas.iniciar_combate(jogador, "Trio de Ronins (Punhos Nus)", hp_inimigo=35, defesa_inimigo=11, min_dano=3, max_dano=7, xp_recompensa=50, fraqueza="Físico", resistencia="Nenhuma")
        if resultado == "morte": return jogador
        layout.imprimir_lento("\n[dim]Você deixa os três desacordados na lama, os nós dos seus dedos rachados e sangrando.[/dim]")
    
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    return jogador

# ==========================================
# CENA 3: A FORJA DE UMA ESTRELA E O CLÍMAX
# ==========================================
def cena_a_forja_estelar(jogador):
    # --- DESAFIO 10: O Sangue e o Aço ---
    layout.cabecalho("A FORJA DO ECLIPSE", "Renascimento")
    
    layout.imprimir_lento(
        "Você retorna à caverna e deposita a Lótus Abissal e a Pérola do Rio na bigorna. "
        "Mestre Kajiya assente. Ele atira os ingredientes e os estilhaços do meteorito no fogo vulcânico "
        "alimentado por magias esquecidas.\n\n"
        "'A parte final do ritual exige o sacrifício da sua aura, Ishido. Coloque a mão no fogo. "
        "Vou fundir o aço da sua espada com o Éter da sua linhagem!'"
    )
    
    layout.console.print("\n[bold]Desafio 10: O Ritual da Dor[/bold]")
    layout.console.print("[white]1 - [Kenjutsu Dificuldade 18][/white] Aceitar a dor física extrema para transferir seu poder para o metal.")
    
    layout.limpar_buffer_teclado()
    input("\nPressione Enter para mergulhar a mão nas chamas... ")
    
    if sistemas.rolar_teste(jogador, "kenjutsu", 18):
        layout.imprimir_lento("\n[green]Você canaliza toda a sua força de vontade. A dor é ofuscada pelo brilho do aço nascendo das cinzas![/green]")
    else:
        layout.imprimir_lento("\n[red]Você grita em agonia! O calor drena sua vida, mas você não recua. O ritual consome seu corpo, mas o aço é forjado![/red]")
        jogador["vitalidade"] -= 10
        if jogador["vitalidade"] <= 0: return jogador

    # O MILAGRE DA FORJA
    layout.divisoria()
    layout.imprimir_lento(
        "A fumaça se dissipa. Kajiya mergulha as lâminas na água sagrada, criando uma nuvem de vapor puro.\n"
        "Ele se vira, segurando duas bainhas magníficas.\n\n"
        "[italic white]'A Kagekiri se partiu para se multiplicar, Ishido. Eu separei as impurezas do meteorito.'[/italic white]\n"
        "Na sua mão direita, a **Mizukiri (Lua Prateada)**. Uma katana fluida e gélida, capaz de congelar e cortar os ventos.\n"
        "Na sua mão esquerda, a **Kokkio (Sol Negro)**. Forjada com o metal estelar puro. Ela não corta armaduras... ela corta o Vazio, ignorando defesas materiais.\n\n"
        "[italic cyan]'Juntas, elas formam o Estilo Nitoryu: A Arte do Eclipse. Levante-se, Mestre das Duas Lâminas.'[/italic cyan]"
    )

    # REMOVENDO PENALIDADES E APLICANDO BUFFS ABSURDOS
    jogador["espada_quebrada"] = False
    jogador["penalidade_espada_aplicada"] = False
    jogador["duas_espadas_longas"] = True
    jogador["kenjutsu"] += 15 # Devolve os 10 perdidos + 5 de buff pelo novo aço
    jogador["destreza"] += 3
    jogador["max_eter"] += 15
    jogador["eter"] = jogador["max_eter"]
    jogador["vitalidade"] = jogador.get("max_vitalidade", 100) # Cura completa
    
    if "habilidades" not in jogador: jogador["habilidades"] = []
    jogador["habilidades"].append("Arte Nitoryu: Eclipse")
    jogador["habilidades"].append("Corte do Vazio")
    
    layout.console.print("\n[bold yellow]" + "*"*60)
    layout.console.print("  ⚔️ O SAMURAI DESPERTOU: ESTILO SOL E LUA ⚔️")
    layout.console.print(" [Penalidade de -10 Kenjutsu Removida!]")
    layout.console.print(" [Bônus Atribuídos: Kenjutsu +5, Destreza +3, Éter Máximo +15]")
    layout.console.print(" [HP e Éter totalmente restaurados!]")
    layout.console.print(" [Novas Habilidades Liberadas em Combate!]")
    layout.console.print("*"*60 + "[/bold yellow]\n")
    layout.esperar_enter()

    # --- DESAFIO 11: O Kensei do Abismo (BOSS) ---
    layout.divisoria()
    layout.imprimir_lento(
        "Antes que você possa agradecer, as paredes da caverna explodem.\n"
        "A água da cachoeira se divide sob o poder de uma intenção assassina esmagadora. "
        "Um samurai colossal, coberto de armadura negra e portando uma Nodachi flamejante entra na forja.\n"
        "'Kensei do Abismo', o Carrasco Pessoal do Mago Kuroi.\n"
        "'Então o ferreiro cego e o ronin bastardo se uniram', ele ruge, a voz distorcida por magia sombria. "
        "'Eu cortarei a cabeça dos dois e entregarei as novas espadas ao meu Mestre!'"
    )
    
    layout.imprimir_lento(
        "\nVocê dá um passo à frente, cobrindo o mestre cego. Você saca o Sol Negro e a Lua Prateada simultaneamente. "
        "O ar congela e o espaço distorce ao seu redor. A verdadeira batalha começa agora."
    )
    
    # Combate de clímax, o jogador vai testar o dano massivo das novas espadas.
    resultado = sistemas.iniciar_combate(jogador, "Kensei do Abismo (CHEFE)", hp_inimigo=100, defesa_inimigo=16, min_dano=6, max_dano=14, xp_recompensa=200, fraqueza="Gelo", resistencia="Físico")
    
    if resultado == "morte" or jogador["vitalidade"] <= 0: return jogador

    layout.divisoria()
    layout.imprimir_lento(
        "O Kensei do Abismo paralisa. O Sol Negro rasgou sua armadura indestrutível através do tecido do espaço, "
        "enquanto a Lua Prateada congelou seu sangue no mesmo instante.\n"
        "Com um som de vidro estilhaçando, o corpo do Carrasco se despedaça em poeira estelar negra.\n\n"
        "Mestre Kajiya sorri de forma serena.\n"
        "'As Lâminas reconheceram seu Mestre. O destino de Takenoko está em suas mãos, Ishido. "
        "Vá. A Torre do Abismo de Kuroi o aguarda nas nuvens corrompidas do horizonte.'"
    )
    
    jogador = sistemas.acampamento_fogueira(jogador, capitulo_atual=4, contexto="espadas_forjadas")
    
    return jogador

# ==========================================
# GESTOR DO CAPÍTULO 4
# ==========================================
def jogar(jogador):
    jogador = cena_sobrevivencia_mizu(jogador)
    if jogador["vitalidade"] <= 0: return jogador
    
    jogador = cena_encontro_ferreiro(jogador)
    if jogador["vitalidade"] <= 0: return jogador
    
    jogador = cena_a_forja_estelar(jogador)
    
    layout.imprimir_lento("\n[dim]As sombras abrem passagem para você. A aproximação para a Torre Final começou.[/dim]")
    layout.esperar_enter()
    return jogador