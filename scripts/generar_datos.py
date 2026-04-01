import pandas as pd

# Estado de resultados simulado
data = {
    "concepto": [
        "Ingresos Totales", "Costo de Ventas", "Utilidad Bruta",
        "Gastos Operativos", "EBITDA", "Depreciación",
        "EBIT", "Gastos Financieros", "Utilidad Antes de Impuestos",
        "Impuestos", "Utilidad Neta"
    ],
    "2022": [850000, 510000, 340000, 120000, 220000, 30000, 190000, 25000, 165000, 49500, 115500],
    "2023": [920000, 540000, 380000, 130000, 250000, 32000, 218000, 22000, 196000, 58800, 137200],
    "2024": [1050000, 590000, 460000, 145000, 315000, 35000, 280000, 20000, 260000, 78000, 182000]
}

df = pd.DataFrame(data)
df.to_excel("data/raw/estado_resultados.xlsx", index=False)
print("Datos generados")
print(df)
