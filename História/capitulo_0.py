# capitulo_0.py
import time
import random
import sys
import layout

def animacao_rolagem():
    """Cria a animação de dados girando (. .. ...)"""
    frames = [".", "..", "...", ".  ", ".. ", "..."]
    for _ in range(2):
        for frame in frames:
            sys.stdout.write(f"\rRolando os dados {frame}")
            sys.stdout.flush()
            time.sleep(0.15)
    print() # Limpa a linha

def rolar_dados_rpg(quantidade, faces):
    animacao_rolagem()
    resultados = [random.randint(1, faces) for _ in range(quantidade)]
    total = sum(resultados)
    detalhes = " + ".join(map(str, resultados))
    return total, detalhes

def rolar_atributos_iniciais():
    layout.limpar_tela()
    layout.cabecalho("A FORJA DO DESTINO", "Sua linhagem desperta")
    
    layout.imprimir_lento("[cyan]Os Kami tecem os fios do seu destino...[/cyan]")
    time.sleep(0.5)
    
    atributos = {}
    
    layout.console.print("\n[bold red]VITALIDADE (HP)[/bold red] - Sua resistência física e fôlego.")
    total_dados, detalhes = rolar_dados_rpg(3, 6)
    atributos["max_vitalidade"] = 10 + total_dados
    atributos["vitalidade"] = atributos["max_vitalidade"]
    layout.console.print(f"[dim]Dados (3d6): [ {detalhes} ] = {total_dados}[/dim]")
    layout.console.print(f"Total (Base 10 + {total_dados}): [bold red]{atributos['vitalidade']}[/bold red]")
    time.sleep(0.5)

    layout.console.print("\n[bold white]KENJUTSU[/bold white] - Força bruta, maestria com a katana e poder de corte.")
    total_dados, detalhes = rolar_dados_rpg(2, 6)
    atributos["kenjutsu"] = 10 + total_dados
    layout.console.print(f"[dim]Dados (2d6): [ {detalhes} ] = {total_dados}[/dim]")
    layout.console.print(f"Total (Base 10 + {total_dados}): [bold white]{atributos['kenjutsu']}[/bold white]")
    time.sleep(0.5)

    layout.console.print("\n[bold green]DESTREZA[/bold green] - Agilidade, esquiva, Parry e furtividade nas sombras.")
    total_dados, detalhes = rolar_dados_rpg(2, 6)
    atributos["destreza"] = 10 + total_dados
    layout.console.print(f"[dim]Dados (2d6): [ {detalhes} ] = {total_dados}[/dim]")
    layout.console.print(f"Total (Base 10 + {total_dados}): [bold green]{atributos['destreza']}[/bold green]")
    time.sleep(0.5)

    layout.console.print("\n[bold magenta]CONHECIMENTO[/bold magenta] - Sabedoria tática, intuição folclórica e leitura de mundo.")
    total_dados, detalhes = rolar_dados_rpg(2, 6)
    atributos["conhecimento"] = 10 + total_dados
    layout.console.print(f"[dim]Dados (2d6): [ {detalhes} ] = {total_dados}[/dim]")
    layout.console.print(f"Total (Base 10 + {total_dados}): [bold magenta]{atributos['conhecimento']}[/bold magenta]")
    time.sleep(0.5)

    layout.console.print("\n[bold cyan]ÉTER[/bold cyan] - Energia anímica da linhagem Shiro. Usada para magias e Dash.")
    total_dados, detalhes = rolar_dados_rpg(3, 6)
    atributos["eter"] = 20 + total_dados
    layout.console.print(f"[dim]Dados (3d6): [ {detalhes} ] = {total_dados}[/dim]")
    layout.console.print(f"Total (Base 20 + {total_dados}): [bold cyan]{atributos['eter']}[/bold cyan]")
    time.sleep(1)
    
    layout.console.print("\n[bold yellow]Sua Ficha de Samurai foi gerada com sucesso![/bold yellow]")
    
    layout.esperar_enter("\n[dim]Pressione Enter para iniciar a história...[/dim]")
    return atributos

def jogar(jogador):
    layout.cabecalho("PRÓLOGO", "O Silêncio da Neve")
    
    historia_parte_1 = (
        "O frio no cume da Colina Lótus corta como vidro. A tempestade mágica de [bold cyan]Éter Puro[/bold cyan] "
        "que isolou este pico do resto de Takenoko por duas décadas finalmente cessou.\n"
        "O silêncio que se seguiu foi ainda mais pesado.\n\n"
        "Seu mestre, [bold yellow]Kazunari[/bold yellow], está morto.\n\n"
        "O ex-capitão da Guarda Obsidiana passou os últimos vinte anos da vida dele te transformando "
        "em uma arma. Você não aprendeu a brincar. Aprendeu a cair, a suportar o frio extremo e a empunhar "
        "uma lâmina com a maestria cega de quem não tem mais nada a perder."
    )
    layout.imprimir_lento(historia_parte_1)
    
    layout.esperar_enter("[dim]Pressione Enter para lembrar do passado...[/dim]")

    historia_parte_2 = (
        "Ele costumava contar sobre a [bold red]Noite das Sombras[/bold red], quando o Alto Sacerdote [bold magenta]Kuroi Shin'en[/bold magenta] "
        "abraçou o núcleo do Astrolábio Celestial, rasgando o véu dimensional. O Abismo inundou o mundo. "
        "Seu pai, o Xogum Nobutatsu, foi assassinado.\n\n"
        "Kazunari invadiu o palácio desmoronando e resgatou você – ainda um bebê – perdendo o braço "
        "esquerdo para uma quimera no processo. Ele nunca foi um pai carinhoso. Seu afeto "
        "vinha disfarçado de instrução militar brutal."
    )
    layout.imprimir_lento(historia_parte_2)
    
    layout.esperar_enter("[dim]Pressione Enter para retornar ao presente...[/dim]")

    historia_parte_3 = (
        "Você termina de erguer o túmulo de pedras brutas. O vento sopra da base da montanha, trazendo "
        "um cheiro de cinzas e corrupção. O [bold]Shogunato de Cinza[/bold] estabelecido por Kuroi "
        "governa o mundo lá embaixo administrando o próprio caos.\n\n"
        "Aos pés do túmulo de Kazunari repousa a velha espada de meteorito que ele protegeu com a vida.\n"
        "A [bold cyan]Kagekiri[/bold cyan] (Corta-Sombras)."
    )
    layout.imprimir_lento(historia_parte_3)
    
    nome_input = input("\nComo você se chama, último herdeiro do clã Shiro? (Aperte Enter para 'Ishido'): ").strip()
    jogador["nome"] = "Ishido" if nome_input == "" else nome_input

    layout.imprimir_lento(f"\nVocê envolve os dedos no cabo frio da espada, [bold]{jogador['nome']}[/bold].")
    
    layout.tocar_sfx("audio/saque_espada.mp3") 
    
    historia_parte_4 = (
        "\nNo instante em que sua pele toca a arma, o metal negro se ilumina. Uma linha de [bold cyan]Éter Puro[/bold cyan] "
        "pulsa pela lâmina, reconhecendo o sangue vivo da sua linhagem.\n"
        "Através da espada, você sente uma presença familiar: um fragmento da alma exausta de Kazunari "
        "fundiu-se à lâmina no momento da morte dele."
    )
    layout.imprimir_lento(historia_parte_4)

    layout.esperar_enter("\n[dim]Pressione Enter para despertar seu poder interior...[/dim]")

    novos_atributos = rolar_atributos_iniciais()
    jogador.update(novos_atributos)

    layout.limpar_tela()
    layout.imprimir_lento("Com a [bold cyan]Kagekiri[/bold cyan] embainhada, você vira as costas para o túmulo do seu mestre.")
    layout.imprimir_lento("A descida da montanha vai começar. E o império corrompido de Takenoko sentirá o seu aço.")
    
    return jogador