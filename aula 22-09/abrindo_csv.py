import pandas as pd

df = pd.read_csv("microdados_ed_basica_2021.csv", encoding="unicode_escape", engine="python", sep=";")
#usecold, error_bad_lines=False, quotechar (soluções para erros)

#print(df.head())
#print(df.tail())

df.drop(columns=df.loc[:, "CO_MICRORREGIAO":"DT_ANO_LETIVO_TERMINO"], inplace=True)

print(df.head())
print(df.tail())

df.to_csv("mais_facil.csv", index=False)