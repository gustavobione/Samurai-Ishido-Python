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
    try:
        pygame.mixer.music.load(caminho_arquivo)
        pygame.mixer.music.play(-1)
    except pygame.error:
        # Falha ao carregar/rodar áudio (driver ausente ou arquivo inválido)
        pass

def parar_musica():
    pygame.mixer.music.stop()

def tocar_sfx(caminho_arquivo):
    try:
        som = pygame.mixer.Sound(caminho_arquivo)
        som.play()
    except pygame.error as e:
        # Propaga erro específico do pygame para o chamador tratar
        raise pygame.error(f"Erro ao tocar efeito sonoro '{caminho_arquivo}': {e}") from e

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
        
        if not pular_animacao_ref[0]:
            if checar_skip():
                pular_animacao_ref[0] = True
            elif not pular_animacao_ref[0]:
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
# PAINEL DE STATUS (GRID FLUIDO - SEM EMOJIS)
# ==========================================
def painel_status(jogador):
    """Ficha do Personagem adaptada para Width Full, usando cores em vez de Emojis"""
    
    max_hp = jogador.get("max_vitalidade", jogador.get("vitalidade", 0))
    hp_atual = jogador['vitalidade']
    eter_atual = jogador.get('eter', 0)
    nivel = jogador.get('nivel', 1)
    
    bonus_defesa = jogador.get("bonus_defesa", 0)
    mod_destreza = jogador.get("destreza", 10) // 4
    defesa_total = 10 + mod_destreza + bonus_defesa
    
    arma = "Katana Kagekiri"
    if jogador.get("duas_espadas_longas"): arma = "Sol Negro & Lua Prateada"
    elif jogador.get("espada_quebrada"): arma = "Cabo Quebrado"

    inventario = jogador.get("inventario", [])
    hp_cor = "red" if hp_atual < (max_hp/3) else "green"
    
    tabela = Table(expand=True, show_header=True, box=box.SIMPLE_HEAD, padding=(0, 2))
    
    tabela.add_column("Vitais", justify="left", style="bold", no_wrap=True)
    tabela.add_column("Atributos", justify="left", style="bold", no_wrap=True)
    tabela.add_column("Inventário", justify="left", style="white", ratio=1, no_wrap=True)
    tabela.add_column("", justify="left", style="white", ratio=1, no_wrap=True)
    tabela.add_column("", justify="left", style="white", ratio=1, no_wrap=True)

    def obter_item(idx):
        if idx == 0 and len(inventario) == 0:
            return "[dim]Vazio[/dim]"
        elif idx < len(inventario):
            return f"- {inventario[idx]}"
        return ""

    # Linha 1 
    tabela.add_row(
        f"[{hp_cor}]HP: {hp_atual}/{max_hp}[/{hp_cor}]", 
        f"[white]Kenjutsu: {jogador['kenjutsu']}[/white]", 
        obter_item(0), obter_item(1), obter_item(2)
    )
    
    # Linha 2 
    tabela.add_row(
        f"[cyan]Éter: {eter_atual}/50[/cyan]", 
        f"[green]Destreza: {jogador['destreza']}[/green]", 
        obter_item(3), obter_item(4), obter_item(5)
    )
    
    # Linha 3 
    tabela.add_row(
        f"[yellow]Honra: {jogador['honra']}[/yellow]", 
        f"[magenta]Conhecimento: {jogador['conhecimento']}[/magenta]",
        obter_item(6), obter_item(7), obter_item(8)
    )

    # Linha 4 
    tabela.add_row(
        f"[white]Arma:[/white] [cyan]{arma}[/cyan]",
        f"[blue]Defesa (CA): {defesa_total}[/blue]",
        obter_item(9), obter_item(10), obter_item(11)
    )
    
    # Linha 5 
    tabela.add_row(
        f"[yellow]Nível: {nivel}[/yellow]",
        "", 
        obter_item(12), obter_item(13), obter_item(14)
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
        escolha = input("\nEscolha sua ação: ").strip()
        
    return escolha