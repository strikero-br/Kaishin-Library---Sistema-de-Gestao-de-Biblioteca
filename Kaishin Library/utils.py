import os
import sys

def resource_path(*relative_path):
    """Retorna o caminho absoluto, considerando o executável ou o ambiente de desenvolvimento."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, *relative_path)
