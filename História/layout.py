# layout.py
import time
import os
import sys
import re
import pygame
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

# Biblioteca nativa do Windows para escutar o teclado em tempo real
if os.name == 'nt':
    import msvcrt

# Inicializa o console do Rich
console = Console()
LARGURA_TELA = 80

# ==========================================
# SISTEMA DE ÁUDIO (PYGAME)
# ==========================================
pygame.mixer.init()

def tocar_musica(caminho_arquivo):
    """Toca uma música de fundo em loop apenas se o arquivo existir"""
    if os.path.exists(caminho_arquivo):
        try:
            pygame.mixer.music.load(caminho_arquivo)
            pygame.mixer.music.play(-1)
        except Exception:
            pass 

def parar_musica():
    """Para a música atual"""
    try:
        pygame.mixer.music.stop()
    except Exception:
        pass

def tocar_sfx(caminho_arquivo):
    """Toca um efeito sonoro rápido apenas se o arquivo existir"""
    if os.path.exists(caminho_arquivo):
        try:
            som = pygame.mixer.Sound(caminho_arquivo)
            som.play()
        except Exception:
            pass

# ==========================================
# INTERFACE E TECLADO
# ==========================================
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def limpar_buffer_teclado():
    """Joga fora teclas extras pressionadas para não bugar o próximo input"""
    if os.name == 'nt':
        while msvcrt.kbhit():
            msvcrt.getch()

def checar_skip():
    """Verifica se alguma tecla foi pressionada para pular a animação"""
    if os.name == 'nt' and msvcrt.kbhit():
        msvcrt.getch() # Consome a tecla
        return True
    return False

def esperar_enter(mensagem="[dim]Pressione Enter para continuar...[/dim]"):
    """Função segura que limpa o teclado antes de pedir um Enter"""
    limpar_buffer_teclado()
    console.print(f"\n{mensagem}")
    input() # Aguarda o enter real
    limpar_buffer_teclado()

def cabecalho(titulo, subtitulo=""):
    limpar_tela()
    texto = f"[bold white]{titulo}[/bold white]"
    if subtitulo:
        texto += f"\n[italic cyan]{subtitulo}[/italic cyan]"
        
    painel = Panel(texto, border_style="cyan", padding=(1, 5), expand=True, title_align="center")
    console.print(painel, justify="center")
    print()

def _processar_tags_e_exibir(tokens, atraso, pular_animacao_ref):
    """Processa tokens (texto + tags) e exibe caractere por caractere"""
    pilha_tags = []
    
    for token in tokens:
        if not token: 
            continue
        
        if token.startswith('[') and token.endswith(']'):
            if token.startswith('[/'):
                if pilha_tags: 
                    pilha_tags.pop()
            else:
                pilha_tags.append(token)
        else:
            _exibir_caracteres(token, pilha_tags, atraso, pular_animacao_ref)

def _exibir_caracteres(token, pilha_tags, atraso, pular_animacao_ref):
    """Exibe cada caractere do token com efeito de digitação"""
    prefixo = "".join(pilha_tags)
    sufixo = "[/]" * len(pilha_tags)
    
    for char in token:
        console.print(f"{prefixo}{char}{sufixo}", end="")
        
        # Se a animação não foi pulada ainda, checamos o teclado e esperamos
        if not pular_animacao_ref[0]:
            if checar_skip():
                pular_animacao_ref[0] = True
                limpar_buffer_teclado() # Limpa o restante do buffer imediatamente
            else:
                time.sleep(atraso)

def imprimir_lento(texto, atraso=0.015):
    """Efeito máquina de escrever que pode ser pulado ao apertar qualquer tecla"""
    limpar_buffer_teclado()
    pular_animacao = [False]  # Uso de lista para passagem por referência
    
    linhas = texto.split('\n')
    for linha in linhas:
        if not linha:
            print()
            continue
        
        tokens = re.split(r'(\[[^\]]*\])', linha)
        _processar_tags_e_exibir(tokens, atraso, pular_animacao)
        print()
    
    print()
    limpar_buffer_teclado()  # Evita que a tecla que pulou o texto pule a próxima tela

def divisoria():
    console.print(f"[dim cyan]{'━' * LARGURA_TELA}[/dim cyan]")

# ==========================================
# PAINEL DE STATUS (GRID EXPANDIDO - RPG)
# ==========================================
def painel_status(jogador):
    """Ficha do Personagem Completa: Vitais, Atributos, Habilidades e Inventário"""
    
    # Cálculos Essenciais
    max_hp = jogador.get("max_vitalidade", jogador.get("vitalidade", 0))
    hp_atual = jogador.get('vitalidade', 0)
    
    max_eter = jogador.get("max_eter", 50)
    eter_atual = jogador.get('eter', 0)
    
    nivel = jogador.get('nivel', 1)
    xp_atual = jogador.get('xp', 0)
    # Lógica Exponencial de XP: 100, 200, 400, 800...
    xp_necessario = 100 * (2 ** (nivel - 1)) 
    
    bonus_defesa = jogador.get("bonus_defesa", 0)
    mod_destreza = jogador.get("destreza", 10) // 4
    defesa_total = 10 + mod_destreza + bonus_defesa
    
    arma = "Katana Kagekiri"
    if jogador.get("duas_espadas_longas"): arma = "Sol Negro & Lua Prateada"
    elif jogador.get("espada_quebrada"): arma = "Cabo Quebrado"

    inventario = jogador.get("inventario", [])
    habilidades = jogador.get("habilidades", [])
    hp_cor = "red" if hp_atual < (max_hp/3) else "green"
    
    # Criando o Grid Full Width
    tabela = Table(expand=True, show_header=True, box=box.SIMPLE_HEAD, padding=(0, 2))
    
    tabela.add_column("Vitais", justify="left", style="bold", no_wrap=True)
    tabela.add_column("Atributos", justify="left", style="bold", no_wrap=True)
    tabela.add_column("Habilidades", justify="left", style="cyan", no_wrap=True)
    tabela.add_column("Inventário", justify="left", style="white", ratio=1, no_wrap=True)
    tabela.add_column("", justify="left", style="white", ratio=1, no_wrap=True)

    def obter_item(lista, idx, texto_vazio):
        if idx == 0 and len(lista) == 0:
            return f"[dim]{texto_vazio}[/dim]"
        elif idx < len(lista):
            return f"- {lista[idx]}"
        return ""

    # Linha 1 
    tabela.add_row(
        f"[{hp_cor}]HP: {hp_atual}/{max_hp}[/{hp_cor}]", 
        f"[white]Kenjutsu: {jogador['kenjutsu']}[/white]",
        obter_item(habilidades, 0, "Nenhuma"),
        obter_item(inventario, 0, "Vazio"), 
        obter_item(inventario, 1, "")
    )
    
    # Linha 2 
    tabela.add_row(
        f"[cyan]Éter: {eter_atual}/{max_eter}[/cyan]", 
        f"[green]Destreza: {jogador['destreza']}[/green]",
        obter_item(habilidades, 1, ""),
        obter_item(inventario, 2, ""), 
        obter_item(inventario, 3, "")
    )
    
    # Linha 3 
    tabela.add_row(
        f"[yellow]Honra: {jogador['honra']}[/yellow]", 
        f"[magenta]Conhecimento: {jogador['conhecimento']}[/magenta]",
        obter_item(habilidades, 2, ""),
        obter_item(inventario, 4, ""), 
        obter_item(inventario, 5, "")
    )

    # Linha 4 
    tabela.add_row(
        f"[white]Arma:[/white] [cyan]{arma}[/cyan]",
        f"[blue]Defesa (CA): {defesa_total}[/blue]",
        obter_item(habilidades, 3, ""),
        obter_item(inventario, 6, ""), 
        obter_item(inventario, 7, "")
    )
    
    # Linha 5 (Exibe o XP progressivo)
    tabela.add_row(
        f"[yellow]Nível: {nivel}[/yellow]",
        f"[dim]XP: {xp_atual}/{xp_necessario}[/dim]", 
        obter_item(habilidades, 4, ""),
        obter_item(inventario, 8, ""), 
        obter_item(inventario, 9, "")
    )

    console.print(Panel(
        tabela, 
        title=f"[bold white]FICHA DO SAMURAI: {jogador['nome'].upper()}[/bold white]", 
        border_style="blue", 
        expand=True
    ))
    print()

# ==========================================
# MENU INICIAL DO JOGO
# ==========================================
def menu_inicial():
    limpar_tela()
    
    arte_titulo = """[bold cyan]
 ██████╗  █████╗ ███╗   ███╗██╗   ██╗██████╗  █████╗ ██╗
██╔════╝ ██╔══██╗████╗ ████║██║   ██║██╔══██╗██╔══██╗██║
███████╗ ███████║██╔████╔██║██║   ██║██████╔╝███████║██║
╚════██║ ██╔══██║██║╚██╔╝██║██║   ██║██╔══██╗██╔══██║██║
███████║ ██║  ██║██║ ╚═╝ ██║╚██████╔╝██║  ██║██║  ██║██║
╚══════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
         ██╗███████╗██╗  ██╗██╗██████╗  ██████╗         
         ██║██╔════╝██║  ██║██║██╔══██╗██╔═══██╗        
         ██║███████╗███████║██║██║  ██║██║   ██║        
         ██║╚════██║██╔══██║██║██║  ██║██║   ██║        
         ██║███████║██║  ██║██║██████╔╝╚██████╔╝        
         ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝         
    [/bold cyan]"""
    
    console.print(arte_titulo, justify="center")
    console.print("[dim white]Uma Jornada Narrativa de Aço, Sangue e Escolhas[/dim white]\n", justify="center")
    
    opcoes_menu = Panel(
        "[1] Iniciar Nova Jornada\n"
        "[2] Rolagens e Regras do Jogo\n"
        "[3] Sair pelo Caminho da Desonra",
        title="[bold yellow]MENU PRINCIPAL[/bold yellow]",
        border_style="yellow",
        expand=False
    )
    console.print(opcoes_menu, justify="center")
    
    escolha = ""
    while escolha not in ["1", "2", "3"]:
        limpar_buffer_teclado() # Limpa sujeiras antes de pedir input
        escolha = input("\nEscolha sua ação: ").strip()
        
    return escolha