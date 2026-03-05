from fastapi import FastAPI, Path, Query
from cardata import CarData

app = FastAPI(
    title="API de Gestión de Coches",
    description="API desarrollada con FastAPI para consultar coches, obtener coches por id y filtrar por marca.",
    version="1.0.0"
)
car = CarData()

@app.get("/coches/")
async def read_coches(skip: int = 0, total: int = 10, todos: bool | None = None):
    if (todos):
        return await car.get_allICoches()
    else:
        return await car.get_coches(skip,total)

@app.get("/coches/{coche_id}")
async def read_coche(coche_id : int):
    return await car.get_coche(coche_id)

@app.get("/coches/marca/")
async def read_marca(marca: str):
    return await car.get_cochesMarca(marca)