"""
Módulo de estilos usando rich.
"""
from rich import print

def _ler(entrada, isArquivo):
    if isArquivo:
        with open(entrada, "r", encoding="utf-8") as f:
            return f.read()
    return entrada

def texto_colorido(entrada, isArquivo=False):
    """
    Exibe texto em azul negrito.
    """
    print(f"[bold blue]{_ler(entrada, isArquivo)}[/bold blue]")

def texto_destacado(entrada, isArquivo=False):
    """
    Exibe texto com fundo amarelo.
    """
    print(f"[black on yellow]{_ler(entrada, isArquivo)}[/black on yellow]")

