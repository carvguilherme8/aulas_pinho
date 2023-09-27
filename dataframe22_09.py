import numpy as np
import pandas as pd

indices = ["The Pacific", "Black Mirror", "CSI", "NCSI", "Lost"]
colunas = ["Nota", "Temporadas", "Episódios"]
dados = [[8.3,1,10],[8.3,6,27],[7.7,15,337],[6.9,14,458],[8.3,6,525]]
df = pd.DataFrame(dados,index=indices,columns=colunas)
print(df, end="\n\n")

print("############# Seleção ##############")
print("Notas:")
print(df["Nota"], end="\n\n")
print("Temporadas e Episódios:")
print(df[["Temporadas","Episódios"]], end="\n\n")

print("############# Loc ILOC ##############")
print("Lost:")
print(df.loc["Lost"], end="\n\n")
print(df.iloc[4], end="\n\n")
print(df.loc["The Pacific", "Temporadas"], end="\n\n")

print("############# Seleção Combinada ##############")
print(df.loc[["The Pacific", "Black Mirror"], ["Temporadas", "Nota"]], end="\n\n")
print(df.loc[:, ["Temporadas", "Nota"]], end="\n\n")

df2 = df.loc[:, ["Temporadas", "Nota"]]


print(type(df.loc[:, ["Temporadas", "Nota"]]))
print(type(df["Nota"]))
print(type(df.loc["NCSI"]))

print(df.columns)
print(type(df.columns))
print(df.columns.values)
print(type(df.columns.values))

df["Coluna Extra"] = df["Nota"]
print(df, end="\n\n")

df.drop("Coluna Extra", axis=1, inplace=True)

df.drop("Lost", axis=0, inplace=True)

print(df)


print("############# Seleção Condicional ##############")

print(df[df["Nota"]>8])
#print(df[df>3])

print("############# Seleção Condicional + múltipla ##############")
print(df[df["Nota"]>8]["Temporadas"], end="\n\n")
print(df[df["Nota"]>8][["Temporadas", "Episódios"]], end="\n\n")

print(df[(df["Nota"]>8) & (df["Temporadas"]>3)])

plataforma = ["HBO", "HBO", "Netflix", "Netflix"]
lancamento = [2020, 2021, 2020, 2021]
indices = pd.MultiIndex.from_arrays([plataforma, lancamento], names=("Plataforma", "Lançamento"))
print("\n\nIndices: ")
print(indices)

print("\nSem Índice: ")
df.reset_index(inplace=True)
print(df)

print("\nRenomear Índice: ")
df.rename(columns={"index":"Nome"}, inplace=True)
print(df)

print("\nConfigurar Índice: ")
df.set_index(indices, inplace=True)
print(df)

print("\nSeleção Multi-Índex: ")
print(df.loc["HBO"].loc[2021])

print("\nCross Selection 1: ")
print(df.xs("HBO"))

print("\nCross Selection 2: ")
print(df.xs(("HBO", 2020)))

print("\nCross Selection 3: ")
print(df.xs(2020, level="Lançamento"))
