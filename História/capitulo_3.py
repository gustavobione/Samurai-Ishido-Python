# capitulo_3.py
import layout
import sistemas

# ==========================================
# ROTA 1: AS MINAS INFERIORES (Foco em Furtividade/Sobrevivência)
# ==========================================
def cena_minas(jogador):
    layout.cabecalho("AS MINAS DE ENXOFRE", "O Peso do Aço")

    layout.imprimir_lento(
        "Você opta pelos dutos de ventilação inferiores, esgueirando-se pelas Minas de Enxofre. "
        "O calor é sufocante, fazendo o suor arder nos olhos. O eco rítmico das picaretas soa "
        "como o bater de um coração doente. Dezenas de humanos escravizados, reduzidos a pele e osso, "
        "quebram rochas vulcânicas sob o olhar cruel de Magistrados de Ferro."
    )
    
    # --- DESAFIO 1: Gás Tóxico ---
    layout.divisoria()
    layout.imprimir_lento("Um bolsão de gás de enxofre invisível bloqueia o túnel principal. O ar ondula com a toxina.")
    layout.console.print("\n[bold]Desafio 1: O Suspiro do Vulcão[/bold]")
    layout.console.print("[white]1 - [Conhecimento Dificuldade 16][/white] Ler as correntes térmicas para contornar o gás pelas reentrâncias superiores.")
    layout.console.print("[cyan]2 - [Passos Fantasmas][/cyan] Gastar 10 de Éter para cruzar a área rapidamente em forma etérea.")
    
    layout.limpar_buffer_teclado()
    esc1 = input("\nSua ação (1 ou 2): ").strip()
    if esc1 == "2" and jogador.get("eter", 0) >= 10:
        jogador["eter"] -= 10
        jogador.setdefault("atributos_usados", set()).add("eter")
        layout.imprimir_lento("\n[cyan]Você vira fumaça e atravessa o gás tóxico ileso.[/cyan]")
    else:
        if esc1 == "2": layout.imprimir_lento("\n[red]Éter insuficiente.[/red]")
        if sistemas.rolar_teste(jogador, "conhecimento", 16):
            layout.imprimir_lento("\n[green]Você escala a parede fria, mantendo o rosto longe da fumaça densa que se acumula no chão.[/green]")
        else:
            layout.imprimir_lento("\n[red]Você escorrega. Uma lufada de enxofre invade seus pulmões! Você tosse sangue e avança cambaleando.[/red]")
            jogador["vitalidade"] -= 5
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 2: O Escravo e o Feitor ---
    layout.divisoria()
    layout.imprimir_lento("Abaixo do seu esconderijo, um ancião colapsa. O Feitor levanta um porrete cravejado para esmagar o crânio do escravo.")
    layout.console.print("\n[bold]Desafio 2: A Punição Injusta[/bold]")
    layout.console.print("[white]1 - [Atacar][/white] Pular e assassinar o guarda brutalmente. [green](+2 Honra)[/green]")
    layout.console.print("[white]2 - [Destreza Dificuldade 18][/white] Eles já estão mortos por dentro. Passar despercebido pelas sombras. [yellow](-2 Honra)[/yellow]")
    
    layout.limpar_buffer_teclado()
    if input("\nSua escolha (1 ou 2): ").strip() == "1":
        jogador["honra"] += 2
        layout.imprimir_lento("\n[dim]Você cai como um raio prateado![/dim]")
        sistemas.iniciar_combate(jogador, "Feitor das Minas", hp_inimigo=35, defesa_inimigo=13, min_dano=3, max_dano=7, xp_recompensa=40, fraqueza="Nenhuma", resistencia="Nenhuma")
    else:
        jogador["honra"] -= 2
        layout.imprimir_lento("\n[dim]Você ouve o som repulsivo de ossos quebrando enquanto ignora o sofrimento alheio.[/dim]")
        if not sistemas.rolar_teste(jogador, "destreza", 18):
            layout.imprimir_lento("\n[red]O sangue do ancião espirra na sua perna, fazendo você tropeçar. O Feitor te vê![/red]")
            sistemas.iniciar_combate(jogador, "Feitor Sanguinário", hp_inimigo=40, defesa_inimigo=14, min_dano=4, max_dano=8, xp_recompensa=45)
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 3: O Rio de Escória ---
    layout.divisoria()
    layout.imprimir_lento("Um fosso profundo cheio de escória de metal incandescente bloqueia o túnel. A única travessia é uma corrente enferrujada bamba.")
    if sistemas.rolar_teste(jogador, "destreza", 15):
        layout.imprimir_lento("\n[green]Você cruza a corrente com o equilíbrio de um gato das montanhas.[/green]")
    else:
        layout.imprimir_lento("\n[red]A corrente cede de um lado! Você fica pendurado e o calor do fosso queima suas botas antes de subir de volta![/red]")
        jogador["vitalidade"] -= 5
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 4: INTERAÇÃO DE ITEM - O Portão de Magma ---
    layout.divisoria()
    layout.imprimir_lento("Uma grade de ferro maciço, aquecida a ponto de brilhar em vermelho-cereja, sela a passagem. Tocar nela derreteria seus ossos.")
    if "Pingente de Gelo" in jogador.get("inventario", []):
        layout.imprimir_lento(
            "\n[bold cyan]*** O PINGENTE DE GELO REAGE ***[/bold cyan]\n"
            "A joia fria no seu pescoço pulsa. Você a tira e pressiona contra a fechadura de ferro incandescente. "
            "O choque térmico é instantâneo e violento. A fechadura estala e quebra, congelada e quebradiça. Você chuta o portão e ele se abre."
        )
        jogador["xp"] += 30
    else:
        layout.imprimir_lento("\n[red]Sem magia de gelo para resfriar a barra, você é forçado a usar a Kagekiri como alavanca e seu próprio corpo para empurrar as grades.[/red]")
        if sistemas.rolar_teste(jogador, "kenjutsu", 18):
            layout.imprimir_lento("\n[green]Com dor agonizante, você deforma as grades o suficiente para passar.[/green]")
        else:
            layout.imprimir_lento("\n[red]A grade derrete sua luva e queima a carne de seus braços severamente![/red]")
            jogador["vitalidade"] -= 8
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 5: Mastim de Ferro ---
    layout.divisoria()
    layout.imprimir_lento("O som do portão acorda um cão de guarda da forja, um construto de ferro e magma. Ele avança babando fogo!")
    sistemas.iniciar_combate(jogador, "Mastim de Ferro", hp_inimigo=40, defesa_inimigo=15, min_dano=3, max_dano=8, xp_recompensa=45, fraqueza="Gelo", resistencia="Fogo")
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 6: O Carrinho Desgovernado ---
    layout.divisoria()
    layout.imprimir_lento("Os trilhos da mina começam a tremer. Um carrinho de minério em chamas desce desgovernado na sua direção no túnel estreito!")
    if sistemas.rolar_teste(jogador, "destreza", 17):
        layout.imprimir_lento("\n[green]No último milésimo de segundo, você desliza por baixo do carrinho passando ileso![/green]")
    else:
        layout.imprimir_lento("\n[red]Você se joga na parede, mas as chamas o atingem em cheio![/red]")
        jogador["vitalidade"] -= 6
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 7: O Ferreiro Cego (AQUISIÇÃO DE ITEM CAP 4) ---
    layout.divisoria()
    layout.imprimir_lento(
        "Você entra numa caverna lateral. Acorrentado a uma bigorna, um ferreiro escravo cego nota seus passos.\n"
        "'A respiração... O leve tilintar do aço meteórico. Você porta a Kagekiri, não é? O sangue Shiro vive.'\n"
        "Ele tosse fuligem. 'Não há esperança aqui. Mas leve isso. Quando o aço falhar, a sombra prevalecerá.'"
    )
    layout.console.print("\n[bold yellow][Item Adicionado: Bomba de Fumaça Alquímica (Crucial para Fuga no Cap 4)][/bold yellow]")
    jogador.setdefault("inventario", []).append("Bomba de Fumaca")
    layout.esperar_enter()

    # --- DESAFIO 8: A Patrulha de Elite ---
    layout.divisoria()
    layout.imprimir_lento("Aproximando-se da câmara principal, um esquadrão de Guardas de Elite marcha em patrulha.")
    if sistemas.rolar_teste(jogador, "conhecimento", 17):
        layout.imprimir_lento("\n[green]Você calcula o tempo dos passos deles, escondendo-se atrás de um pilar de obsidiana até passarem.[/green]")
    else:
        layout.imprimir_lento("\n[red]Uma pedra solta chuta o chão. A patrulha vira![/red]")
        sistemas.iniciar_combate(jogador, "Guarda Corrompido", hp_inimigo=35, defesa_inimigo=14, min_dano=4, max_dano=7, xp_recompensa=35)
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 9: O Capataz das Minas (Sub-Boss) ---
    layout.divisoria()
    layout.imprimir_lento("Guardando a porta do núcleo do vulcão está o Capataz das Minas, brandindo um chicote flamejante.")
    sistemas.iniciar_combate(jogador, "Capataz Enraivecido", hp_inimigo=50, defesa_inimigo=15, min_dano=5, max_dano=10, xp_recompensa=70, fraqueza="Gelo", resistencia="Fogo")
    
    return jogador


# ==========================================
# ROTA 2: A FORJA PRINCIPAL (Foco em Ação e Brutalidade)
# ==========================================
def cena_forja(jogador):
    layout.cabecalho("AS FORJAS ESCRAVOCRATAS", "A Sinfonia do Aço")

    layout.imprimir_lento(
        "Você avança pelos portões imensos da Forja Principal. Rios de metal derretido fluem como cachoeiras. "
        "A sinfonia de mil martelos batendo simultaneamente no aço ecoa nas paredes cavernosas. "
        "Magistrados Demônios administram a criação de armamentos para o exército sombrio de Kuroi."
    )
    
    # --- DESAFIO 1: A Chuva de Faíscas ---
    layout.divisoria()
    layout.imprimir_lento("O martelar mecânico das bigornas gigantes lança ondas de faíscas incandescentes em intervalos regulares na ponte de entrada.")
    if sistemas.rolar_teste(jogador, "destreza", 16):
        layout.imprimir_lento("\n[green]Você memoriza o padrão rítmico e dança entre as ondas de fogo sem se queimar.[/green]")
    else:
        layout.imprimir_lento("\n[red]Você é pego por uma lufada de faíscas afiadas que penetram suas roupas![/red]")
        jogador["vitalidade"] -= 5
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 2: Escórias Vivas ---
    layout.divisoria()
    layout.imprimir_lento("O resíduo mágico das forjas ganha vida. Duas massas de escória fervente se erguem, assumindo formas bestiais.")
    sistemas.iniciar_combate(jogador, "Golems de Escória (2x)", hp_inimigo=45, defesa_inimigo=12, min_dano=4, max_dano=7, xp_recompensa=50, fraqueza="Gelo", resistencia="Físico")
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 3: O Andaime Colapsando ---
    layout.divisoria()
    layout.imprimir_lento("A luta desestabiliza o andaime de madeira petrificada. Ele começa a colapsar em direção ao rio de aço derretido!")
    if sistemas.rolar_teste(jogador, "destreza", 18):
        layout.imprimir_lento("\n[green]Pulando de viga em viga em queda livre, você crava a espada na parede sólida e se puxa para cima.[/green]")
    else:
        layout.imprimir_lento("\n[red]Você não é rápido o bastante! Seus pés afundam no calor absurdo por um segundo antes de você conseguir saltar![/red]")
        jogador["vitalidade"] -= 8
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 4: INTERAÇÃO DE ITEM - O Fogo Vivo ---
    layout.divisoria()
    layout.imprimir_lento("O caminho é barrado por uma Parede de Chama Viva, um feitiço de segurança dos ferreiros sombrios.")
    if "Pingente de Gelo" in jogador.get("inventario", []):
        layout.imprimir_lento(
            "\n[bold cyan]*** O PINGENTE DE GELO REAGE ***[/bold cyan]\n"
            "O Pingente irradia uma aura congelante. Você caminha em direção às chamas. Onde você pisa, o fogo cede, "
            "transformando-se em fumaça inofensiva. A relíquia de sua terra gélida o protegeu perfeitamente."
        )
        jogador["xp"] += 30
    else:
        layout.imprimir_lento("\n[red]Sem o Pingente de Gelo, você cruza os braços e tenta correr pelo inferno mágico na pura força de vontade.[/red]")
        if sistemas.rolar_teste(jogador, "kenjutsu", 18):
            layout.imprimir_lento("\n[green]Sua aura espiritual rebate parte do fogo mágico, mas você ainda se queima.[/green]")
            jogador["vitalidade"] -= 4
        else:
            layout.imprimir_lento("\n[red]O fogo vivo se enrola no seu corpo, causando queimaduras de terceiro grau![/red]")
            jogador["vitalidade"] -= 10
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 5: Acólito da Chama Negra ---
    layout.divisoria()
    layout.imprimir_lento("Protegendo a próxima seção, um feiticeiro da forja prepara um ritual de chamas profanas.")
    sistemas.iniciar_combate(jogador, "Acólito da Chama Negra", hp_inimigo=35, defesa_inimigo=11, min_dano=5, max_dano=12, xp_recompensa=45, fraqueza="Físico", resistencia="Fogo")
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 6: O Relicário Roubado ---
    layout.divisoria()
    layout.imprimir_lento("Você encontra um carrinho contendo katanas cerimoniais roubadas dos antigos clãs, prestes a serem derretidas.")
    layout.console.print("\n[bold]Desafio 6: Memórias Profanadas[/bold]")
    layout.console.print("[white]1 - [Ação][/white] Tomar tempo para resgatar os brasões das espadas e honrar os mortos. [green](+3 Honra, Risco de dano)[/green]")
    layout.console.print("[white]2 - [Ação][/white] Ignorar. Sua missão é maior que aço velho. [yellow](-2 Honra)[/yellow]")
    
    layout.limpar_buffer_teclado()
    if input("\nSua escolha (1 ou 2): ").strip() == "1":
        jogador["honra"] += 3
        if sistemas.rolar_teste(jogador, "conhecimento", 15):
            layout.imprimir_lento("\n[green]Você resgata os brasões com destreza antes do carrinho afundar no magma.[/green]")
        else:
            layout.imprimir_lento("\n[red]O calor extremo estilhaça um metal perto de você, perfurando seu rosto.[/red]")
            jogador["vitalidade"] -= 4
    else:
        jogador["honra"] -= 2
        layout.imprimir_lento("\n[dim]Você dá as costas ao passado, o olhar fixo apenas na vingança.[/dim]")
    layout.esperar_enter()

    # --- DESAFIO 7: O Traidor da Forja (AQUISIÇÃO DE ITEM CAP 4) ---
    layout.divisoria()
    layout.imprimir_lento(
        "Um Magistrado ferido rasteja até você. Ele desertou as fileiras após se recusar a queimar crianças.\n"
        "'Samurai... mate o General... vingue minha covardia.' Ele estende um cinto pesado com uma corrente modificada.\n"
        "'Isso me permitia andar pelas estruturas altas. Use para fugir quando a montanha cair.'"
    )
    layout.console.print("\n[bold yellow][Item Adicionado: Arpéu de Corrente (Crucial para Fuga no Cap 4)][/bold yellow]")
    jogador.setdefault("inventario", []).append("Arpeu de Corrente")
    layout.esperar_enter()

    # --- DESAFIO 8: O Fole do Inferno ---
    layout.divisoria()
    layout.imprimir_lento("Para chegar ao núcleo, você deve passar pelo Fole Principal, que lança lufadas de ar superaquecido que cortam como navalhas.")
    if sistemas.rolar_teste(jogador, "destreza", 17):
        layout.imprimir_lento("\n[green]Você calcula o timing perfeito, correndo entre os sopros escaldantes.[/green]")
    else:
        layout.imprimir_lento("\n[red]Você é pego no meio de um sopro! O ar ferve seus pulmões.[/red]")
        jogador["vitalidade"] -= 6
    if jogador["vitalidade"] <= 0: return jogador
    layout.esperar_enter()

    # --- DESAFIO 9: Centurião de Bronze (Sub-Boss) ---
    layout.divisoria()
    layout.imprimir_lento("O último protetor do portão do núcleo é um autômato monstruoso de bronze, armado com um machado térmico.")
    sistemas.iniciar_combate(jogador, "Centurião de Bronze", hp_inimigo=55, defesa_inimigo=16, min_dano=5, max_dano=9, xp_recompensa=75, fraqueza="Gelo", resistencia="Físico")
    
    return jogador


# ==========================================
# O CLÍMAX: O CORAÇÃO DO VULCÃO E A QUEBRA DO HERÓI
# ==========================================
def cena_climax(jogador):
    if jogador["vitalidade"] <= 0: return jogador
    
    layout.cabecalho("O CORAÇÃO DO VULCÃO", "A Fornalha de Kuroi")

    layout.imprimir_lento(
        "Independente da rota, as gigantescas portas de ferro fundido se abrem para o núcleo do vulcão.\n"
        "Um mar revolto de magma borbulha no fundo de uma cratera massiva. No centro de uma ponte de "
        "obsidiana paira o General En'enra. Seu corpo oscila entre fumaça tóxica, rocha vulcânica e "
        "pura magia corrompida. Ele carrega uma lança que goteja metal líquido."
    )
    
    layout.imprimir_lento("\n[bold yellow]'O herdeiro Shiro... Sua linhagem gélida evaporará sob minhas mãos!'[/bold yellow]")
    
    # Combate Épico do Boss
    resultado = sistemas.iniciar_combate(jogador, "General En'enra, O Arauto do Magma (CHEFE)", hp_inimigo=85, defesa_inimigo=16, min_dano=6, max_dano=13, xp_recompensa=150, fraqueza="Gelo", resistencia="Físico")
    
    if resultado == "morte" or jogador["vitalidade"] <= 0: return jogador
    
    # ==============================================================
    # EVENTO NARRATIVO CHAVE: A ESPADA QUEBRA
    # ==============================================================
    layout.cabecalho("O ESTILHAÇAR DA ESPERANÇA", "O Preço da Vitória")

    layout.imprimir_lento(
        "O General cai de joelhos, o magma esfriando e petrificando em seu peito onde você cravou a Kagekiri.\n"
        "Ofegante, você gira o punho para finalizar o serviço e extrair a espada...\n\n"
        "...Mas a arma reage ao calor. A Kagekiri, forjada no gelo eterno do Monte Shiro, "
        "não suporta o estresse térmico absoluto ao mergulhar profundamente no coração de pura lava mágica."
    )
    
    layout.imprimir_lento(
        "Com um estalo agudo que reverbera em toda a montanha, [bold cyan]A KAGEKIRI SE PARTE.[/bold cyan]\n"
        "A lâmina lendária explode em uma miríade de estilhaços azuis. O General tomba, morto e transformado em cinzas, "
        "mas o choque o empurra para trás. Você olha para sua mão ensanguentada."
    )
    
    layout.console.print("\n[bold red]SISTEMA: A KAGEKIRI FOI QUEBRADA![/bold red]")
    layout.console.print("[dim]Você não possui mais uma arma viável. Seu Kenjutsu será inútil para danos severos a partir de agora.[/dim]")
    
    jogador["espada_quebrada"] = True
    # Limpa a Kagekiri fantasma da tela (se existir) e adiciona o cabo inútil.
    jogador.setdefault("inventario", []).append("Cabo Quebrado da Kagekiri")
    
    layout.esperar_enter()
    
    layout.divisoria()
    layout.imprimir_lento(
        "Os alarmes do vulcão soam. A morte do General desestabilizou o núcleo da montanha. "
        "Gêiseres de fogo explodem ao redor. O chão racha. Você aperta o cabo inútil da espada contra o peito. "
        "Sem sua arma, lutar é suicídio."
    )
    
    # A FUGA SEM ARMAS (Usa o item ganho na rota)
    tem_bomba = "Bomba de Fumaca" in jogador.get("inventario", [])
    tem_arpeu = "Arpeu de Corrente" in jogador.get("inventario", [])
    
    layout.console.print("\n[bold]A Caverna Desmorona. Como você foge?[/bold]")
    layout.console.print("[white]1 - [Destreza Dificuldade 20][/white] 'O vento sobrevive à queda'. Tentar surfar as encostas de cinzas em desmoronamento.")
    if tem_bomba:
        layout.console.print("[yellow]2 - [Usar Item][/yellow] Detonar a Bomba de Fumaça Alquímica para cegar a montanha e cobrir sua fuga cega.")
    elif tem_arpeu:
        layout.console.print("[yellow]2 - [Usar Item][/yellow] Disparar o Arpéu de Corrente nas estalactites para cruzar o abismo em balanços velozes.")
    
    layout.limpar_buffer_teclado()
    escolha_fuga = input("\nEscolha sua rota de fuga: ").strip()
    
    if escolha_fuga == "2" and (tem_bomba or tem_arpeu):
        layout.imprimir_lento("\n[green]O item recebido do ferreiro salva sua vida. Você ignora os desmoronamentos, ganhando velocidade e escapando ileso enquanto o fogo engole a retaguarda.[/green]")
    else:
        layout.imprimir_lento("\n[dim]O pânico guia suas pernas enquanto a montanha desmorona![/dim]")
        if sistemas.rolar_teste(jogador, "destreza", 20):
            layout.imprimir_lento("\n[green]Por um milagre, você desliza entre os pedregulhos chamejantes e é ejetado pela base do vulcão.[/green]")
        else:
            layout.imprimir_lento("\n[red]Uma chuva de pedras vulcânicas esmaga seus ombros! Você é lançado morro abaixo de forma brutal![/red]")
            jogador["vitalidade"] -= 12
            layout.console.print("[bold red]-12 de HP por ferimentos críticos de fuga.[/bold red]")

    if jogador["vitalidade"] <= 0: return jogador
    
    # A MEMÓRIA DA ESPERANÇA
    layout.esperar_enter()
    layout.cabecalho("AS CINZAS DO ORGULHO")
    
    layout.imprimir_lento(
        "Mutilado, com os pulmões queimando e as mãos fechadas sobre um pedaço de madeira estilhaçado, "
        "você rola até a borda de um novo território.\n"
        "O calor infernal fica para trás. Você sente lama fria no rosto e o cheiro pungente de "
        "água salobra, juncos e neblina densa. Você chegou à Província de Mizu.\n\n"
        "O mundo escurece. Uma memória antiga de Kazunari o mantém ancorado à realidade:\n"
        "[italic white]'Se a lâmina falhar, busque as águas rasas de Mizu. O Mestre Kajiya, o maior forjador "
        "da nossa era, foi exilado nas charnecas há trinta anos. Somente ele pode religar o aço de uma estrela.'[/italic white]\n\n"
        "A vingança terá que esperar. Sobreviver à selva de Mizu desarmado e encontrar o velho mestre "
        "agora é o seu único objetivo."
    )
    
    # Fogueira final (Meditação com foco no luto)
    jogador = sistemas.acampamento_fogueira(jogador, capitulo_atual=3, contexto="perda_espada")
    
    return jogador


# ==========================================
# GESTOR DO CAPÍTULO 3
# ==========================================
def jogar(jogador):
    layout.cabecalho("CAPÍTULO 3", "As Forjas da Desonra")

    layout.imprimir_lento(
        "Você cruza os antigos Portões de Ferro da Província de Tetsu. "
        "O céu é pintado com as cores do inferno. À sua frente, o coração militar do Shogunato de Cinza "
        "se ergue como um tumor vulcânico. Para destruir a base militar, você precisará infiltrar-se no núcleo."
    )

    layout.console.print("\n[bold]Escolha sua via de infiltração:[/bold]")
    layout.console.print("[white]1 - As Minas Inferiores.[/white] (Foco: Subterfúgio, sombras e a revolta dos escravos).")
    layout.console.print("[white]2 - A Forja Principal.[/white] (Foco: Ação frontal, armadilhas pesadas e magia bélica).")

    escolha_caminho = ""
    while escolha_caminho not in ["1", "2"]:
        layout.limpar_buffer_teclado()
        escolha_caminho = input("\nEscolha (1 ou 2): ").strip()

    if escolha_caminho == "1":
        jogador = cena_minas(jogador)
    elif escolha_caminho == "2":
        jogador = cena_forja(jogador)

    if jogador["vitalidade"] <= 0: return jogador
    
    # Todos convergem para o mesmo clímax (O Boss da Forja e a quebra da espada)
    jogador = cena_climax(jogador)
    
    return jogador