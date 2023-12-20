"""
Módulo principal del API
"""
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

#Crea instancia de fastapi
app = FastAPI()
app.title = 'Aplicación de ventas'
app.version = '1.0.1'
ventas = [
    {
        "id": 1,
        "fecha": "01/01/23",
        "tienda": "Tienda01",
        "importe": 2500
    },
    {
        "id": 2,
        "fecha": "22/01/23",
        "tienda": "Tienda02",
        "importe": 4500
    }
]

# Crea punto de entrada o endpoint
@app.get('/', tags=['Inicio'])
def mensaje():
    """
    Esta función imprime un mensaje
    Returns:
    str: Emite el msn
    """
    return HTMLResponse('<h2>Titulo html desde FastAPI</h2>')

@app.get('/ventas', tags=['Ventas'])
def dame_ventas():
    """
    Esta función regresa las ventas por tienda
    Returns:
    str: Emite el msn
    """
    return ventas

@app.get('/ventas{id}', tags=['Ventas'])
def dame_venta_por_id(venta_id:int):
    """
    Esta función regresa las ventas por tienda de acuerdo al id
    Returns:
    str: Emite el msn
    """
    for elem in ventas:
        if elem['id']==venta_id:
            return elem
    return []

@app.get('/ventas/', tags=['Ventas'])
def dame_ventas_por_tienda(tienda:str):
    """
    Esta función regresa las ventas por tienda de acuerdo al nombre de la tienda
    Returns:
    str: Emite la información de la tienda
    """
    return [elem for elem in ventas if elem['tienda']==tienda]

@app.post('/ventas', tags=['Ventas'])
def crea_venta(id_tienda: int = Body(), fecha: str = Body(),
               tienda: str = Body(), importe: float = Body()):
    """
    Agrega a la lista de ventas la nueva tienda

    Args:
        * id_tienda (int, optional):Id de la tienda.
        * fecha (str, optional):Fecha de creación de la tienda.
        * tienda (str, optional): Nombre de la tienda.
        * importe (float, optional): El importe de la tienda.

    Returns:
        ventas(list): Retorna la lista de todas las tiendas
    """
    ventas.append(
        {
            "id": id_tienda,
            "fecha": fecha,
            "tienda": tienda,
            "importe": importe
        }
    )
    return ventas

@app.put('/ventas/{id}',tags=['Ventas'])
def actualiza_ventas(id_tienda: int, fecha: str = Body(),
                     tienda: str = Body(), importe: float = Body()):
    """
    Actualiza la información de la nueva tienda de acuerdo a su id

    Args:
    * id_tienda (int, optional):Id de la tienda.
    * fecha (str, optional):Fecha de creación de la tienda.
    * tienda (str, optional): Nombre de la tienda.
    * importe (float, optional): El importe de la tienda.

    Returns:
    * ventas(list): Retorna la lista de todas las tiendas
    """
    for elem in ventas:
        if elem['id'] == id_tienda:
            elem['fecha'] = fecha
            elem['tienda'] = tienda
            elem['importe'] = importe
    return ventas
