import random
import time
import layout

# ==========================================
# PROGRESSÃO E LEVEL UP
# ==========================================
def checar_level_up(jogador):
    """Verifica se o jogador tem XP suficiente e faz a evolução. Guarda o XP excedente."""
    nivel_atual = jogador.get("nivel", 1)
    xp_atual = jogador.get("xp", 0)
    
    # Lógica Exponencial de XP: 100, 200, 400, 800...
    xp_necessario = 100 * (2 ** (nivel_atual - 1)) 

    # Usa 'while' caso o jogador ganhe muito XP de uma vez e suba mais de um nível
    subiu_de_nivel = False
    while jogador["xp"] >= xp_necessario:
        jogador["nivel"] += 1
        jogador["xp"] -= xp_necessario # O excedente continua no jogador["xp"]
        nivel_atual = jogador["nivel"]
        xp_necessario = 100 * (2 ** (nivel_atual - 1))
        subiu_de_nivel = True
        
        layout.imprimir_lento(f"\n[bold yellow]*** O SANGUE DOS SHIRO FERVE. VOCÊ ATINGIU O NÍVEL {nivel_atual}! ***[/bold yellow]")
        
        # Rolagens de aumento de status gerais (1d3 para atributos, 1d6 para pools)
        add_ken = random.randint(1, 3)
        add_des = random.randint(1, 3)
        add_con = random.randint(1, 3)
        add_hp = random.randint(3, 6)
        add_eter = random.randint(3, 6)
        
        jogador["kenjutsu"] += add_ken
        jogador["destreza"] += add_des
        jogador["conhecimento"] += add_con
        
        jogador["max_vitalidade"] += add_hp
        jogador["vitalidade"] = jogador["max_vitalidade"] # Cura total ao upar
        
        if "max_eter" not in jogador:
            jogador["max_eter"] = jogador.get("eter", 50)
            
        jogador["max_eter"] += add_eter
        jogador["eter"] = jogador["max_eter"] # Restaura Éter ao upar
        
        layout.console.print("[cyan]Seu corpo e mente se adaptaram às atrocidades deste império:[/cyan]")
        layout.console.print(f"[white]Kenjutsu +{add_ken}[/white] | [green]Destreza +{add_des}[/green] | [magenta]Conhecimento +{add_con}[/magenta]")
        layout.console.print(f"[red]HP Máximo +{add_hp}[/red] | [cyan]Éter Máximo +{add_eter}[/cyan]")
        layout.esperar_enter("[dim]Sua jornada continua mais forte...[/dim]")

    return jogador

# ==========================================
# SISTEMA DE FOGUEIRA
# ==========================================
def gerar_reflexao(jogador, capitulo_atual, contexto):
    """Gera textos dinâmicos de meditação baseados nas ações do jogador."""
    texto = "[dim]Você fecha os olhos e revisita as memórias recentes...[/dim]\n"
    if capitulo_atual == 1:
        if contexto == "vila_gelo":
            texto += "[italic cyan]O som do vento cortante nas ruínas... A frieza da armadura do Tenente Shiro... Você reflete sobre como a corrupção distorceu o legado do seu clã. Cada golpe que você deu foi um ato de misericórdia para com as almas perdidas na neve.[/italic cyan]"
        elif contexto == "caverna":
            texto += "[italic magenta]A escuridão esmagadora das Cavernas da Mandíbula ainda pesa nos seus ombros. Você se lembra do eco monstruoso batendo nas paredes de pedra, ajustando sua respiração para não ser engolido pelo medo.[/italic magenta]"
        else:
            texto += "[italic white]Os ensinamentos de Kazunari ecoam na sua mente. A lâmina é a extensão da alma.[/italic white]"
    return texto

def acampamento_fogueira(jogador, capitulo_atual=1, contexto=""):
    """Sistema dividido entre Descansar (Heal) e Meditar (Buff/Up de atributo)."""
    layout.cabecalho("O DESCANSO DO GUERREIRO", "O calor da fogueira afasta o abismo")
    
    layout.imprimir_lento(
        "Você encontra um local seguro, acende uma fogueira escondida e senta. "
        "A Kagekiri repousa no seu colo. O fogo estala, e você tem um momento de paz."
    )
    
    while True:
        layout.console.print("\n[bold]O que você fará esta noite?[/bold]")
        layout.console.print("[white]1 - [Descansar][/white] Limpar as feridas e dormir (Restaura HP e Éter).")
        layout.console.print("[cyan]2 - [Meditar][/cyan] Refletir sobre as lutas de hoje (Tenta evoluir atributos usados).")
        
        layout.limpar_buffer_teclado()
        escolha = input("\nEscolha (1 ou 2): ").strip()
        
        if escolha == "1":
            cura = random.randint(15, 25)
            max_vit = jogador.get("max_vitalidade", 15)
            jogador["vitalidade"] = min(max_vit, jogador.get("vitalidade", 0) + cura)
            jogador["eter"] = jogador.get("max_eter", 50)
            layout.imprimir_lento(f"\n[green]Você tem um sono pesado e restaurador. HP curado em {cura}. Éter totalmente restaurado.[/green]")
            break
            
        elif escolha == "2":
            layout.imprimir_lento(f"\n{gerar_reflexao(jogador, capitulo_atual, contexto)}")
            
            atributos_usados = jogador.get("atributos_usados", set())
            if atributos_usados:
                teve_aumento = False
                for attr in atributos_usados:
                    if random.randint(1, 100) <= 50: # 50% de chance na meditação
                        jogador[attr] += 1
                        layout.imprimir_lento(f"[bold green]Sua clareza mental aprimora seus instintos. {attr.capitalize()} subiu +1 permanentemente![/bold green]")
                        teve_aumento = True
                if not teve_aumento:
                    layout.imprimir_lento("[dim]Você medita profundamente, mas sente que precisa de mais desafios práticos para dominar esses movimentos.[/dim]")
            else:
                layout.imprimir_lento("[dim]Você tenta meditar, mas não vivenciou experiências suficientes hoje para tirar novas lições.[/dim]")
            
            # Limpa os atributos para o próximo ciclo
            jogador["atributos_usados"].clear()
            break
        else:
            layout.console.print("[red]Escolha inválida.[/red]")

    layout.esperar_enter("[dim]A fogueira apaga. É hora de seguir jornada...[/dim]")
    return jogador

# ==========================================
# MOTOR DE COMBATE CENTRALIZADO
# ==========================================
def aplicar_multiplicador(dano_base, elemento, fraqueza, resistencia):
    """Calcula fraquezas e resistências"""
    if elemento == fraqueza and fraqueza != "Nenhuma":
        layout.console.print(f"[bold yellow]FRAQUEZA EXPLORADA! Dano Duplo! ({elemento})[/bold yellow]")
        return int(dano_base * 2)
    elif elemento == resistencia and resistencia != "Nenhuma":
        layout.console.print(f"[dim]O inimigo resiste ao ataque... Dano Reduzido! ({elemento})[/dim]")
        return int(dano_base * 0.5)
    return dano_base

def iniciar_combate(jogador, nome_inimigo, hp_inimigo, defesa_inimigo, min_dano, max_dano, xp_recompensa, fraqueza="Nenhuma", resistencia="Nenhuma"):
    layout.imprimir_lento(f"\n[bold red]COMBATE INICIADO: {nome_inimigo.upper()}[/bold red]")
    layout.tocar_sfx("audio/batalha_inicio.mp3")
    
    mod_defesa = (jogador.get("destreza", 10) + jogador.get("kenjutsu", 10)) // 4
    defesa_jogador = 10 + mod_defesa
    bonus_ataque_inimigo = max_dano // 2
    
    inimigo_analisado = False
    carregando_ataque = False
    
    while hp_inimigo > 0 and jogador["vitalidade"] > 0:
        layout.divisoria()
        max_hp = jogador.get("max_vitalidade", jogador["vitalidade"])
        eter_atual = jogador.get("eter", 0)
        
        ca_mostrado = defesa_inimigo if inimigo_analisado else "??"
        hp_mostrado = hp_inimigo if inimigo_analisado else "??"
        fraq_mostrada = fraqueza if inimigo_analisado else "??"
        res_mostrada = resistencia if inimigo_analisado else "??"
        
        layout.console.print(f"[red]HP:[/red] {jogador['vitalidade']}/{max_hp} | [blue]Defesa:[/blue] {defesa_jogador} | [cyan]Éter:[/cyan] {eter_atual}/{jogador.get('max_eter', 50)} | [yellow]Honra:[/yellow] {jogador.get('honra', 10)}")
        layout.console.print(f"[bold red]Inimigo:[/bold red] {nome_inimigo} | [red]HP:[/red] {hp_mostrado} | [blue]CA:[/blue] {ca_mostrado}")
        if inimigo_analisado:
            layout.console.print(f"[dim]Fraqueza:[/dim] [yellow]{fraq_mostrada}[/yellow] | [dim]Resistência:[/dim] [white]{res_mostrada}[/white]")
        
        if carregando_ataque:
            layout.console.print("\n[bold yellow]⚠️ O INIMIGO ESTÁ CARREGANDO UM ATAQUE DEVASTADOR! ⚠️[/bold yellow]")

        layout.console.print("\n[white]1 - [Atacar][/white] Corte de Kagekiri (Físico).")
        layout.console.print("[cyan]2 - [Passos Fantasmas][/cyan] Esquiva perfeita e ataque nas costas. ([dim]Custo: 10 Éter[/dim]).")
        if "Lâmina de Gelo" in jogador.get("habilidades", []):
            layout.console.print("[blue]3 - [Lâmina de Gelo][/blue] Dano elemental (Gelo) e congela o alvo. ([dim]Custo: 15 Éter[/dim]).")
        
        if not inimigo_analisado:
            layout.console.print("[magenta]4 - [Analisar][/magenta] Revela HP, CA, Fraquezas e Resistências. ([dim]Custo: 5 Éter[/dim]).")
            
        layout.console.print("[yellow]5 - [Golpe Sujo][/yellow] Jogar areia nos olhos (Ataque garantido, mas CUSTA -2 Honra).")
        
        layout.limpar_buffer_teclado()
        acao = input("\nAção: ").strip()
        turno_inimigo = True
        inimigo_congelado = False
        
        # 1. ATAQUE NORMAL
        if acao == "1":
            layout.imprimir_lento("[white]Você avança empunhando a Kagekiri![/white]")
            d20 = random.randint(1, 20)
            jogador.setdefault("atributos_usados", set()).add("kenjutsu")
            total_ataque = d20 + jogador['kenjutsu']
            
            layout.console.print(f"[dim]Rolando Ataque: d20 ({d20}) + Kenjutsu ({jogador['kenjutsu']}) = {total_ataque} vs CA {ca_mostrado}[/dim]")
            time.sleep(1)
            
            if total_ataque >= defesa_inimigo:
                dano_base = random.randint(3, 10) + (jogador['kenjutsu'] // 3)
                dano_final = aplicar_multiplicador(dano_base, "Físico", fraqueza, resistencia)
                hp_inimigo -= dano_final
                layout.imprimir_lento(f"[bold green]ACERTO![/bold green] Você rasgou a defesa inimiga causando {dano_final} de dano.")
            else:
                layout.imprimir_lento("[bold red]ERRO![/bold red] O inimigo bloqueou ou desviou do seu ataque.")
                
        # 2. PASSOS FANTASMAS
        elif acao == "2":
            if eter_atual >= 10:
                jogador["eter"] -= 10
                jogador.setdefault("atributos_usados", update(["destreza", "eter"]))
                layout.imprimir_lento("[bold cyan]PASSOS FANTASMAS![/bold cyan] Você vira névoa, desviando e surgindo nas costas do inimigo.")
                turno_inimigo = False
                
                dano_base = random.randint(5, 12) + (jogador['kenjutsu'] // 3)
                dano_final = aplicar_multiplicador(dano_base, "Físico", fraqueza, resistencia)
                hp_inimigo -= dano_final
                layout.imprimir_lento(f"[green]Apunhalada crítica causando {dano_final} de dano![/green]")
            else:
                layout.imprimir_lento("[bold red]FALHA![/bold red] Sem Éter, seus músculos travam.")
                defesa_jogador -= 5 
                
        # 3. LÂMINA DE GELO
        elif acao == "3" and "Lâmina de Gelo" in jogador.get("habilidades", []):
            if eter_atual >= 15:
                jogador["eter"] -= 15
                jogador.setdefault("atributos_usados", set()).add("eter")
                layout.imprimir_lento("[bold blue]LÂMINA DE GELO![/bold blue] A Kagekiri congela o ar.")
                
                dano_base = random.randint(8, 15) + (jogador['conhecimento'] // 3)
                dano_final = aplicar_multiplicador(dano_base, "Gelo", fraqueza, resistencia)
                hp_inimigo -= dano_final
                
                layout.imprimir_lento(f"[blue]Causou {dano_final} de dano de Gelo. O inimigo está CONGELADO![/blue]")
                inimigo_congelado = True
                turno_inimigo = False
                carregando_ataque = False 
            else:
                layout.imprimir_lento("[bold red]FALHA![/bold red] Falta Éter. A lâmina apenas solta fumaça fria.")
                
        # 4. ANALISAR
        elif acao == "4" and not inimigo_analisado:
            if eter_atual >= 5:
                jogador["eter"] -= 5
                jogador.setdefault("atributos_usados", set()).add("conhecimento")
                inimigo_analisado = True
                layout.imprimir_lento("[bold magenta]Focando o Éter em seus olhos, o mundo desacelera...[/bold magenta]")
                layout.imprimir_lento("As correntes de energia revelam os segredos biológicos e espirituais do alvo.")
            else:
                layout.imprimir_lento("[red]Falta Éter para focar a visão mística.[/red]")

        # 5. GOLPE SUJO (MECÂNICA DE HONRA)
        elif acao == "5":
            jogador["honra"] -= 2
            layout.imprimir_lento("[bold yellow]DESONRA![/bold yellow] Você chuta terra e detritos no rosto do oponente, quebrando o código samurai.")
            dano_base = random.randint(5, 10)
            dano_final = aplicar_multiplicador(dano_base, "Físico", fraqueza, resistencia)
            hp_inimigo -= dano_final
            layout.imprimir_lento(f"[green]O inimigo fica cego momentaneamente! Você acerta um golpe covarde causando {dano_final} de dano.[/green]")
            carregando_ataque = False # Interrompe ataques do inimigo

        else:
            layout.imprimir_lento("[dim]Ação inválida. Você hesitou e perdeu sua chance.[/dim]")
            
        # ================= MORTE DO INIMIGO =================
        if hp_inimigo <= 0:
            layout.imprimir_lento(f"\n[bold white]O {nome_inimigo} desaba sem vida a seus pés. Vitória![/bold white]")
            jogador["xp"] = jogador.get("xp", 0) + xp_recompensa
            layout.console.print(f"[bold yellow]+{xp_recompensa} XP[/bold yellow]")
            
            # Checa o level up independente logo após a vitória
            jogador = checar_level_up(jogador)
            return "vitoria"
            
        # ================= TURNO DO INIMIGO =================
        if turno_inimigo and not inimigo_congelado:
            layout.imprimir_lento(f"\n[dim][Turno do Inimigo: {nome_inimigo}][/dim]")
            
            if carregando_ataque:
                layout.imprimir_lento(f"[bold red]O {nome_inimigo} libera o ATAQUE DEVASTADOR![/bold red]")
                dano_sofrido = random.randint(max_dano, max_dano * 2)
                layout.imprimir_lento(f"[red]Um golpe brutal quebra sua guarda! Você sofre {dano_sofrido} de dano crítico![/red]")
                jogador["vitalidade"] -= dano_sofrido
                carregando_ataque = False
            else:
                if max_dano >= 8 and random.randint(1, 100) <= 25:
                    layout.imprimir_lento(f"[bold yellow]O {nome_inimigo} recua e começa a canalizar uma energia esmagadora para o próximo turno![/bold yellow]")
                    carregando_ataque = True
                else:
                    dado_ataque = random.randint(1, 20)
                    total_ataque = dado_ataque + bonus_ataque_inimigo
                    
                    time.sleep(0.5)
                    layout.console.print(f"[dim]Ataque Inimigo: {dado_ataque} + {bonus_ataque_inimigo} = {total_ataque} vs Sua Defesa ({defesa_jogador})[/dim]")
                    time.sleep(0.5)
                    
                    if total_ataque >= defesa_jogador:
                        dano_sofrido = random.randint(min_dano, max_dano)
                        layout.imprimir_lento(f"[bold red]O {nome_inimigo} acerta o golpe! Você sofre {dano_sofrido} de dano.[/bold red]")
                        jogador["vitalidade"] -= dano_sofrido
                    else:
                        layout.imprimir_lento(f"[blue]Você bloqueia e desvia o ataque do {nome_inimigo} com sucesso![/blue]")
        
        defesa_jogador = 10 + mod_defesa 
            
    if jogador["vitalidade"] <= 0: 
        return "morte"

# ==========================================
# TESTES DE HABILIDADE CENTRALIZADOS
# ==========================================
def rolar_teste(jogador, atributo_nome, dificuldade=20):
    """Rola o teste e registra o uso do atributo para futuro Level Up"""
    import random
    import time
    import layout
    
    valor_atributo = jogador.get(atributo_nome, 10)
    jogador.setdefault("atributos_usados", set()).add(atributo_nome) 
    
    d20 = random.randint(1, 20)
    total = d20 + valor_atributo
    layout.console.print(f"\n[dim]Rolando teste de {atributo_nome.capitalize()}...[/dim]")
    time.sleep(1)
    
    cor = "green" if total >= dificuldade else "red"
    layout.console.print(f"[dim]d20 ({d20}) + {atributo_nome.capitalize()} ({valor_atributo}) = [/dim][bold {cor}]{total}[/bold {cor}] [dim](Dif: {dificuldade})[/dim]")
    time.sleep(1)
    return total >= dificuldade