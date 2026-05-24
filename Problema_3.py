# Fase 5 Codigo en phyton
# Problema 3
#Jesus Manuel Velasquez Arias - Estudiante de Ingenieria de la UNAD - Fundamentos de Programacion

def calcular_cantidad_a_pedir(StockActual, StockMinimo):
    if StockActual < StockMinimo:
        return StockMinimo - StockActual
    else:
        return 0


inventario = [
    ["Articulo1", "Teclado", 8, 15],
    ["Articulo2", "Mouse", 20, 10],
    ["Articulo3", "Monitor", 4, 8],
    ["Articulo4", "Cable HDMI", 30, 25],
    ["Articulo5", "Memoria USB", 6, 12]
]


print("INFORME DE REABASTECIMIENTO DE INVENTARIO")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    StockActual = articulo[2]
    StockMinimo = articulo[3]

    CantidadAPedir = calcular_cantidad_a_pedir(StockActual, StockMinimo)

    print(f"Código: {codigo}")
    print(f"Artículo: {nombre}")
    print(f"Stock actual: {StockActual}")
    print(f"Stock mínimo requerido: {StockMinimo}")
    print(f"Cantidad a pedir: {CantidadAPedir}")
    print()