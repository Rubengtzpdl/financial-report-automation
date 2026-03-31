import subprocess
import sys

scripts = [
    "scripts/generar_datos.py",
    "scripts/calcular_indicadores.py",
    "scripts/generar_graficas.py",
    "scripts/generar_reporte.py"
]

print("🚀 Iniciando automatización de reporte financiero...\n")
for script in scripts:
    print(f"▶ Corriendo {script}...")
    result = subprocess.run([sys.executable, script], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"❌ Error en {script}: {result.stderr}")
        break

print("Reporte generado exitosamente.")