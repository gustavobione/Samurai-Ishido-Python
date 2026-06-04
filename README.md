# 🗡️ Samurai Ishido

**Samurai Ishido** é um RPG de aventura narrativa em texto (Text-Based RPG) ambientado em um universo de *Dark Fantasy* Oriental. Focado em escolhas morais, combates táticos e exploração, o jogo leva o jogador por uma jornada de luto, sobrevivência e vingança contra um império corrompido pela magia negra.

Desenvolvido por **Gustavo Teixeira Bione** e **Lucas Ferraz Valença Parente**.

---

## 📜 Sinopse

Há vinte anos, durante a Noite das Sombras, o Alto Sacerdote Kuroi Shin'en abraçou o núcleo do Astrolábio Celestial, rasgando o véu dimensional. O Xogum foi assassinado, o império de Takenoko caiu e o Abismo inundou o mundo.

Você é **Ishido**, o último herdeiro do Clã Shiro. Salvo ainda bebê pelo antigo capitão Kazunari, você foi forjado no isolamento congelado da montanha como uma arma viva. Agora, com a morte do seu mestre, você empunha a *Kagekiri* (Corta-Sombras) — uma katana forjada de um meteorito ancestral — e desce a montanha para enfrentar o Shogunato de Cinza. O destino de Takenoko repousa na lâmina da sua espada e no peso da sua Honra.

---

## ⚙️ Características e Sistemas

* **Combate Dinâmico e Tático:** Lute rolando dados (D20 + Atributos) contra a Classe de Armadura (CA) dos inimigos. Descubra fraquezas elementais, use esquivas perfeitas e magias consumindo Éter.
* **Sistema de Honra:** Suas ações importam. Abates furtivos e "golpes sujos" poupam HP, mas drenam sua Honra. Duelos abertos e atitudes heroicas a elevam. Chegar a zero de Honra resulta em *Game Over* (Seppuku).
* **Múltiplas Rotas e Finais:** Cada capítulo oferece caminhos distintos (como as Minas de Enxofre vs. a Forja Principal). Suas rotas definem quais itens você encontra e quais desafios enfrentará no futuro.
* **Progressão de Personagem:** Evolua seus atributos (Kenjutsu, Destreza, Conhecimento) ganhando XP em combates ou através da prática passiva ao meditar nas fogueiras.
* **Interface Imersiva:** Painel de status em tempo real e textos estilizados utilizando a biblioteca `rich`, além de suporte a SFX e trilha sonora via `pygame`.

---

## 💻 Pré-requisitos

Para rodar o jogo, você precisará do **Python 3.8+** instalado na sua máquina. 

O jogo foi otimizado com a biblioteca nativa `msvcrt` para captura de teclado dinâmico no Windows, garantindo que o texto sendo impresso lentamente possa ser "pulado" sem bugar o terminal.

### Bibliotecas Externas Utilizadas:
* `rich` (Para a interface gráfica no terminal: cores, tabelas e painéis)
* `pygame` (Para reprodução de áudio e efeitos sonoros)

---

## 🚀 Como Instalar e Rodar

**1. Clone o repositório**
```bash
git clone [https://github.com/seu-usuario/samurai-ishido.git](https://github.com/seu-usuario/samurai-ishido.git)
cd samurai-ishido
```

2. Crie um Ambiente Virtual (Opcional, mas recomendado)

```Bash
python -m venv venv
# Para ativar no Windows:
venv\Scripts\activate
# Para ativar no Mac/Linux:
source venv/bin/activate
```

3. Instale as dependências

```Bash
pip install -r requirements.txt
```

4. Prepare as pastas de áudio (Opcional)
Se desejar a experiência completa com som, crie uma pasta chamada audio na raiz do projeto e adicione seus arquivos .mp3 correspondentes aos chamados no código (ex: audio/vento_montanha.mp3, audio/saque_espada.mp3, audio/batalha_inicio.mp3). O jogo possui tratamento de erro e funcionará normalmente em silêncio caso os arquivos não sejam encontrados.

PS: Parte de audio está parametrizada mas ainda não foi implementada, somente em funções futuras.

5. Inicie o jogo

```Bash
python História/_main.py
```

## 🏗️ Estrutura do Projeto

O código foi componentizado para facilitar a expansão narrativa:

main.py - O gestor principal que conecta os capítulos.

layout.py - Interface de usuário, formatação de textos (Rich) e áudio (Pygame).

sistemas.py - Motor de RPG (Rolagens, Combate, Level Up, Fogueiras e Cálculos de Dano).

capitulo_0.py a boss.py - Os arquivos de roteiro contendo as árvores de decisões, rotas e narrativas do jogo.