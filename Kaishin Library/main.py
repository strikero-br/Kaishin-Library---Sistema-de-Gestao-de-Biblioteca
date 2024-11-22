# main.py

import os
import sys
from model.telaLogin import telaLogin
from utils import resource_path  # Importa a função resource_path do novo módulo utils.py

# Sobrescrevendo a função open para ajustar os caminhos automaticamente
import builtins
original_open = builtins.open

def open(file, *args, **kwargs):
    """Sobrescreve open para ajustar automaticamente o caminho dos arquivos."""
    file = resource_path(file)  # Ajusta o caminho com resource_path
    return original_open(file, *args, **kwargs)

builtins.open = open  # Substitui open globalmente

# Importações para garantir que o PyInstaller inclua os módulos
import model.cliente
import model.bibliotecario
import model.emprestimos
import model.livro
import model.usuario

if __name__ == "__main__":
    caminho_logo = resource_path("imagens", "logo.png")  # Exemplo de ajuste manual para imagens
    tela_login = telaLogin()
