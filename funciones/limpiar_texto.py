"""
limpiar_texto.py

Utilidad para normalizar texto de columnas categóricas (nombres de
departamentos, municipios, etc.) antes de usarlas como clave de unión
entre distintas fuentes de datos.
"""

import unicodedata


def limpiar_texto(s: str) -> str:
    """
    Normaliza un string: pasa a minúsculas, quita tildes/diacríticos
    y recorta espacios al inicio/final.

    Parámetros
    ----------
    s : str
        Texto a normalizar.

    Retorna
    -------
    str
        Texto normalizado.

    Ejemplo
    -------
    >>> limpiar_texto("  Canelones ")
    'canelones'
    >>> limpiar_texto("Tacuarembó")
    'tacuarembo'
    """
    s = s.strip().lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s


# --- Caso de prueba ---
if __name__ == "__main__":
    assert limpiar_texto("  Canelones ") == "canelones"
    assert limpiar_texto("Tacuarembó") == "tacuarembo"
    assert limpiar_texto("MONTEVIDEO") == "montevideo"
    print("Todos los casos de prueba pasaron.")
