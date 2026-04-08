"""
Módulo de progresso com rich.
"""
from rich.progress import track
from time import sleep

def _ler(entrada, isArquivo):
    if isArquivo:
        with open(entrada, "r", encoding="utf-8") as f:
            return f.read()
    return entrada

def progresso_simples(entrada, isArquivo=False):
    """
    Barra de progresso padrão.
    """
    for _ in track(range(10), description=_ler(entrada, isArquivo)):
        sleep(0.1)

def progresso_rapido(entrada, isArquivo=False):
    """
    Barra de progresso rápida.
    """
    for _ in track(range(5), description=_ler(entrada, isArquivo)):
        sleep(0.05)
