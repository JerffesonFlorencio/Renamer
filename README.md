Caso não fucione
# 1) Desativar o venv atual (se estiver ativo)
deactivate 2>$null

# 2) Apagar o venv antigo
Remove-Item -Recurse -Force .venv

# 3) Criar um novo venv (ajuste a versão se precisar)
py -3.12 -m venv .venv
# Se não tiver o launcher 'py', use o Python instalado:
# "C:\Program Files\Python312\python.exe" -m venv .venv

# 4) Ativar
.\.venv\Scripts\Activate.ps1

# (Se der erro de política de execução)
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# 5) Garantir pip funcional
python -m ensurepip --upgrade
python -m pip install --upgrade pip

# 6) Instalar dependências
python -m pip install -r requirements.txt


Primeiro, abra o terminal dentro da pasta Renamer e rode:
</>Bash
pwd

Vai aparecer algo parecido com:
</>Bash
/home/legal/Documentos/Renamer

Guarde esse caminho.

Depois descubra automaticamente a pasta da Área de Trabalho:
</>Bash
DESKTOP=$(xdg-user-dir DESKTOP)

Agora crie o atalho:
</>Bash
nano "$DESKTOP/Renamer.desktop"

Cole isto dentro:
</>ini
[Desktop Entry]
Version=1.0
Type=Application
Name=Renomeador de Arquivos
Comment=Abrir Renomeador de Arquivos
Exec=/home/legal/Documentos/Renamer/.venv/bin/python /home/legal/Documentos/Renamer/app.py
Path=/home/legal/Documentos/Renamer
Icon=utilities-terminal
Terminal=false
Categories=Utility;

⚠️ Importante: troque:

/home/legal/Documentos/Renamer

pelo caminho que apareceu no seu pwd.

Salve no nano com:

CTRL + O
ENTER
CTRL + X

Depois dê permissão para executar:
</>Bash
chmod +x "$DESKTOP/Renamer.desktop"

E marque o atalho como confiável:
</>Bash
gio set "$DESKTOP/Renamer.desktop" metadata::trusted true

Pronto. Deve aparecer na sua Área de Trabalho como Renomeador de Arquivos. Ao dar dois cliques, ele vai executar diretamente:
</>Bash
.venv/bin/python → app.py