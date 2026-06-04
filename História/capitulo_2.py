# capitulo_2.py
import layout
import sistemas
import time

# ==========================================
# ROTA 1: FLORESTA (COPAS) - O DOSSEL DAS ILUSÕES
# Rota para quem veio da Vila Gelo (Superfície)
# ==========================================
def cena_floresta_copas(jogador):
    layout.cabecalho("A FLORESTA MURMURANTE", "O Dossel das Ilusões")

    layout.imprimir_lento(
        "Deixando o gelo da montanha para trás, o ar se torna subitamente morno e perfumado com o cheiro "
        "de folhas em decomposição. Você se encontra não no chão da Floresta Murmurante, mas no topo de seu dossel.\n\n"
        "As árvores aqui são titânicas. Galhos da largura de pontes se entrelaçam sobre um oceano de névoa cinzenta "
        "que oculta o solo dezenas de metros abaixo. A luz do sol entra fraca, filtrada por folhas do tamanho de escudos."
    )
    
    # ---------------- DESAFIO 1: O EQUILÍBRIO DO VENTO ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "O vento não sopra, ele chora. Para avançar para a próxima árvore ancestral, você precisa "
        "atravessar um tronco coberto de musgo azul, escorregadio e assolado por lufadas de vento imprevisíveis."
    )
    layout.console.print("\n[bold]Desafio 1: A Ponte de Musgo[/bold]")
    layout.console.print("[white]1 - [Destreza Dificuldade 15][/white] Correr focando no seu centro de gravidade.")
    layout.console.print("[cyan]2 - [Passos Fantasmas][/cyan] Gastar 10 de Éter para teleportar sobre as lufadas mais fortes.")
    
    layout.limpar_buffer_teclado()
    esc = input("\nComo você cruza? (1 ou 2): ").strip()
    
    if esc == "2" and jogador.get("eter", 0) >= 10:
        jogador["eter"] -= 10
        jogador.setdefault("atributos_usados", set()).add("eter")
        layout.imprimir_lento("\n[cyan]Você se dissolve na brisa. O vento furioso passa direto pelo seu corpo etéreo até você se materializar do outro lado.[/cyan]")
    else:
        if esc == "2": layout.imprimir_lento("\n[red]Éter insuficiente. Você terá que confiar nos seus pés.[/red]")
        if sistemas.rolar_teste(jogador, "destreza", 15):
            layout.imprimir_lento("\n[green]Sucesso! Seus pés deslizam estrategicamente, compensando cada empurrão do vento.[/green]")
        else:
            layout.imprimir_lento("\n[red]FALHA! Um rajada repentina faz você escorregar. Você cai, batendo as costelas num galho inferior antes de se estabilizar.[/red]")
            jogador["vitalidade"] -= 6
            
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # ---------------- DESAFIO 2: A ILUSÃO DO MESTRE ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "Avançando pela folhagem densa, o ar congela. A névoa rodopia e forma a figura do seu mestre "
        "Kazunari. Mas ele está diferente. Ele possui ambos os braços e sorri calorosamente, estendendo "
        "a mão sobre um abismo. 'Venha, Ishido. Pise aqui, a ilusão é o chão, a verdade é o vazio. Confie em mim.'"
    )
    layout.console.print("\n[bold]Desafio 2: O Fantasma da Saudade[/bold]")
    layout.console.print("[white]1 - [Conhecimento Dificuldade 16][/white] Focar a mente para analisar o fluxo de Éter e quebrar o Genjutsu (ilusão).")
    layout.console.print("[white]2 - [Honra e Kenjutsu Dificuldade 15][/white] 'Meu mestre sacrificou o braço por mim!'. Atacar a ofensa à memória dele.")
    
    layout.limpar_buffer_teclado()
    esc2 = input("\nSua reação (1 ou 2): ").strip()
    
    if esc2 == "1":
        if sistemas.rolar_teste(jogador, "conhecimento", 16):
            layout.imprimir_lento("\n[green]Seus olhos brilham. Você vê a magia pútrida sustentando a miragem. O fantasma se desfaz em cinzas.[/green]")
        else:
            layout.imprimir_lento("\n[red]A ilusão perfura sua mente. Uma dor de cabeça agonizante o força a cair de joelhos.[/red]")
            jogador["vitalidade"] -= 5
    else:
        if sistemas.rolar_teste(jogador, "kenjutsu", 15):
            layout.imprimir_lento("\n[green]Você saca a Kagekiri com lágrimas de raiva. O corte espectral despedaça a ilusão demoníaca no ar.[/green]")
            jogador["honra"] += 1
            layout.console.print("[bold green]+1 de Honra pela devoção.[/bold green]")
        else:
            layout.imprimir_lento("\n[red]Você ataca cegamente e quase cai do abismo! A ilusão ri e explode em energia negra, queimando você.[/red]")
            jogador["vitalidade"] -= 5

    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # ---------------- DESAFIO 3: CORVOS DE SANGUE ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "A quebra da ilusão atraiu moradores indesejados. Três corvos do tamanho de cães, com bicos "
        "de metal enferrujado e olhos vazados pela corrupção, mergulham das folhagens disparando "
        "penas afiadas como navalhas."
    )
    resultado = sistemas.iniciar_combate(jogador, "Bando de Corvos Metálicos", hp_inimigo=30, defesa_inimigo=14, min_dano=2, max_dano=6, xp_recompensa=40, fraqueza="Gelo", resistencia="Nenhuma")
    if resultado == "morte": return jogador
    layout.esperar_enter()

    # ---------------- DESAFIO 4: O LABIRINTO DE SEDA ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "O caminho se estreita em um túnel natural coberto de seda de aranha prateada, grossa como cabos "
        "de aço. É grudenta e vibra com qualquer passo. Presos nela há esqueletos de samurais e feras."
    )
    layout.console.print("\n[bold]Desafio 4: A Seda de Jorogumo[/bold]")
    layout.console.print("[white]1 - [Destreza Dificuldade 17][/white] Contorcer-se pelo labirinto sem tocar num único fio.")
    layout.console.print("[white]2 - [Kenjutsu Dificuldade 15][/white] Cortar a teia brutalmente, assumindo o risco de chamar a atenção.")
    
    layout.limpar_buffer_teclado()
    esc4 = input("\nComo você avança? (1 ou 2): ").strip()
    
    if esc4 == "1":
        if sistemas.rolar_teste(jogador, "destreza", 17):
            layout.imprimir_lento("\n[green]Ágil como um felino, você atravessa o labirinto mortal sem disparar uma única vibração.[/green]")
        else:
            layout.imprimir_lento("\n[red]Seu ombro esbarra num fio. Um mecanismo natural dispara dardos de osso embebidos em veneno paralisante das paredes![/red]")
            jogador["vitalidade"] -= 6
    else:
        layout.imprimir_lento("\n[dim]Você corta a teia, abrindo caminho. O som reverbera longe.[/dim]")
        if sistemas.rolar_teste(jogador, "kenjutsu", 15):
            layout.imprimir_lento("\n[green]Você foi tão rápido que conseguiu atravessar o túnel antes que os donos da teia aparecessem.[/green]")
        else:
            layout.imprimir_lento("\n[red]Você se enrosca na seda pesada. Pequenas aranhas venenosas caem sobre você antes que consiga se libertar![/red]")
            jogador["vitalidade"] -= 6

    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # ---------------- DESAFIO 5: O DILEMA DO DAITENGU ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "Ao sair da teia, você chega a uma plataforma suspensa colossal, feita de árvores entrelaçadas. "
        "No centro, meditando sobre um santuário xintoísta em ruínas, está um Daitengu. Ele tem pele vermelha, "
        "um nariz proeminente e empunha uma Odachi (espada gigante). Pendurada acima do abismo, há uma gaiola "
        "de bambu com um mensageiro humano machucado.\n\n"
        "Ele abre olhos cor de ouro: 'O cheiro da linhagem Shiro. Eu não sirvo ao feiticeiro Kuroi, mas odeio "
        "sua raça indigna. Vá embora, ou prove que o aço de Takenoko ainda não apodreceu.'"
    )
    layout.console.print("\n[bold]Desafio 5: O Guardião dos Céus[/bold]")
    layout.console.print("[white]1 - [Combater][/white] O aço decide a honra. Aceitar o duelo de espadas frontalmente. [green](Ganha Honra)[/green]")
    layout.console.print("[white]2 - [Conhecimento Dificuldade 18][/white] 'Guerreiros dos céus prezam pelo respeito'. Responder com um Haiku milenar.")
    
    layout.limpar_buffer_teclado()
    esc5 = input("\nO que você faz? (1 ou 2): ").strip()
    lutou_tengu = False
    
    if esc5 == "1":
        layout.imprimir_lento("\n[dim]Você saca a Kagekiri e entra em postura. O Daitengu sorri ferozmente e avança.[/dim]")
        jogador["honra"] += 2
        lutou_tengu = True
    else:
        if sistemas.rolar_teste(jogador, "conhecimento", 18):
            layout.imprimir_lento(
                "\n[green]Você embainha a espada e declama: 'Vento que não corta / Pássaro que não pousa / Aço reconhece aço.'\n"
                "O monstro arregala os olhos, finca a espada no chão e se curva profundamente. 'Há sabedoria na linhagem Shiro', "
                "ele murmura, abrindo a gaiola do prisioneiro.[/green]"
            )
            jogador["honra"] += 3
            jogador["xp"] += 50
        else:
            layout.imprimir_lento("\n[red]Você engasga na última sílaba. O Daitengu suspira. 'Macacos tentando imitar a grandeza', diz ele, erguendo a lâmina![/red]")
            lutou_tengu = True

    if lutou_tengu:
        resultado = sistemas.iniciar_combate(jogador, "Daitengu (Semi-Chefe)", hp_inimigo=50, defesa_inimigo=15, min_dano=4, max_dano=9, xp_recompensa=60, fraqueza="Nenhuma", resistencia="Físico")
        if resultado == "morte": return jogador
        layout.imprimir_lento("\n[dim]O Tengu cai de joelhos, reconhecendo seu valor no último suspiro. O prisioneiro consegue se soltar e fugir.[/dim]")

    layout.esperar_enter()

    # ---------------- DESAFIO 6: ONMORAKI (CHEFE) ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "No final da plataforma, próximo à beirada que desce para a próxima região, o céu escurece. "
        "Uma nuvem de miasma negro se condensa no formato de uma garça demoníaca, com escamas no lugar "
        "de penas e olhos humanos dispostos assimetricamente em seu pescoço. O Onmoraki (Demônio Pássaro) "
        "nasceu das almas corrompidas dos moradores da floresta e quer devorar o que restou de luz em você."
    )
    resultado = sistemas.iniciar_combate(jogador, "Onmoraki, O Pássaro Cadáver (CHEFE)", hp_inimigo=60, defesa_inimigo=16, min_dano=5, max_dano=11, xp_recompensa=90, fraqueza="Gelo", resistencia="Físico")
    if resultado == "morte": return jogador
    layout.esperar_enter()

    # ---------------- DESAFIO 7: A PENA DO DESTINO ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "A criatura guincha e explode em uma nuvem de fumaça acre. No local de sua morte, uma única pena negra, "
        "rígida como aço e banhada em magia ancestral, flutua lentamente até suas mãos."
    )
    layout.console.print("\n[bold yellow][Item Adicionado: Pena de Aço Yokai (Material Essencial para o Cap 4)][/bold yellow]")
    if "inventario" not in jogador: jogador["inventario"] = []
    jogador["inventario"].append("Pena de Aço Yokai")
    
    layout.imprimir_lento(
        "\nVocê olha para baixo. Um lago vulcânico cerca a entrada da próxima província. Você salta, "
        "usando os galhos inferiores para amortecer a queda, finalmente montando um acampamento isolado "
        "antes dos Portões de Ferro."
    )
    
    jogador = sistemas.acampamento_fogueira(jogador, capitulo_atual=2, contexto="copas_floresta")
    layout.esperar_enter("[dim]A tela será limpa para exibir seu status atualizado...[/dim]")
    return jogador


# ==========================================
# ROTA 2: FLORESTA (CHÃO) - A LAMA E O SANGUE [ROTA DIFÍCIL]
# Rota para quem veio da Caverna (Subterrâneo)
# ==========================================
def cena_floresta_chao(jogador):
    layout.cabecalho("A FLORESTA MURMURANTE", "Os Caminhos de Lama (Rota Hostil)")

    layout.imprimir_lento(
        "Você emerge das profundezas da terra direto para o pântano inferior da Floresta Murmurante. "
        "O cheiro de enxofre das cavernas é substituído pelo odor nauseante de decomposição. "
        "A lama negra sobe até os seus calcanhares, dificultando cada passo. O céu é invisível, "
        "escondido pelo dossel de raízes e folhas milenares.\n\n"
        "Esta é a região onde o Shogunato de Cinza despeja seus prisioneiros e rituais fracassados. "
        "As árvores parecem sangrar uma seiva escura e lamuriosa."
    )
    
    # ---------------- DESAFIO 1: A NÉVOA ÁCIDA ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "Um banco de névoa verde-musgo rola sobre as águas rasas em sua direção. O cheiro queima "
        "as narinas. Você sabe que inalar isso dissolve a garganta de dentro para fora, além de "
        "ocultar dezenas de sanguessugas demoníacas (Hirudines) que aguardam na água."
    )
    layout.console.print("\n[bold]Desafio 1: A Maré Verde[/bold]")
    layout.console.print("[white]1 - [Conhecimento Dificuldade 16][/white] Identificar as correntes de vento do pântano e traçar uma rota segura e demorada pelas margens altas.")
    layout.console.print("[white]2 - [Destreza Dificuldade 17][/white] Prender a respiração, ignorar a água podre e correr em linha reta o mais rápido possível.")
    
    layout.limpar_buffer_teclado()
    esc = input("\nComo você avança? (1 ou 2): ").strip()
    
    if esc == "1":
        if sistemas.rolar_teste(jogador, "conhecimento", 16):
            layout.imprimir_lento("\n[green]Você lê as marcas nas árvores velhas, contornando perfeitamente os bolsões de gás letal sem se contaminar.[/green]")
        else:
            layout.imprimir_lento("\n[red]Você pisa em falso em um tronco oco que desaba. Você afunda na água podre, inalando gás e sendo mordido pelas sanguessugas![/red]")
            jogador["vitalidade"] -= 7
    else:
        if sistemas.rolar_teste(jogador, "destreza", 17):
            layout.imprimir_lento("\n[green]Seus pulmões queimam pela falta de ar, mas sua velocidade impressionante o tira da área de perigo antes que as feras o alcancem.[/green]")
        else:
            layout.imprimir_lento("\n[red]A lama densa trava suas pernas. O desespero o faz respirar o ar tóxico e os vermes o atacam até você se arrastar para fora.[/red]")
            jogador["vitalidade"] -= 7

    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # ---------------- DESAFIO 2: A PONTE DE OSSOS (COMBATE) ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "O pântano dá lugar a um rio de piche borbulhante. A única travessia é uma ponte pênsil, "
        "estruturada com bambu e ossos gigantescos. Bloqueando o caminho, três Ronins traidores com "
        "armaduras manchadas e veias corrompidas preparam suas armas."
    )
    resultado = sistemas.iniciar_combate(jogador, "Ronins Traidores (Corrompidos)", hp_inimigo=40, defesa_inimigo=13, min_dano=3, max_dano=8, xp_recompensa=45, fraqueza="Nenhuma", resistencia="Nenhuma")
    if resultado == "morte": return jogador
    layout.esperar_enter()

    # ---------------- DESAFIO 3: O ESPINHEIRO NEGRO E A OPALA VULCÂNICA ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "Após o rio, uma barricada natural intransponível barra o caminho: um paredão "
        "de Espinhos Negros pulsantes. Eles reagem ao Éter, chicoteando com espinhos venenosos quem se aproxima."
    )
    tem_opala = "Opala Vulcânica" in jogador.get("inventario", [])
    
    if tem_opala:
        layout.imprimir_lento(
            "\n[bold yellow]*** INTERAÇÃO DE ITEM ***[/bold yellow]\n"
            "O ambiente hostil faz a [bold red]Opala Vulcânica[/bold red] no seu inventário brilhar intensamente. "
            "Você a segura na palma da mão e a encosta nos espinhos. O calor brutal da joia das cavernas "
            "entra em reação com a corrupção da planta."
        )
        layout.imprimir_lento("\n[green]Em segundos, o espinheiro grita e murcha, virando cinzas e abrindo um túnel seguro para você! Nenhum esforço foi necessário.[/green]")
        jogador["xp"] += 20
    else:
        layout.imprimir_lento(
            "\n[red]Você não possui nenhuma fonte de calor ou item específico para lidar com a planta profana. "
            "A única opção é hackear e cortar caminho com a Kagekiri usando força bruta.[/red]"
        )
        if sistemas.rolar_teste(jogador, "kenjutsu", 18):
            layout.imprimir_lento("\n[green]Com precisão milimétrica e dezenas de golpes velozes, você abre caminho sem se arranhar.[/green]")
        else:
            layout.imprimir_lento("\n[red]Os espinhos reagem violentamente! Eles rasgam sua pele, injetando um veneno paralisante e torturante![/red]")
            jogador["vitalidade"] -= 10
            layout.console.print("[bold red]-10 de HP por mutilação venenosa.[/bold red]")

    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # ---------------- DESAFIO 4: O KAPPA FEITOR (HONRA) ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "Mais à frente, você se esconde atrás de raízes grossas. Dezenas de camponeses submersos na água "
        "suja estão sendo chicoteados para extrair seiva mágica. O feitor é um Kappa gigantesco, com "
        "espetos no casco e uma tigela na cabeça transbordando feitiçaria ácida. Salvar os camponeses "
        "chamará a fúria da besta, mas ignorá-los é manchar sua alma com o sangue dos fracos."
    )
    layout.console.print("\n[bold]Desafio 4: O Dilema dos Oprimidos[/bold]")
    layout.console.print("[white]1 - [Combater][/white] Saltar na lama e matar o feitor para libertá-los. [green](+3 Honra)[/green]")
    layout.console.print("[white]2 - [Furtividade Destreza 17][/white] Eles já estão mortos por dentro. Dar a volta e abandonar os inocentes à própria sorte. [yellow](-3 Honra)[/yellow]")
    
    layout.limpar_buffer_teclado()
    esc4 = input("\nSua escolha (1 ou 2): ").strip()
    lutou_kappa = False
    
    if esc4 == "1":
        layout.imprimir_lento("\n[dim]Seu grito de guerra cala o chicote do monstro. Você avança como um verdadeiro samurai![/dim]")
        jogador["honra"] += 3
        lutou_kappa = True
    else:
        layout.imprimir_lento("\n[dim]Você fecha o coração para a empatia e se esgueira pela borda do acampamento.[/dim]")
        jogador["honra"] -= 3
        if sistemas.rolar_teste(jogador, "destreza", 17):
            layout.imprimir_lento("\n[green]Você foge como um covarde, mas ileso. Os gritos das vítimas ecoam nas suas costas.[/green]")
        else:
            layout.imprimir_lento("\n[red]Você pisa num galho! O Kappa percebe sua presença e joga a carga de escravos para o lado, vindo direto na sua direção![/red]")
            lutou_kappa = True

    if lutou_kappa:
        resultado = sistemas.iniciar_combate(jogador, "Kappa Feitor", hp_inimigo=55, defesa_inimigo=15, min_dano=5, max_dano=10, xp_recompensa=70, fraqueza="Nenhuma", resistencia="Nenhuma")
        if resultado == "morte": return jogador
        if esc4 == "1": layout.imprimir_lento("\n[green]Os camponeses o reverenciam chorando enquanto fogem para a liberdade.[/green]")

    layout.esperar_enter()

    # ---------------- DESAFIO 5: O CEMITÉRIO FLUTUANTE ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "Você alcança uma área onde dezenas de santuários e lanternas de pedra estão afundando lentamente "
        "na lama negra. É um antigo cemitério. No instante em que você pisa ali, os espíritos vingativos "
        "acorrentados pela magia de Kuroi emergem da lama clamando por calor vital."
    )
    resultado = sistemas.iniciar_combate(jogador, "Almas Gélidas da Lama", hp_inimigo=45, defesa_inimigo=12, min_dano=4, max_dano=8, xp_recompensa=50, fraqueza="Físico", resistencia="Gelo")
    if resultado == "morte": return jogador
    layout.esperar_enter()

    # ---------------- DESAFIO 6: O NUSHI, REI DOS SAPOS (CHEFE) ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "A água barrenta recua para os lados. A terra treme, e uma montanha de verrugas purulentas, musgo "
        "e mandíbulas cavernosas emerge. É um Nushi, o Sapo Gigante corrompido, guardião soberano deste pântano. "
        "Sua língua é rápida como um chicote de aço e sua barriga é dura como rocha."
    )
    # Boss da rota difícil. Mais HP e bate muito forte.
    resultado = sistemas.iniciar_combate(jogador, "Nushi, O Rei da Lama (CHEFE EXTREMO)", hp_inimigo=80, defesa_inimigo=17, min_dano=6, max_dano=12, xp_recompensa=120, fraqueza="Gelo", resistencia="Físico")
    if resultado == "morte": return jogador
    layout.esperar_enter()

    # ---------------- DESAFIO 7: O ALTAR E A LÁGRIMA DE DRAGÃO ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "A carcaça do Nushi afunda na lama. Sob os escombros de onde ele emergiu, revela-se a entrada de um "
        "pequeno altar afogado. Você mergulha no lodo e encontra uma urna trancada por raízes. Ao parti-la, "
        "um brilho escarlate pulsante ilumina a escuridão."
    )
    layout.console.print("\n[bold yellow][Item Épico Adicionado: Lágrima do Dragão de Lama (Material Essencial para o Cap 4)][/bold yellow]")
    if "inventario" not in jogador: jogador["inventario"] = []
    jogador["inventario"].append("Lágrima de Dragão")
    
    jogador["honra"] += 2
    layout.console.print("[bold green]+2 Honra por expurgar a abominação suprema do pântano.[/bold green]")
    
    layout.imprimir_lento(
        "\nVocê sai do pântano coberto de sangue e vísceras, encontrando uma clareira de rochas vulcânicas secas "
        "pouco antes dos grandiosos Portões de Ferro. A exaustão quase desliga seu cérebro. Você desaba para montar acampamento."
    )
    
    jogador = sistemas.acampamento_fogueira(jogador, capitulo_atual=2, contexto="chao_floresta")
    layout.esperar_enter("[dim]A tela será limpa para exibir seu status atualizado...[/dim]")
    return jogador


# ==========================================
# INÍCIO E GESTOR DO CAPÍTULO 2
# ==========================================
def jogar(jogador):
    layout.cabecalho("CAPÍTULO 2", "O Desespero da Floresta Murmurante")

    layout.imprimir_lento(
        "A paisagem mudou. O ar é pesado e sufocante.\n"
        "Seu caminho é ditado pelas escolhas do passado..."
    )
    time.sleep(1)

    # Identifica a rota anterior verificando o inventário ou lógica simples.
    # Vila Gelo deu "Pingente de Gelo". Cavernas deu "Opala Vulcânica".
    inventario = jogador.get("inventario", [])
    
    if "Opala Vulcânica" in inventario:
        layout.imprimir_lento("\n[dim]Como você atravessou as Cavernas da Mandíbula, seu trajeto desemboca no chão pantanoso da floresta.[/dim]")
        layout.esperar_enter()
        jogador = cena_floresta_chao(jogador)
    else:
        # Padrão ou Pingente de Gelo
        layout.imprimir_lento("\n[dim]Como você desceu pelas Ruínas da Neve (Vila Gelo), seu trajeto o leva aos galhos superiores, o Dossel da floresta.[/dim]")
        layout.esperar_enter()
        jogador = cena_floresta_copas(jogador)

    if jogador["vitalidade"] <= 0: return jogador
    
    # --- TRANSIÇÃO PARA O CAPÍTULO 3 ---
    layout.divisoria()
    layout.imprimir_lento(
        "Com a Floresta Murmurante para trás, a terra macia dá lugar a pedras afiadas de basalto escuro. "
        "No horizonte, fumaça vulcânica tinge o céu de um vermelho doentio, e o som constante de "
        "marteladas em bigornas ecoa como o batimento cardíaco da terra.\n\n"
        "Você encontrou os Portões de Ferro Antigo. Esta é a fronteira com a Província de Tetsu, "
        "outrora o lar dos orgulhosos mestres ferreiros, agora transformada nas infames Forjas Escravocratas de Kuroi.\n\n"
        "A jornada está prestes a ficar muito mais quente..."
    )
    
    return jogador