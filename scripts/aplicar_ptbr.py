#!/usr/bin/env python3
"""Tradução em português brasileiro para a interface Android do easy-ps2-fpkg.
Aplica substituições EXATAS de literais C#; não traduz argumentos do emulador.
Execute na raiz do repositório ou passe a raiz como primeiro argumento.
"""
from pathlib import Path
import sys

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
source = root / 'src' / 'ps2fpkg.android' / 'MainActivity.cs'
project = root / 'src' / 'ps2fpkg.android' / 'ps2fpkg.android.csproj'
if not source.is_file() or not project.is_file():
    sys.exit('ERRO: arquivo Android não encontrado. Execute na raiz do easy-ps2-fpkg.')

# IMPORTANTE: traduzimos o texto mostrado ao usuário, não os valores técnicos.
T = {
    'PS2 → PS4/PS5 fpkg': 'PS2 → PS4/PS5 • Conversor de PKG',
    'Pick a PS2 .iso (or .7z/.zip), choose options, tap Convert. ': 'Selecione um jogo de PS2 (.iso, .chd ou arquivo compactado), configure as opções e toque em Converter. ',
    'Emulator assets download once (~109 MB). The .pkg lands in the output folder.': 'Os arquivos do emulador são baixados uma vez (~109 MB). O PKG será salvo na pasta de destino.',
    "Grant 'All files access' (required)": 'Permitir acesso a todos os arquivos (obrigatório)',
    'Storage access: granted ✓': 'Acesso aos arquivos autorizado ✓',
    'Game file (.iso / .7z / .zip)': 'Arquivo do jogo (.iso, .chd, .7z, .zip, .rar)',
    'Pick': 'Selecionar',
    'Emulator core': 'Versão do emulador',
    'Jak v2 = widest compatibility. Rogue v1 = try if a game misbehaves on Jak.': 'Jak v2 oferece maior compatibilidade. Se houver problemas, experimente Rogue v1.',
    'Graphics': 'Gráficos',
    'Internal resolution (uprender)': 'Resolução interna (uprender)',
    'Render scale. 1×1 = native (fastest, best for heavy games); higher = sharper but heavier.': 'Escala de renderização: 1×1 = nativa (mais rápida); valores maiores melhoram a nitidez, mas exigem mais desempenho.',
    'Default': 'Padrão',
    'Upscale filter': 'Filtro de aprimoramento',
    'How the image is smoothed when scaled to your screen.': 'Define como a imagem é suavizada ao ser ampliada para a tela.',
    'None': 'Nenhum',
    'Display mode': 'Modo de exibição',
    'How the picture fills the screen.': 'Define como a imagem ocupa a tela.',
    'Full': 'Tela cheia',
    'Fit': 'Ajustar',
    'Original': 'Original',
    'Multitap (4-player adapter)': 'Multitap (adaptador para até 4 jogadores)',
    'Enable the PS2 multitap on a controller port. Leave Off unless a game needs 3–4 pads.': 'Ative o multitap em uma porta de controle. Mantenha desativado, exceto se o jogo exigir 3 ou 4 controles.',
    'Off': 'Desativado',
    'Port 1': 'Porta 1',
    'Port 2': 'Porta 2',
    'Both': 'Ambas',
    'Conversion speed (heat)': 'Velocidade da conversão (temperatura)',
    'Packing maxes the CPU and warms the phone — plug in for big games. Auto adapts to temperature. You can change this mid-convert. (Device: {_cores} cores.)': 'A conversão usa bastante o processador e pode aquecer o celular. Para jogos grandes, conecte o carregador. Automático adapta a velocidade à temperatura; você pode alterar durante a conversão. (Aparelho: {_cores} núcleos.)',
    'Auto': 'Automático',
    'Balanced': 'Equilibrado',
    'Cool': 'Frio',
    'Advanced (optional)': 'Configurações avançadas (opcional)',
    'Custom title (blank = auto from game ID)': 'Nome personalizado (vazio = identificar pelo jogo)',
    'Extra emulator flags, one per line (e.g. ee-cycle-rate=1)': 'Parâmetros extras do emulador, um por linha (ex.: ee-cycle-rate=1)',
    'Cover art': 'Capa do jogo',
    "Use the game's official box art for the home-screen icon & background (downloaded by serial). Pick files below to override.": 'Usar a capa oficial do jogo no ícone e no fundo do PS4 (obtida pelo código do jogo). Se preferir, selecione suas próprias imagens abaixo.',
    'Official cover': 'Capa oficial',
    'Emulator default': 'Padrão do emulador',
    'Custom art (optional)': 'Imagens personalizadas (opcional)',
    'Override with your own icon (512×512 PNG) & background (1920×1080 PNG).': 'Use seu próprio ícone (PNG 512×512) e imagem de fundo (PNG 1920×1080).',
    'Pick game icon': 'Selecionar ícone do jogo',
    'Pick background': 'Selecionar imagem de fundo',
    'Output folder': 'Pasta de destino',
    'Convert': 'Converter',
    'Converting…': 'Convertendo…',
    'Pause': 'Pausar',
    'Resume': 'Retomar',
    'Log': 'Registro da conversão',
    'No file picker app available.': 'Nenhum gerenciador de arquivos disponível.',
    'Selected: ': 'Selecionado: ',
    "Couldn't use that folder; keeping ": 'Não foi possível usar a pasta; mantida: ',
    'Icon: ': 'Ícone: ',
    'Background: ': 'Fundo: ',
    "Couldn't read image: ": 'Não foi possível ler a imagem: ',
    'Grant All files access first.': 'Primeiro, autorize o acesso a todos os arquivos.',
    'Pick a game file first.': 'Selecione um arquivo de jogo primeiro.',
    'Locating ': 'Localizando ',
    ' on storage...': ' no armazenamento...',
    'Found: ': 'Encontrado: ',
    'Not found on disk — importing a copy (this can take a while)...': 'Arquivo não localizado no armazenamento — importando uma cópia (pode demorar)...',
    'DONE ✅ ({r.Checks}/{r.Checks} checks OK)': 'CONCLUÍDO ✅ ({r.Checks}/{r.Checks} verificações OK)',
    'Size : ': 'Tamanho: ',
    'Title : ': 'Título: ',
    'Done — pkg saved.': 'Concluído! O arquivo PKG foi salvo.',
    'ERROR: ': 'ERRO: ',
    '⚙ speed → {sel}': '⚙ velocidade → {sel}',
    ' (adapts to temperature)': ' (ajuste automático por temperatura)',
    '▶ resumed': '▶ conversão retomada',
    '⏸ paused — CPU idle; tap Resume to continue': '⏸ pausado — toque em Retomar para continuar',
    'normal': 'normal',
    'light': 'leve',
    'moderate': 'moderado',
    'SEVERE': 'GRAVE',
    'CRITICAL': 'CRÍTICO',
    'EMERGENCY': 'EMERGÊNCIA',
    'SHUTDOWN': 'DESLIGAMENTO',
    '🌡 device is {names[s]}': '🌡 temperatura do aparelho: {names[s]}',
    " — consider 'Cool' or pause": ' — considere usar o modo Frio ou pausar',
    '🌡 device cooled down': '🌡 temperatura do aparelho reduzida',
    '🌡 auto-paused (too hot) — resumes when it cools': '🌡 pausa automática por aquecimento — retorna quando esfriar',
    '🌡 auto-throttled to {n} cores': '🌡 controle térmico: {n} núcleos em uso',
}
# Removemos chaves de valor igual: nenhuma alteração desnecessária.
T = {k: v for k, v in T.items() if k != v}
body = source.read_text(encoding='utf-8')
if 'Arquivo do jogo (.iso, .chd, .7z, .zip, .rar)' in body and 'Velocidade da conversão (temperatura)' in body:
    print('Tradução já aplicada; nenhuma alteração no código.')
else:
    mandatory = ['Game file (.iso / .7z / .zip)', 'Conversion speed (heat)', 'Pick game icon', "Grant 'All files access' (required)", 'Convert']
    absent = [s for s in mandatory if '"' + s + '"' not in body]
    if absent:
        sys.exit('ERRO: a versão do upstream mudou. Não é seguro aplicar esta tradução: ' + ', '.join(absent))
    count, missing = 0, []
    for old, new in T.items():
        fragment = '"' + old + '"'
        if fragment not in body:
            missing.append(old)
            continue
        count += body.count(fragment)
        body = body.replace(fragment, '"' + new + '"')
    # Uma mensagem térmica é interpolada com outros literais e precisa de ajuste textual.
    body = body.replace('🌡 device is ', '🌡 temperatura do aparelho: ')
    # Não traduzir os valores técnicos (strings entre aspas minúsculas).
    for token in ['"auto"', '"full"', '"cool"', '"bal"', '"Jak v2"', '"Rogue v1"', '"both"', '"none"']:
        if token not in body:
            sys.exit('ERRO: identificador do motor aparentemente alterado: ' + token)
    # Nome exibido pelo launcher, preservando o nome do projeto de origem.
    body = body.replace('[Activity(Label = "PS2 fPKG"', '[Activity(Label = "PS2 FPKG PT-BR"')
    source.write_text(body, encoding='utf-8')
    print(f'Textos traduzidos em MainActivity.cs: {count} ocorrências.')
    if missing:
        print(f'Aviso: {len(missing)} expressões opcionais não encontradas. Exemplos: {missing[:8]}')

# Permite instalar a tradução lado a lado com o aplicativo original.
proj = project.read_text(encoding='utf-8')
proj2 = proj.replace('<ApplicationId>com.spiral.ps2fpkg</ApplicationId>', '<ApplicationId>com.spiral.ps2fpkg.ptbr</ApplicationId>')
proj2 = proj2.replace('<ApplicationDisplayVersion>1.0</ApplicationDisplayVersion>', '<ApplicationDisplayVersion>1.2.0-ptbr</ApplicationDisplayVersion>')
if proj2 == proj and 'com.spiral.ps2fpkg.ptbr' not in proj:
    sys.exit('ERRO: ApplicationId do csproj desconhecido.')
project.write_text(proj2, encoding='utf-8')
print('Identificador: com.spiral.ps2fpkg.ptbr')
print('Motor de conversão original preservado.')
