import argparse
from personalizador import layout, painel, progresso, estilo


def main():
    parser = argparse.ArgumentParser(
        description="Personalizador de texto com Rich"
    )

    parser.add_argument("mensagem", help="Texto ou caminho do arquivo")

    parser.add_argument(
        "-a", "--arquivo",
        action="store_true",
        help="Indica que a entrada é um arquivo"
    )

    parser.add_argument(
        "-m", "--modulo",
        required=True,
        help="layout, painel, progresso, estilo"
    )

    parser.add_argument(
        "-f", "--funcao",
        required=True,
        help="Função do módulo"
    )

    args = parser.parse_args()

    if args.modulo == "layout":
        funcoes = {
            "layout_duplo": layout.layout_duplo,
            "layout_vertical": layout.layout_vertical
        }

    elif args.modulo == "painel":
        funcoes = {
            "painel_simples": painel.painel_simples,
            "painel_destacado": painel.painel_destacado
        }

    elif args.modulo == "progresso":
        funcoes = {
            "progresso_simples": progresso.progresso_simples,
            "progresso_rapido": progresso.progresso_rapido
        }

    elif args.modulo == "estilo":
        funcoes = {
            "texto_colorido": estilo.texto_colorido,
            "texto_destacado": estilo.texto_destacado
        }

    else:
        print("Módulo inválido")
        return

    if args.funcao in funcoes:
        funcoes[args.funcao](args.mensagem, args.arquivo)
    else:
        print("Função inválida")
        print("Disponíveis:", list(funcoes.keys()))


if __name__ == "__main__":
    main()