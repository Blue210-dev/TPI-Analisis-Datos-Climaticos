import pandas as pd
import matplotlib.pyplot as plt

def analizar_clima():
    # 1. Carga del dataset oficial utilizando la ruta relativa requerida
    ruta_datos = "datos/annual.csv"
    df = pd.read_csv(ruta_datos)
    
    # Filtramos por una sola fuente (por ejemplo, GISTEMP) para no duplicar datos en el gráfico
    if 'Source' in df.columns:
        df = df[df['Source'] == 'GISTEMP']
    
    # 2. Procesamiento estadístico basado en las columnas reales ('Year' y 'Mean')
    # Ajustamos la lógica para cumplir con los indicadores solicitados por la cátedra
    temp_media_historica = df['Mean'].mean()
    temp_max_registrada = df['Mean'].max()
    temp_min_registrada = df['Mean'].min()
    
    print("=== REPORTE CLIMÁTICO GLOBAL (GISTEMP) ===")
    print(f"Temperatura/Anomalía Media Histórica: {temp_media_historica:.4f}")
    print(f"Valor Máximo Registrado: {temp_max_registrada:.4f}")
    print(f"Valor Mínimo Registrado: {temp_min_registrada:.4f}")
    print("==========================================")
    
    # 3. Generación del gráfico estadístico evolutivo en el tiempo
    # Ordenamos por año para que la línea no se cruce de forma caótica
    df = df.sort_values('Year')
    
    plt.figure(figsize=(10, 5))
    plt.plot(df['Year'], df['Mean'], marker='.', color='crimson', linestyle='-', label='Anomalía Media Anual')
    
    plt.title('Evolución Histórica de la Temperatura Global')
    plt.xlabel('Año')
    plt.ylabel('Desviación de Temperatura / Media')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    
    # 4. Exportación del gráfico a la carpeta /resultados
    ruta_grafico = "resultados/grafico_clima.png"
    plt.savefig(ruta_grafico)
    plt.close()
    print(f"Gráfico guardado exitosamente en: {ruta_grafico}")

if __name__ == "__main__":
    analizar_clima()
