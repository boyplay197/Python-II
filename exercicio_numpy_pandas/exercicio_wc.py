import pandas as pd
import numpy as np

# =========================
# LER CSV
# =========================

wc = pd.read_csv("matches_1930_2022.csv")

print("\nCOLUNAS ENCONTRADAS:\n")
print(wc.columns)

# =========================
# FUNÇÃO PARA ACHAR COLUNA
# =========================

def achar_coluna(possibilidades):

    for nome in possibilidades:
        if nome in wc.columns:
            return nome

    return None


# =========================
# ENCONTRAR COLUNAS
# =========================

col_time1 = achar_coluna([
    "home_team",
    "Home Team Name",
    "team1"
])

col_time2 = achar_coluna([
    "away_team",
    "Away Team Name",
    "team2"
])

col_gols1 = achar_coluna([
    "home_score",
    "Home Team Goals",
    "score1"
])

col_gols2 = achar_coluna([
    "away_score",
    "Away Team Goals",
    "score2"
])

col_data = achar_coluna([
    "date",
    "Date"
])

col_copa = achar_coluna([
    "tournament",
    "Tournament",
    "copa"
])

col_rodada = achar_coluna([
    "stage",
    "Stage",
    "Round"
])

col_comparecimento = achar_coluna([
    "attendance",
    "Attendance"
])

# =========================
# RENOMEAR
# =========================

renomear = {}

if col_time1:
    renomear[col_time1] = "time_1"

if col_time2:
    renomear[col_time2] = "time_2"

if col_gols1:
    renomear[col_gols1] = "gols_1"

if col_gols2:
    renomear[col_gols2] = "gols_2"

if col_data:
    renomear[col_data] = "data"

if col_copa:
    renomear[col_copa] = "copa"

if col_rodada:
    renomear[col_rodada] = "rodada"

if col_comparecimento:
    renomear[col_comparecimento] = "comparecimento"

wc = wc.rename(columns=renomear)

# =========================
# DATA E ANO
# =========================

if "data" in wc.columns:

    wc["data"] = pd.to_datetime(
        wc["data"],
        errors="coerce"
    )

    wc["ano"] = wc["data"].dt.year

# =========================
# CONVERSÕES
# =========================

if "gols_1" in wc.columns:
    wc["gols_1"] = pd.to_numeric(
        wc["gols_1"],
        errors="coerce"
    ).fillna(0)

if "gols_2" in wc.columns:
    wc["gols_2"] = pd.to_numeric(
        wc["gols_2"],
        errors="coerce"
    ).fillna(0)

print("\n====================")
print("INFO DATAFRAME")
print("====================\n")

print(wc.info())

# =========================
# SALVAR CSV
# =========================

wc.to_csv("wc_formatado.csv", index=False)

print("\nCSV FORMATADO SALVO!\n")

# =========================
# MAIOR AUDIÊNCIA
# =========================

if "comparecimento" in wc.columns:

    print("\n====================")
    print("MAIOR AUDIÊNCIA")
    print("====================\n")

    maior = wc["comparecimento"].max()

    print(
        wc[
            wc["comparecimento"] == maior
        ]
    )

# =========================
# QUANTIDADE COPAS
# =========================

if "copa" in wc.columns and "ano" in wc.columns:

    print("\n====================")
    print("COPAS")
    print("====================\n")

    print(
        wc.groupby("copa")["ano"]
        .nunique()
    )

# =========================
# TOTAL GOLS
# =========================

if (
    "time_1" in wc.columns and
    "time_2" in wc.columns and
    "gols_1" in wc.columns and
    "gols_2" in wc.columns
):

    g1 = wc.groupby("time_1")["gols_1"].sum()

    g2 = wc.groupby("time_2")["gols_2"].sum()

    gols = g1.add(g2, fill_value=0)

    gols = gols.reset_index()

    gols.columns = [
        "pais",
        "total_gols"
    ]

    gols = gols.sort_values(
        by="total_gols",
        ascending=False
    )

    print("\n====================")
    print("TOTAL DE GOLS")
    print("====================\n")

    print(gols.head(20))

print("\nPROGRAMA FINALIZADO!")