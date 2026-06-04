# boss.py
import layout
import sistemas
import random
import time

def cena_fase_1(jogador):
    layout.cabecalho("FASE 1: O FEITICEIRO DOS MIL ROSTOS", "A Sanidade Despedaça")
    
    layout.imprimir_lento(
        "Kuroi Shin'en não saca uma lâmina. Ele apenas levanta dois dedos. O corpo dele se desfaz "
        "em fumaça negra arcana. Em um piscar de olhos, o Salão do Trono se enche com **DEZ** cópias "
        "perfeitas do feiticeiro flutuando no ar. "
        "Todas elas começam a canalizar esferas de chamas de éter negro, prontas para incinerar a sua existência."
    )
    
    layout.console.print("\n[bold]Desafio Final 1/3: As Ilusões Mortais[/bold]")
    layout.console.print(f"[cyan]Éter Atual: {jogador.get('eter',0)}/{jogador.get('max_eter',50)}[/cyan]")
    layout.console.print("[magenta]1 - [Analisar (Magia)][/magenta] Gastar 10 de Éter para focar seus olhos através da mentira e achar o verdadeiro.")
    layout.console.print("[white]2 - [Conhecimento Dificuldade 23][/white] Fechar os olhos e tentar ouvir o único coração que bate.")
    layout.console.print("[white]3 - [Destreza Dificuldade 25][/white] Usar velocidade absoluta do Nitoryu para cortar as dez cópias antes que a magia dispare.")
    
    layout.limpar_buffer_teclado()
    acao = input("\nSua ação (1, 2 ou 3): ").strip()
    
    if acao == "1" and jogador.get("eter", 0) >= 10:
        jogador["eter"] -= 10
        jogador.setdefault("atributos_usados", set()).add("eter")
        layout.imprimir_lento("\n[magenta]Com a Visão Mística, as cópias ficam cinzas, enquanto o verdadeiro Kuroi brilha em vermelho vivo. Você avança certeiro e corta seu ombro![/magenta]")
    else:
        if acao == "1": layout.imprimir_lento("\n[red]Éter insuficiente. A dor obscurece sua visão mágica.[/red]")
        
        if acao == "3":
            if sistemas.rolar_teste(jogador, "destreza", 25):
                layout.imprimir_lento("\n[green]Você vira um furacão de lâminas! As cópias estouram como vidro. A última é o Kuroi verdadeiro, que grita ao receber um corte da Lua Prateada no peito![/green]")
            else:
                layout.imprimir_lento("\n[red]Você é rápido, mas a magia é instantânea! As dez esferas de chamas arcanas bombardeiam você no ar![/red]")
                jogador["vitalidade"] -= 15
        else:
            if sistemas.rolar_teste(jogador, "conhecimento", 23):
                layout.imprimir_lento("\n[green]Você bloqueia os sentidos falsos. No silêncio total, nove cópias são ocas. A da esquerda respira. Você abre os olhos e corta o ombro dele![/green]")
            else:
                layout.imprimir_lento("\n[red]Os sons e as risadas das ilusões esmagam sua concentração. Kuroi dispara o fogo infernal nas suas costas![/red]")
                jogador["vitalidade"] -= 15

    layout.esperar_enter()
    return jogador


def cena_fase_2(jogador):
    if jogador["vitalidade"] <= 0: return jogador
    
    layout.cabecalho("FASE 2: A REJEIÇÃO DA LINHAGEM", "O Poder do Xogum Roubado")
    
    layout.imprimir_lento(
        "Kuroi Shin'en rasteja para trás, o sangue negro manchando o mármore sagrado.\n"
        "[bold yellow]'O MUNDO SUPERA O SANGUE!'[/bold yellow], ele berra aspergindo sua raiva."
    )
    layout.imprimir_lento(
        "Ele ergue as duas mãos para o teto. As dez partes do *Disco do Abismo* rodam violentamente, "
        "descendo para cobri-lo. Uma cúpula esférica de energia cósmica, impenetrável e imutável, se forma.\n"
        "'Este é o poder do Imperador! E ele me obedece agora!', grita Kuroi, protegido pelo próprio artefato "
        "roubado da sua família."
    )
    
    layout.console.print("\n[bold]Desafio Final 2/3: O Falso Deus[/bold]")
    layout.console.print(f"[yellow]Honra Atual: {jogador.get('honra', 10)}[/yellow]")
    layout.console.print("[white]1 - [Honra Nv 20+ Exigida][/white] O Caminho do Rei. Abaixar as armas, caminhar até o escudo e exigir que o Disco reconheça o Herdeiro Legítimo por sua pureza.")
    if "Corte do Vazio" in jogador.get("habilidades", []):
        layout.console.print(f"[magenta]2 - [Corte do Vazio][/magenta] Gastar 15 Éter (Éter Atual: {jogador.get('eter',0)}) para ignorar o bloqueio físico com o Sol Negro.")
    layout.console.print("[white]3 - [Kenjutsu Dificuldade 27][/white] O aço das estrelas forjado não cede. Colidir o Nitoryu na barreira com toda a sua energia vital.")
    
    layout.limpar_buffer_teclado()
    acao = input("\nComo destruir o que não pode ser destruído? ").strip()
    
    if acao == "1":
        if jogador.get("honra", 10) >= 20:
            layout.imprimir_lento(
                "\n[green]Você embainha as espadas. Você caminha em silêncio. A essência cristalina dos Shiro brilha "
                "ao redor do seu corpo. Ao encostar a mão no escudo corrompido, a Honra pura anula as trevas. "
                "O Disco do Abismo o reconhece, pisca em azul e... desliga a barreira de Kuroi! O mago entra em choque brutal.[/green]"
            )
        else:
            layout.imprimir_lento(
                "\n[red]Você tenta apelar ao sagrado, mas o Disco recua. Suas mãos estão manchadas demais com atalhos, "
                "emboscadas e desonra. A barreira sente suas falhas e o repele violentamente com um choque divino![/red]"
            )
            jogador["vitalidade"] -= 18
            
    elif acao == "2" and "Corte do Vazio" in jogador.get("habilidades", []) and jogador.get("eter", 0) >= 15:
        jogador["eter"] -= 15
        jogador.setdefault("atributos_usados", set()).add("eter")
        layout.imprimir_lento(
            "\n[magenta]Você não tenta quebrar a barreira, você rasga a tela do universo. A lâmina ônix do Sol Negro "
            "atravessa a magia divina como papel, rasgando o peito de Kuroi de dentro para fora![/magenta]"
        )
    else:
        if acao == "2": layout.imprimir_lento("\n[red]Requisitos de Éter falharam.[/red]")
        
        layout.imprimir_lento("\n[dim]Você ergue o Sol e a Lua acima da cabeça, canalizando a força de um furacão![/dim]")
        if sistemas.rolar_teste(jogador, "kenjutsu", 27):
            layout.imprimir_lento(
                "\n[green]SUCESSO ABSOLUTO! O choque astronômico de duas armas estelares contra um artefato da mesma origem cria uma explosão cósmica. "
                "A barreira divina racha e estilhaça em milhões de fragmentos![/green]"
            )
        else:
            layout.imprimir_lento(
                "\n[red]FALHA! A barreira é imutável. A força do impacto rebate para o seu próprio corpo, deslocando seus ombros e lançando você pelo ar ensanguentado![/red]"
            )
            jogador["vitalidade"] -= 20

    layout.esperar_enter()
    return jogador


def cena_fase_3(jogador):
    if jogador["vitalidade"] <= 0: return jogador
    
    layout.cabecalho("FASE FINAL: O AVATAR DO CAOS", "O Fim dos Tempos")
    
    layout.imprimir_lento(
        "Sem escudo, sangrando e derrotado nas artes místicas, Kuroi Shin'en ri.\n"
        "Uma risada que racha as pilastras do teto. Não é mais uma voz humana.\n\n"
        "[bold red]'SE EU NÃO POSSO GOVERNAR O QUE HÁ SOBRE O CÉU... ELE NÃO EXISTIRÁ!'[/bold red]\n\n"
        "O mago estende as mãos trêmulas e funde a si próprio o núcleo do Disco do Abismo. "
        "A carne de Kuroi evapora, sendo substituída por pura matéria negra cósmica. Ele cresce de forma abissal. "
        "Dez... quinze metros de altura."
    )
    layout.imprimir_lento(
        "O teto do castelo é vaporizado. O céu tempestuoso da Capital serve de palco.\n"
        "O Avatar do Caos surge: Uma massa rotativa de trevas com braços de fogo, "
        "orbes que gravitam em sua cintura e centenas de olhos que choram sangue negro. "
        "O mundo treme."
    )
    layout.esperar_enter("[dim]A lenda de Ishido termina aqui...[/dim]")
    
    # O CHEFE FINAL NO SISTEMA DE COMBATE OFICIAL
    # Atribuí uma resistência à "Físico" para que habilidades como Lâmina de Gelo e Corte do Vazio brilhem aqui
    resultado = sistemas.iniciar_combate(
        jogador, 
        nome_inimigo="AVATAR DO CAOS (DEUS DO ABISMO)", 
        hp_inimigo=200, 
        defesa_inimigo=22, 
        min_dano=12, 
        max_dano=25, 
        xp_recompensa=0, # Fim do jogo
        fraqueza="Nenhuma", 
        resistencia="Físico"
    )
    
    return jogador


def epilogo(jogador):
    layout.cabecalho("EPÍLOGO", "O Peso de Uma Era")
    
    layout.imprimir_lento(
        "O Avatar se retorce em uma explosão de energia silenciosa. Um clarão engole os céus, "
        "e as nuvens corrompidas de Takenoko se dissolvem pela primeira vez em décadas. "
        "A poeira cósmica cai como neve sobre a torre arruinada. Kuroi Shin'en não existe mais."
    )
    layout.imprimir_lento(
        "Você desaba de joelhos, coberto de fuligem e sangue.\n"
        "Flutuando a meio metro do chão de mármore partido, pulsando com energia infinita "
        "e sem mestre, está o [bold cyan]Disco do Abismo[/bold cyan]. O artefato supremo. "
        "Aquele que corrompeu o Shogunato."
    )
    layout.imprimir_lento(
        "Ele canta para você. O disco oferece a cura do mundo, a imortalidade, o poder absoluto. "
        "Você poderia assumir o Trono de Obsidiana. Ninguém jamais ousaria contestar o Xogum das Sombras."
    )
    
    layout.console.print("\n[bold]As Lâminas na sua mão tremem. Qual será a sua última ordem?[/bold]")
    layout.console.print(f"[yellow]Honra Atual: {jogador.get('honra', 10)}[/yellow]")
    layout.console.print("[white]1 - [A Purificação][/white] O poder absoluto corrompe absolutamente. Desferir um golpe letal para estilhaçar o Disco para sempre.")
    layout.console.print("[white]2 - [O Império de Cinzas][/white] Reivindicar o Disco. Absorvê-lo para restaurar Takenoko sob o seu punho de ferro.")
    
    layout.limpar_buffer_teclado()
    escolha_final = input("\nSua decisão ecoará pela eternidade (1 ou 2): ").strip()
    
    layout.divisoria()
    
    if escolha_final == "1":
        layout.imprimir_lento(
            "Você ergue o Sol Negro e a Lua Prateada cruzados acima da cabeça. "
            "A aura de Kazunari e as memórias das vítimas da neve, da floresta e da forja guiam seus braços.\n"
            "Com um grito primal, você corta a própria fundação da magia!\n\n"
            "O Disco do Abismo racha. Uma explosão branca pacífica varre a capital. Toda a corrupção é varrida da existência.\n"
            "A Torre desmorona para sempre. Você salta a salvo pelos telhados enquanto a luz do amanhecer, pura e natural, banha o seu rosto."
        )
        layout.imprimir_lento(
            "\n[bold green]Anos depois, os arrozais florescem em Mizu. Não há mais lordes demônios, "
            "tampouco Xoguns intocáveis. Apenas lendas folclóricas de um espadachim descalço "
            "com duas lâminas estelares vagando pelo Japão restaurado, vivendo a vida de um homem livre.[/bold green]"
        )
        
    else:
        layout.imprimir_lento(
            "Você abaixa as lâminas e caminha até o Disco. A sua alma cansada de dor e perda aceita o sacrifício.\n"
            "Ao encostar no artefato, as chamas cósmicas sobem pelo seu braço, mesclando-se à sua carne.\n"
            "Seus olhos assumem uma cor eterna, sem fundo. As vozes de bilhões de mortos ajoelham-se em sua mente."
        )
        layout.imprimir_lento(
            "\n[bold red]Você se senta no trono despedaçado de seu pai.\n"
            "Kuroi foi fraco. O Imperador foi tolo.\n"
            f"As portas do mundo se abrem para os horrores reanimados sob o seu comando. Lorde {jogador['nome']}, "
            "o Arauto das Duas Lâminas, levanta a mão e mergulha o leste do mundo no seu Império Pessoal de Morte e Fogo.\n"
            "A tirania encontrou o seu Deus da Guerra absoluto.[/bold red]"
        )

    time.sleep(3)
    layout.cabecalho("FIM DE JOGO", "Obrigado por jogar Samurai Ishido")
    
    layout.console.print(f"[bold cyan]Seu Samurai Finalizou com:[/bold cyan]")
    layout.console.print(f"Honra: {jogador.get('honra', 0)}")
    layout.console.print(f"Kenjutsu: {jogador.get('kenjutsu', 0)} | Destreza: {jogador.get('destreza', 0)} | Conhecimento: {jogador.get('conhecimento', 0)}")
    layout.console.print(f"Inventário Retido: {', '.join(jogador.get('inventario', ['Vazio']))}")
    
    layout.esperar_enter("\nPressione Enter para fechar as cortinas do palco...")


# ==========================================
# GESTOR DO BOSS
# ==========================================
def jogar(jogador):
    jogador = cena_fase_1(jogador)
    if jogador["vitalidade"] <= 0: 
        layout.imprimir_lento("\n[dim]As ilusões o enlouqueceram. Seu corpo virou cinzas na Câmara do Trono.[/dim]")
        return jogador
        
    jogador = cena_fase_2(jogador)
    if jogador["vitalidade"] <= 0: 
        layout.imprimir_lento("\n[dim]A barreira cósmica esmagou sua existência antes de você sequer piscar.[/dim]")
        return jogador
        
    jogador = cena_fase_3(jogador)
    if jogador["vitalidade"] <= 0: 
        layout.imprimir_lento("\n[dim]O Avatar das Trevas devorou as estrelas e engoliu o mundo em escuridão infinita.[/dim]")
        return jogador
        
    epilogo(jogador)
    
    return jogador