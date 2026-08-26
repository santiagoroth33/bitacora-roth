# Receta: leer un CSV con encoding Latin-1 y números con separador de miles

## Cuándo usarla

Fuentes públicas uruguayas (INE, intendencias) suelen exportar CSVs con
encoding Latin-1 en vez de UTF-8, y números formateados con puntos como
separador de miles y coma como decimal.

## Procedimiento

```python
import pandas as pd

# 1. Leer con el encoding correcto
df = pd.read_csv("poblacion.csv", encoding="latin-1", sep=";")

# 2. Limpiar columnas numéricas con formato de miles
df["poblacion"] = (
    df["poblacion"]
    .astype(str)
    .str.replace(".", "", regex=False)   # quita separador de miles
    .str.replace(",", ".", regex=False)  # coma decimal -> punto decimal
    .astype(float)
    .astype(int)
)

# 3. Verificar que no quedaron nulos inesperados
assert df["poblacion"].isna().sum() == 0
```

## Cómo detectar si un archivo tiene este problema

- Si aparecen caracteres raros (`Ã³`, `Ã©`) en vez de tildes → problema de encoding.
- Si una columna que debería ser numérica aparece como `object` en
  `df.dtypes` → probablemente tiene separadores de miles como texto.

## Notas

- Si `latin-1` no funciona, probar `encoding="cp1252"` (Windows-1252),
  que es otra variante común en archivos exportados desde Excel.
