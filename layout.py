"""
Módulo de layout com rich.
"""
from rich.layout import Layout
from rich import print

def _ler(entrada, isArquivo):
    if isArquivo:
        with open(entrada, "r", encoding="utf-8") as f:
            return f.read()
    return entrada

def layout_duplo(entrada, isArquivo=False):
    """
    Layout horizontal.
    """
    layout = Layout()
    layout.split_row(
        Layout(_ler(entrada, isArquivo)),
        Layout("Direita")
    )
    print(layout)

def layout_vertical(entrada, isArquivo=False):
    """
    Layout vertical.
    """
    layout = Layout()
    layout.split_column(
        Layout("Topo"),
        Layout(_ler(entrada, isArquivo))
    )
    print(layout)
