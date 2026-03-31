from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.units import inch
import pandas as pd
from datetime import datetime

doc = SimpleDocTemplate("reports/reporte_financiero.pdf", pagesize=letter)
styles = getSampleStyleSheet()
elements = []

# Estilo título
titulo_style = ParagraphStyle("titulo", parent=styles["Title"],
    fontSize=20, textColor=colors.HexColor("#1F4E79"), spaceAfter=10)
subtitulo_style = ParagraphStyle("subtitulo", parent=styles["Heading2"],
    fontSize=13, textColor=colors.HexColor("#2E75B6"), spaceAfter=8)

# Título
elements.append(Paragraph("Reporte Financiero Automatizado", titulo_style))
elements.append(Paragraph(f"Empresa Ejemplo S.A. de C.V. | Generado: {datetime.now().strftime('%d/%m/%Y %H:%M')}", styles["Normal"]))
elements.append(Spacer(1, 0.3*inch))

# Indicadores clave
elements.append(Paragraph("Indicadores Clave 2024", subtitulo_style))
kpis = [
    ["Indicador", "2022", "2023", "2024"],
    ["Ingresos Totales (MXN)", "850,000", "920,000", "1,050,000"],
    ["Utilidad Neta (MXN)", "115,500", "137,200", "182,000"],
    ["Margen Bruto (%)", "40.0%", "41.3%", "43.8%"],
    ["Margen EBITDA (%)", "25.9%", "27.2%", "30.0%"],
    ["Margen Neto (%)", "13.6%", "14.9%", "17.3%"],
]

tabla = Table(kpis, colWidths=[2.8*inch, 1.2*inch, 1.2*inch, 1.2*inch])
tabla.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1F4E79")),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 10),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.HexColor("#EBF3FB"), colors.white]),
    ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#BDC3C7")),
    ("ALIGN", (1,0), (-1,-1), "CENTER"),
    ("PADDING", (0,0), (-1,-1), 6),
]))
elements.append(tabla)
elements.append(Spacer(1, 0.3*inch))

# Gráficas
elements.append(Paragraph("Análisis Gráfico", subtitulo_style))
elements.append(Image("reports/graficas_financieras.png", width=6.5*inch, height=2.5*inch))
elements.append(Spacer(1, 0.3*inch))

# Conclusiones
elements.append(Paragraph("Conclusiones", subtitulo_style))
conclusiones = [
    "• Los ingresos crecieron un 23.5% entre 2022 y 2024.",
    "• El margen neto mejoró de 13.6% a 17.3%, indicando mayor eficiencia operativa.",
    "• El EBITDA creció un 43.2%, señal positiva de rentabilidad operativa.",
    "• Se recomienda continuar optimizando gastos operativos para mantener la tendencia."
]
for c in conclusiones:
    elements.append(Paragraph(c, styles["Normal"]))
    elements.append(Spacer(1, 0.1*inch))

doc.build(elements)
print("Reporte PDF generado en reports/reporte_financiero.pdf")