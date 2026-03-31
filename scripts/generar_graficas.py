import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
df = pd.read_excel("data/raw/estado_resultados.xlsx", index_col="concepto")
años = ["2022", "2023", "2024"]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Gráfica 1 - Ingresos vs Utilidad Neta
axes[0].bar(años, df.loc["Ingresos Totales"], color="#3498DB", label="Ingresos Totales", alpha=0.8)
axes[0].bar(años, df.loc["Utilidad Neta"], color="#2ECC71", label="Utilidad Neta", alpha=0.8)
axes[0].set_title("Ingresos vs Utilidad Neta", fontweight="bold")
axes[0].set_ylabel("MXN")
axes[0].legend()

# Gráfica 2 - Márgenes
margenes = {
    "Margen Bruto": [40.0, 41.3, 43.8],
    "Margen EBITDA": [25.9, 27.2, 30.0],
    "Margen Neto": [13.6, 14.9, 17.3]
}
for nombre, valores in margenes.items():
    axes[1].plot(años, valores, marker="o", linewidth=2.5, label=nombre)
axes[1].set_title("Evolución de Márgenes (%)", fontweight="bold")
axes[1].set_ylabel("%")
axes[1].legend()

plt.tight_layout()
plt.savefig("reports/graficas_financieras.png", dpi=150)
plt.show()
print("Gráficas guardadas")