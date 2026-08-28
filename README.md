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


/home/legal/Documentos/Renamer

e o app.py usa a .venv, podemos criar um atalho executável na Área de Trabalho que já abre o app.py usando o Python da .venv.

Primeiro, dentro do terminal, crie o script de inicialização:

cd ~/Documentos/Renamer

nano iniciar.sh

Cole:

#!/bin/bash

cd /home/legal/Documentos/Renamer
exec /home/legal/Documentos/Renamer/.venv/bin/python app.py

Salve com:

Ctrl + O
Enter
Ctrl + X

Dê permissão:

chmod +x ~/Documentos/Renamer/iniciar.sh

Agora crie o atalho na Área de Trabalho automaticamente:

DESKTOP="$(xdg-user-dir DESKTOP)"

cat > "$DESKTOP/Renamer.desktop" <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Renamer
Comment=Executar Renamer
Exec=/home/legal/Documentos/Renamer/iniciar.sh
Path=/home/legal/Documentos/Renamer
Terminal=false
Icon=utilities-terminal
Categories=Utility;
EOF

Depois dê permissão:

chmod +x "$DESKTOP/Renamer.desktop"

E marque como confiável no Ubuntu:

gio set "$DESKTOP/Renamer.desktop" metadata::trusted true

Agora deve aparecer na Área de Trabalho um ícone chamado Renamer. Ao dar dois cliques, ele executará:

.venv/bin/python app.py

sem precisar abrir o terminal nem ativar a .venv manualmente.

Se quiser ver o terminal e os logs quando abrir, altere esta linha:

Terminal=false

para:

Terminal=true
