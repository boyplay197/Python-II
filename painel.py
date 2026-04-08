"""
Módulo de painéis com rich.
"""
from rich.panel import Panel
from rich import print

def _ler(entrada, isArquivo):
    if isArquivo:
        with open(entrada, "r", encoding="utf-8") as f:
            return f.read()
    return entrada

def painel_simples(entrada, isArquivo=False):
    """
    Painel simples.
    """
    print(Panel(_ler(entrada, isArquivo), title="Painel"))

def painel_destacado(entrada, isArquivo=False):
    """
    Painel com borda vermelha.
    """
    print(Panel(_ler(entrada, isArquivo), title="Destaque", border_style="red"))
