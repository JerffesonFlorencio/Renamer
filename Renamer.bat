@echo off
REM Definir o diretório do projeto
cd "%USERPROFILE%\Documents\Renamer"

REM Ativar o ambiente virtual
call .env\Scripts\activate

REM Executar o script Python
python app.py

REM Pausar a janela para visualizar mensagens
pause