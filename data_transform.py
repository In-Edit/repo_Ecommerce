#Proyecto Final
import pandas as pd

# Ruta del archivo CSV intermedio
archivo_csv = 'ventasEcommerce.csv'

try:
    # Leer el archivo CSV
  data = pd.read_csv(archivo_csv)
    
    # Ordenar los datos por nombre
  data_ordenada = data.sort_values(by='Country')
   
    # Guardar archivo CSV ordenado y filtrado
    archivo_csv_ordenado = 'ventasEcommerce_ordenada.csv'
    data_ordenada.to_csv(archivo_csv_ordenado, index=False, encoding='utf-8')
    
    print(f"Datos exportados exitosamente a {archivo_csv_ordenado}")
except Exception as e:
    print(f"Error al transformar los datos: {e}")