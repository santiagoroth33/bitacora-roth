# Error: fechas que no ordenan cronológicamente

## Cómo se manifestó

Al graficar una serie temporal de matrícula escolar, las fechas
aparecían fuera de orden en el eje X, aunque el CSV original estaba
ordenado correctamente fila por fila.

## Causa

La columna `fecha` se había leído como texto (`dtype: object`) en vez
de como tipo fecha (`datetime64`), así que al graficar u ordenar se
aplicaba orden alfabético en vez de cronológico. Por ejemplo,
"2026-02-01" quedaba después de "2026-10-01" porque "1" < "2"
alfabéticamente en la posición del mes.

## Cómo lo detecté

Ejecuté `df.dtypes` y vi que la columna `fecha` figuraba como `object`
en lugar de `datetime64[ns]`.

## Solución

```python
df["fecha"] = pd.to_datetime(df["fecha"])
df = df.sort_values("fecha")
```

## Cómo evitarlo en el futuro

Después de leer cualquier CSV con columnas de fecha, correr
`df.dtypes` como chequeo de rutina antes de graficar o unir tablas.
