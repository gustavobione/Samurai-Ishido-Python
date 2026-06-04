# capitulo_1.py
import layout
import sistemas

# ==========================================
# ROTA 1: A VILA CONGELADA (EXPANDIDA)
# ==========================================
def cena_vila_gelo(jogador):
    layout.cabecalho("AS RUÍNAS DE NEVE", "Ecos do Clã Shiro")
    
    layout.imprimir_lento(
        "A trilha estreita serpenteia montanha abaixo, mergulhando você em um mar de névoa pálida. "
        "A temperatura cai drasticamente, e a neve sob suas botas começa a soar como vidro quebrando.\n\n"
        "Logo, as silhuetas de pagodes arruinados emergem da tempestade. Esta é a antiga Vila de Treinamento "
        "do Clã Shiro, um lugar onde a elite militar forjava seu corpo e espírito. Agora, o silêncio é "
        "absoluto, perturbado apenas pelo uivo fantasmagórico do vento esgueirando-se pelos telhados esburacados."
    )
    
    # ------------------ DESAFIO 1 ------------------
    layout.divisoria()
    layout.imprimir_lento(
        "Para acessar o pátio principal, você deve cruzar a Grande Ponte do Suspiro. A estrutura de madeira, "
        "outrora majestosa, está petrificada por uma crosta de gelo escuro. O abismo abaixo não revela seu "
        "fundo, exalando um miasma que congela o ar."
    )
    layout.console.print("\n[bold]Desafio 1: A Ponte Congelada[/bold]")
    layout.console.print(f"[cyan]Éter Atual: {jogador.get('eter',0)}/{jogador.get('max_eter',50)}[/cyan]")
    layout.console.print("[white]1 - [Destreza Dificuldade 14][/white] Caminhar com leveza cirúrgica, sentindo as micro-fissuras no gelo antes de pisar.")
    layout.console.print("[cyan]2 - [Passos Fantasmas][/cyan] Gastar 10 de Éter para se materializar no ar, cruzando o abismo em um piscar de olhos.")
    
    layout.limpar_buffer_teclado()
    esc = input("\nComo você cruza? (1 ou 2): ").strip()
    
    if esc == "2" and jogador.get("eter", 0) >= 10:
        jogador["eter"] -= 10
        jogador.setdefault("atributos_usados", set()).add("eter")
        layout.imprimir_lento("\n[cyan]Sua forma física dissolve-se em fumaça azul. O vento tenta agarrá-lo, mas você já está do outro lado, sólido e ileso.[/cyan]")
    else:
        if esc == "2": 
            layout.imprimir_lento("\n[red]Você tenta puxar a energia da linhagem, mas o Éter falha. Você é forçado a tentar a travessia manual.[/red]")
        
        if sistemas.rolar_teste(jogador, "destreza", 14):
            layout.imprimir_lento("\n[green]Sucesso! Você desliza como uma folha ao vento, distribuindo seu peso perfeitamente até alcançar solo firme.[/green]")
        else:
            layout.imprimir_lento("\n[red]FALHA! Perto do fim, o gelo cede com um estalo ensurdecedor. Você despenca, conseguindo agarrar a borda no último segundo, mas os farpas de gelo rasgam suas mãos.[/red]")
            jogador["vitalidade"] -= 5
            layout.console.print("[red]-5 de HP pelo esforço e ferimentos.[/red]")
            
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # ------------------ DESAFIO 2 ------------------
    layout.divisoria()
    layout.imprimir_lento(
        "Pisando no pátio interno, o cheiro de morte antiga inunda suas narinas. Entre as estátuas de "
        "samurais congeladas, dois pares de olhos azuis incandescente se acendem na nevasca. "
        "Eram cães mastins da Guarda, agora bestas distorcidas pelo frio do Abismo. A carne rasgada deles "
        "revela ossos de puro gelo."
    )
    resultado = sistemas.iniciar_combate(jogador, "Matilha Corrompida (2 Lobos)", hp_inimigo=30, defesa_inimigo=12, min_dano=2, max_dano=6, xp_recompensa=35, fraqueza="Fogo", resistencia="Gelo")
    if resultado == "morte": return jogador
    layout.esperar_enter()

    # ------------------ DESAFIO 3 ------------------
    layout.divisoria()
    layout.imprimir_lento(
        "Com as bestas abatidas, a tempestade repentinamente ganha força, criando um ciclone impenetrável "
        "que bloqueia o caminho para o Templo Superior. No centro do pátio, pendurado por correntes "
        "enferrujadas, há o Sino do Guardião, coberto por séculos de geada mágica. A lenda diz que seu som "
        "apazigua os espíritos da montanha."
    )
    layout.console.print("\n[bold]Desafio 3: O Sino Congelado[/bold]")
    layout.console.print("[white]1 - [Kenjutsu Dificuldade 15][/white] Usar a força bruta e o cabo da espada como martelo para quebrar o gelo e ecoar o sino.")
    layout.console.print("[white]2 - [Conhecimento Dificuldade 14][/white] Encontrar os pontos de ressonância corretos no bronze para dissipar a magia sem esforço físico.")
    
    layout.limpar_buffer_teclado()
    esc_sino = input("\nSua ação (1 ou 2): ").strip()
    
    if esc_sino == "1":
        if sistemas.rolar_teste(jogador, "kenjutsu", 15):
            layout.imprimir_lento("\n[green]Com um golpe estrondoso, as correntes tremem e o gelo se estilhaça em mil pedaços! O tom grave do sino rasga a tempestade, abrindo caminho.[/green]")
        else:
            layout.imprimir_lento("\n[red]O impacto é imperfeito. O gelo absorve o choque, e uma onda de frio rebota pelo seu braço, causando danos aos seus músculos antes de finalmente soar.[/red]")
            jogador["vitalidade"] -= 3
    else:
        if sistemas.rolar_teste(jogador, "conhecimento", 14):
            layout.imprimir_lento("\n[green]Você dedilha o bronze, sentindo a malha mágica. Um toque preciso com a Kagekiri anula a runa invisível. O sino soa puro e cristalino, acalmando os ventos.[/green]")
        else:
            layout.imprimir_lento("\n[red]Sua mente falha em decifrar os padrões. Ao tocar o sino no ponto errado, uma explosão de energia gélida o arremessa para trás.[/red]")
            jogador["vitalidade"] -= 3
            
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # ------------------ DESAFIO 4 ------------------
    layout.divisoria()
    layout.imprimir_lento(
        "A névoa se dissipa o suficiente para revelar o Templo Superior, mas algo está errado. "
        "Uma intenção assassina pesa no ar. Acima, no telhado curvado de um santuário menor, um Espectro "
        "Arqueiro retesa um arco enorme. A flecha negra já está apontada para o seu peito.\n"
        "Exatamente acima do atirador, uma imensa gárgula de pedra, afrouxada pelo tempo, balança."
    )
    layout.console.print("\n[bold]Desafio 4: A Emboscada do Arqueiro[/bold]")
    layout.console.print("[white]1 - [Conhecimento Dificuldade 16][/white] Lançar uma kunai na gárgula, esmagando o atirador antes que ele o veja. Assassinar sem chance de defesa. [yellow](Custa Honra)[/yellow]")
    layout.console.print("[white]2 - [Kenjutsu Dificuldade 17][/white] Avançar de frente, brandindo a lâmina para desviar a flecha e fatiá-lo. [green](Ganha Honra)[/green]")
    
    layout.limpar_buffer_teclado()
    esc2 = input("\nSua reação (1 ou 2): ").strip()
    lutou_arqueiro = False
    
    if esc2 == "1":
        if sistemas.rolar_teste(jogador, "conhecimento", 16):
            layout.imprimir_lento("\n[green]A Kunai atinge a junção da estátua. A gárgula desaba em silêncio, esmagando o espectro. Um abate perfeito.[/green]")
            jogador["xp"] += 30
            jogador["honra"] -= 1
            layout.console.print("[bold yellow]+30 XP. A mancha da covardia suja seu espírito. (-1 Honra)[/bold yellow]")
        else:
            layout.imprimir_lento("\n[red]A kunai resvala na pedra. O atirador percebe o ataque e dispara uma flecha que rasga seu ombro![/red]")
            jogador["vitalidade"] -= 5
            lutou_arqueiro = True
    else:
        if sistemas.rolar_teste(jogador, "kenjutsu", 17):
            layout.imprimir_lento("\n[green]Você encara a morte. Num movimento fluido, rebate a flecha no ar, usa os detritos para saltar até o telhado e corta o arqueiro ao meio![/green]")
            jogador["xp"] += 30
            jogador["honra"] += 1 
            layout.console.print("[bold green]+30 XP. Você agiu sob a luz da espada, honrando os ancestrais! (+1 Honra)[/bold green]")
        else:
            layout.imprimir_lento("\n[red]Seus reflexos falham. A flecha quebra sua guarda e crava profundamente no seu flanco![/red]")
            jogador["vitalidade"] -= 5
            lutou_arqueiro = True

    if lutou_arqueiro and jogador["vitalidade"] > 0:
        resultado = sistemas.iniciar_combate(jogador, "Espectro Arqueiro", hp_inimigo=15, defesa_inimigo=12, min_dano=3, max_dano=7, xp_recompensa=20, fraqueza="Físico", resistencia="Nenhuma")
        if resultado == "morte": return jogador
        
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # ------------------ DESAFIO 5 ------------------
    layout.divisoria()
    layout.imprimir_lento(
        "Finalmente, você pisa nas escadarias do dojo principal. O portão duplo foi arrancado das dobradiças. "
        "No interior escurecido, as antigas brasas se acendem com uma chama azul doentia. "
        "Uma figura colossal se levanta lentamente das sombras. Uma armadura oca, preenchida com um furacão "
        "de neve e ódio. O Tenente Espectral Shiro arrasta sua Nodachi pelo piso de madeira, "
        "gritando em uma língua que mistura lamento e raiva."
    )
    resultado = sistemas.iniciar_combate(jogador, "Tenente Shiro (CHEFE)", hp_inimigo=45, defesa_inimigo=15, min_dano=4, max_dano=9, xp_recompensa=80, fraqueza="Físico", resistencia="Gelo")
    
    if resultado == "vitoria":
        layout.imprimir_lento(
            "\nCom um último golpe da Kagekiri, a ligação espiritual da armadura é cortada. "
            "A neve cessa abruptamente. As placas de aço caem pesadamente pelo dojo. "
            "Sob os restos do peitoral, você nota algo brilhando."
        )
        layout.imprimir_lento(
            "É um medalhão ancestral preservado. Ao tocá-lo, imagens de um passado orgulhoso "
            "inundam sua mente, lembrando-o de quem você realmente é."
        )
        jogador["honra"] += 2
        layout.console.print("\n[bold green]+2 de Honra pela purificação do templo.[/bold green]")
        layout.console.print("[bold yellow][Item Adicionado: Pingente de Gelo Eterno (Passiva: +2 Defesa)][/bold yellow]")
        
        if "inventario" not in jogador: jogador["inventario"] = []
        jogador["inventario"].append("Pingente de Gelo")
        jogador["bonus_defesa"] += 2
        
        layout.esperar_enter()
        
        layout.imprimir_lento(
            "A exaustão toma conta do seu corpo. Atrás do dojo, há um pequeno altar de pedra abrigado "
            "do vento, perfeito para montar acampamento antes de seguir viagem."
        )
        # Acampamento
        jogador = sistemas.acampamento_fogueira(jogador, capitulo_atual=1, contexto="vila_gelo")

    # Espera antes de sair da rota, para o jogador ler como ficou a fogueira
    layout.esperar_enter("[dim]A tela será limpa para exibir seu status atualizado...[/dim]")
    return jogador

# ==========================================
# ROTA 2: AS CAVERNAS DA MANDÍBULA
# ==========================================
def cena_caverna(jogador):
    layout.cabecalho("AS CAVERNAS DA MANDÍBULA", "Trevas Primordiais")
    
    layout.imprimir_lento(
        "A encosta direita da montanha não possui escadas esculpidas, apenas uma fissura natural "
        "na rocha escura que parece engolir a luz. O ar quente e úmido que sobe das profundezas "
        "cheira a minérios antigos e putrefação. Você mergulha na escuridão, onde ecos de gotas d'água "
        "soam como o tique-taque de um relógio fúnebre."
    )

    # ------------------ DESAFIO 1 ------------------
    layout.divisoria()
    layout.imprimir_lento(
        "Após minutos de descida, a passagem se estreita e os túneis ganham uma tonalidade esverdeada. "
        "À sua frente, uma espessa nuvem de fumaça tóxica flutua rente ao solo. É o Sopro do Abismo, um "
        "gás paralisante que derrete lentamente os pulmões de quem tenta respirar ali."
    )
    layout.console.print("\n[bold]Desafio 1: O Miasma Sufocante[/bold]")
    layout.console.print("[white]1 - [Destreza Dificuldade 15][/white] Prender a respiração e correr cegamente, desviando das rochas escorregadias até o outro lado.")
    layout.console.print("[white]2 - [Conhecimento Dificuldade 14][/white] Rasgar um pedaço do seu kimono e utilizar terra úmida com minerais da caverna para criar um filtro de ar improvisado.")
    
    layout.limpar_buffer_teclado()
    esc = input("\nComo você atravessa? (1 ou 2): ").strip()
    
    if esc == "1":
        if sistemas.rolar_teste(jogador, "destreza", 15):
            layout.imprimir_lento("\n[green]Seus pulmões queimam, e as pernas pedem socorro, mas você emerge do outro lado, tossindo a salvo da nuvem mortal.[/green]")
        else:
            layout.imprimir_lento("\n[red]Você tropeça em uma estalagmite no escuro! O ar foge dos pulmões e você inala o veneno profano, cambaleando até a saída.[/red]")
            jogador["vitalidade"] -= 6
            layout.console.print("[red]-6 de HP por danos pulmonares e escoriações.[/red]")
    else:
        if sistemas.rolar_teste(jogador, "conhecimento", 14):
            layout.imprimir_lento("\n[green]O tecido filtra perfeitamente a toxicidade. Você caminha em segurança pelo gás, com a respiração fria, mas limpa.[/green]")
        else:
            layout.imprimir_lento("\n[red]Você mistura a terra errada. A composição não segura o veneno e queima seu rosto, obrigando você a correr em pânico para o fim do túnel![/red]")
            jogador["vitalidade"] -= 5
            layout.console.print("[red]-5 de HP por envenenamento leve.[/red]")

    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # ------------------ DESAFIO 2 ------------------
    layout.divisoria()
    layout.imprimir_lento(
        "A fumaça fica para trás, revelando uma câmara colossal. O piso desaparece num buraco negro. "
        "A única forma de prosseguir é por meio de pilares de rocha vulcânica dispersos pelo abismo, "
        "pouco iluminados por fungos bioluminescentes."
    )
    layout.console.print("\n[bold]Desafio 2: A Ponte Quebrada do Vazio[/bold]")
    layout.console.print(f"[cyan]Éter Atual: {jogador.get('eter',0)}/{jogador.get('max_eter',50)}[/cyan]")
    layout.console.print("[white]1 - [Destreza Dificuldade 16][/white] Fazer uma série de saltos calculados sobre os pilares instáveis.")
    layout.console.print("[cyan]2 - [Passos Fantasmas][/cyan] Gastar 10 de Éter para teleportar de um lado ao outro, sem correr riscos físicos.")

    layout.limpar_buffer_teclado()
    esc2 = input("\nComo você cruza o abismo? (1 ou 2): ").strip()
    
    if esc2 == "2" and jogador.get("eter", 0) >= 10:
        jogador["eter"] -= 10
        jogador.setdefault("atributos_usados", set()).add("eter")
        layout.imprimir_lento("\n[cyan]Canalizando seu sangue, o mundo perde a cor e você surge milagrosamente na borda segura do outro lado.[/cyan]")
    else:
        if esc2 == "2": 
            layout.imprimir_lento("\n[red]Você tenta puxar a energia da linhagem, mas sua mente falha. Você precisa saltar.[/red]")
            
        if sistemas.rolar_teste(jogador, "destreza", 16):
            layout.imprimir_lento("\n[green]Seus saltos são precisos como os de um predador. A pedra cede apenas segundos depois que suas botas a abandonam.[/green]")
        else:
            layout.imprimir_lento("\n[red]Um pilar se esfarela. Você despenca, conseguindo cravar a Kagekiri na parede de pedra metros abaixo, mas luxando o ombro no processo e precisando escalar o resto.[/red]")
            jogador["vitalidade"] -= 5
            layout.console.print("[red]-5 de HP pela queda.[/red]")

    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # ------------------ DESAFIO 3 ------------------
    layout.divisoria()
    layout.imprimir_lento(
        "Você adentra corredores de cristal maciço. Porém, o som de garras arranhando o vidro ecoa. "
        "Do teto despencam horrores aracnídeos gigantes, suas carapaças formadas por quartzo espinhoso "
        "e presas gotejando ácido corrosivo."
    )
    resultado = sistemas.iniciar_combate(jogador, "Aranhas de Cristal (3 Obreiras)", hp_inimigo=35, defesa_inimigo=11, min_dano=2, max_dano=7, xp_recompensa=40, fraqueza="Físico", resistencia="Gelo")
    if resultado == "morte": return jogador
    layout.esperar_enter()

    # ------------------ DESAFIO 4 ------------------
    layout.divisoria()
    layout.imprimir_lento(
        "Atrás da toca das aranhas, escondido pelo tempo, repousa o Altar Obsceno. Estátuas bestiais "
        "de onis distorcidos cercam uma bacia cheia de um líquido vermelho incandescente. O altar sussurra "
        "na sua mente, prometendo restaurar sua força mágica em troca do sangue fresco da sua ferida."
    )
    layout.console.print("\n[bold]Desafio 4: A Barganha do Abismo[/bold]")
    layout.console.print("[white]1 - [Oferecer o próprio Sangue][/white] Cortar a mão e derramar na bacia. Restaura todo o seu Éter e dá XP, mas [yellow]Custa muita Honra[/yellow].")
    layout.console.print("[white]2 - [Kenjutsu Dificuldade 18][/white] Repudiar a oferta profana e tentar destruir o altar pagão com um golpe de espada. [green](Ganha Honra)[/green]")
    
    layout.limpar_buffer_teclado()
    esc4 = input("\nQual a sua escolha? (1 ou 2): ").strip()
    
    if esc4 == "1":
        layout.imprimir_lento("\n[dim]A lâmina corta sua palma. O sangue cai na bacia, sibilando. O líquido sobe pelo seu braço em formato de sombras, inundando sua mente com poder vil.[/dim]")
        jogador["vitalidade"] -= 4
        jogador["eter"] = jogador.get("max_eter", 50)
        jogador["xp"] += 35
        jogador["honra"] -= 3
        layout.console.print("[bold yellow]Éter totalmente restaurado. +35 XP. Sua ligação com as artes das trevas se estreita. (-3 Honra, -4 HP)[/bold yellow]")
    else:
        if sistemas.rolar_teste(jogador, "kenjutsu", 18):
            layout.imprimir_lento("\n[green]Seu rugido abafa as vozes! A Kagekiri desce impiedosa partindo o altar e a bacia ao meio. A magia das trevas se dissolve.[/green]")
            jogador["xp"] += 30
            jogador["honra"] += 2
            layout.console.print("[bold green]+30 XP. Você manteve sua integridade moral inabalável. (+2 Honra)[/bold green]")
        else:
            layout.imprimir_lento("\n[red]Sua espada bate na pedra e ricocheteia! O altar revida sua agressão, disparando um relâmpago rubro contra seu peito![/red]")
            jogador["vitalidade"] -= 6
            layout.console.print("[red]-6 de HP por retribuição mágica profana.[/red]")

    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # ------------------ DESAFIO 5 ------------------
    layout.divisoria()
    layout.imprimir_lento(
        "No fundo da galeria final da caverna encontra-se um lago subterrâneo sem vida. Mas assim que você "
        "se aproxima da margem, a água começa a ferver e recuar. Uma enorme rocha se ergue do solo, "
        "revelando braços musculosos compostos de granito negro e carne pútrida. O Guardião das Profundezas, "
        "um Golém distorcido por corrupção anciã, se coloca entre você e a saída da montanha."
    )
    resultado = sistemas.iniciar_combate(jogador, "Golém das Profundezas (CHEFE)", hp_inimigo=50, defesa_inimigo=16, min_dano=5, max_dano=10, xp_recompensa=90, fraqueza="Nenhuma", resistencia="Físico")
    
    if resultado == "vitoria":
        layout.imprimir_lento(
            "\nO colosso emite um grunhido profundo antes de se desfazer em uma pilha de escombros inúteis. "
            "No núcleo do peito de pedra do monstro, incrustado, há uma joia brilhante."
        )
        layout.imprimir_lento(
            "Você a arranca. É uma Opala Vulcânica, quente ao toque, emanando uma força vigorosa."
        )
        jogador["honra"] += 1
        layout.console.print("\n[bold green]+1 de Honra por eliminar uma abominação antiga.[/bold green]")
        layout.console.print("[bold yellow][Item Adicionado: Opala Vulcânica (+5 HP Máximo)][/bold yellow]")
        
        # Atualização correta do Inventário e Status
        if "inventario" not in jogador: jogador["inventario"] = []
        jogador["inventario"].append("Opala Vulcânica")
        jogador["max_vitalidade"] += 5
        jogador["vitalidade"] += 5
        
        layout.esperar_enter()
        
        layout.imprimir_lento(
            "As pedras colapsadas do golem fornecem abrigo perfeito contra a umidade da caverna. "
            "Exausto da jornada subterrânea, você raspa algumas pedras de sílex para fazer uma pequena fogueira."
        )
        # Acampamento
        jogador = sistemas.acampamento_fogueira(jogador, capitulo_atual=1, contexto="caverna")

    # Espera antes de sair da rota, para o jogador ler como ficou a fogueira
    layout.esperar_enter("[dim]A tela será limpa para exibir seu status atualizado...[/dim]")
    return jogador

# ==========================================
# INÍCIO DO CAPÍTULO 1
# ==========================================
def jogar(jogador):
    layout.cabecalho("CAPÍTULO 1", "O Despertar do Mundo")

    layout.imprimir_lento(
        "A tempestade no cume finalmente ficou para trás. "
        "Você chega à encruzilhada na encosta da montanha. O vento sopra em duas direções distintas.\n\n"
        "À esquerda, o caminho desce em direção aos escombros da antiga vila de treinamento militar, "
        "congelada no tempo e envolta em uma névoa densa e uivante. O orgulho passado do seu clã jaz lá.\n\n"
        "À direita, os portões de pedra desmoronados para as Cavernas da Mandíbula escancaram a escuridão. "
        "Um abismo subterrâneo repleto de lendas de horrores rastejantes e rituais profanos."
    )

    layout.console.print("\n[bold]Qual caminho você escolherá para a descida?[/bold]")
    layout.console.print("[white]1 - A Vila de Treinamento (A Rota das Ruínas de Neve).[/white]")
    layout.console.print("[white]2 - As Cavernas da Mandíbula (A Rota das Trevas Subterrâneas).[/white]")

    escolha_caminho = ""
    while escolha_caminho not in ["1", "2"]:
        layout.limpar_buffer_teclado()
        escolha_caminho = input("\nEscolha (1 ou 2): ").strip()

    if escolha_caminho == "1":
        jogador = cena_vila_gelo(jogador)
    elif escolha_caminho == "2":
        jogador = cena_caverna(jogador)

    return jogador