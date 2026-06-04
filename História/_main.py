# main.py
import sys
import layout
import capitulo_0 as prologo
import capitulo_1
import capitulo_2
import capitulo_3

import sistemas

def checar_morte(jogador):
    if jogador["vitalidade"] <= 0:
        layout.parar_musica()
        layout.cabecalho("FIM DE JOGO", "O Shogunato de Cinza venceu")
        layout.imprimir_lento(
            "[bold red]Sua visão escurece. A Kagekiri cai de suas mãos, perdendo o brilho azul-ciano. "
            "O império de Kuroi Shin'en reinará nas sombras pela eternidade.[/bold red]"
        )
        return True
    
    if jogador["honra"] <= 0:
        layout.parar_musica()
        layout.cabecalho("FIM DE JOGO", "O Caminho da Desonra")
        layout.imprimir_lento(
            "[bold red]O peso das suas ações cruéis destruiu o código do samurai. "
            "A vergonha consome sua alma. Em silêncio, sob o céu corrompido, você comete Seppuku.[/bold red]"
        )
        return True
    
    return False

def mostrar_regras():
    layout.limpar_tela()
    layout.cabecalho("O SISTEMA DE RPG", "Regras e Rolagens")
    texto = """
[bold cyan]1. Testes de Habilidade:[/bold cyan] 
Durante a história, as Múltiplas Escolhas testarão seus atributos.
O sistema rola [bold yellow]1d20 + seu Atributo[/bold yellow]. Se o resultado for maior que a Dificuldade do desafio, você tem sucesso!

[bold cyan]2. O Combate Misto:[/bold cyan] 
Você ataca rolando [bold yellow]1d20 + Kenjutsu[/bold yellow] contra a [dim]Defesa (CA)[/dim] do inimigo. O dano depende da sua arma.
Você também poderá usar o [bold]Dash de Éter[/bold] ou tentar um [bold]Parry[/bold] se a sua [green]Destreza[/green] for alta.

[bold cyan]3. Honra e Vitalidade:[/bold cyan] 
Agir como um verdadeiro herói aumenta sua [yellow]Honra[/yellow], mas geralmente exige lutas brutais que custam [red]HP[/red].
Fugir, usar furtividade ou trapacear poupa seu HP, mas drena Honra. 
Cuidado: Se a Honra chegar a zero, é Game Over (Seppuku).

[bold cyan]4. Éter:[/bold cyan] 
A energia da sua linhagem. Pode ser gasta para curar fora de combate, usar Visão Mística ou desferir ataques massivos.
    """
    layout.console.print(texto)
    
    layout.console.print("\n[dim]Pressione Enter para voltar ao menu...[/dim]")
    input()

def iniciar_jogo():
    while True:
        escolha_menu = layout.menu_inicial()
        
        if escolha_menu == "1":
            break
        elif escolha_menu == "2":
            mostrar_regras()
        elif escolha_menu == "3":
            layout.imprimir_lento("\n[bold red]Você abandonou sua espada. O Abismo consome Takenoko.[/bold red]")
            sys.exit()

    jogador = {
        "nome": "",
        "nivel": 1,
        "vitalidade": 0,
        "max_vitalidade": 0,
        "eter": 0,
        "kenjutsu": 0,
        "destreza": 0,
        "conhecimento": 0,
        "honra": 10,
        "inventario": [],
        "bonus_defesa": 0,
        "bonus_dano_arma": 0,
        "duas_espadas_longas": False,
        "espada_quebrada": False
    }

    # ================= PROLÓGO =================
    layout.tocar_musica("audio/vento_montanha.mp3") 
    
    jogador = prologo.jogar(jogador)
    if checar_morte(jogador):
        return
    
    # Exibe a Ficha de Personagem formatada em 3 blocos perfeitamente alinhada
    layout.painel_status(jogador)
    
    layout.console.print("\n[dim]Pressione Enter para iniciar o Capítulo 1...[/dim]")
    input()

    # ================= CAPÍTULO 1 =================
    layout.limpar_tela()
    
    jogador = capitulo_1.jogar(jogador)
    if checar_morte(jogador):
        return
    
    layout.limpar_tela()
    layout.painel_status(jogador)

    layout.esperar_enter("[dim]Pressione Enter para iniciar o Capítulo 2...[/dim]")

    # ================= CAPÍTULO 2 =================
    layout.limpar_tela()
    
    jogador = capitulo_2.jogar(jogador)
    if checar_morte(jogador):
        return
    
    layout.limpar_tela()
    layout.painel_status(jogador)

    layout.esperar_enter("[dim]Pressione Enter para iniciar o Capítulo 3...[/dim]")

        # ================= CAPÍTULO 3 =================
    layout.limpar_tela()
    
    jogador = capitulo_3.jogar(jogador)
    if checar_morte(jogador):
        return
    
    layout.limpar_tela()
    layout.painel_status(jogador)

    layout.esperar_enter("[dim]Pressione Enter para iniciar o Capítulo 4...[/dim]")

if __name__ == "__main__":
    iniciar_jogo()