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
