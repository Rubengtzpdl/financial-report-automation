import pandas as pd

df = pd.read_excel("data/raw/estado_resultados.xlsx", index_col="concepto")

indicadores = {
    "Margen Bruto (%)": (df.loc["Utilidad Bruta"] / df.loc["Ingresos Totales"] * 100).round(2),
    "Margen EBITDA (%)": (df.loc["EBITDA"] / df.loc["Ingresos Totales"] * 100).round(2),
    "Margen Neto (%)": (df.loc["Utilidad Neta"] / df.loc["Ingresos Totales"] * 100).round(2),
    "Crecimiento Ingresos (%)": [None, 
        round((920000-850000)/850000*100, 2),
        round((1050000-920000)/920000*100, 2)]
}

df_ind = pd.DataFrame(indicadores, index=["2022", "2023", "2024"]).T.reset_index()
df_ind.columns = ["indicador", "2022", "2023", "2024"]
df_ind.to_excel("data/processed/indicadores.xlsx", index=False)
print("Indicadores calculados")
print(df_ind)