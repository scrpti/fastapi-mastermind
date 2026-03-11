from fastapi import FastAPI, Response, status, Path, Query, Body
from futboldata import FutbolData
from models import Partido
from typing import Annotated


app = FastAPI()
futdata = FutbolData()

@app.get("/partidos")
async def getPartidos(skip: Annotated[int, Query(description="Skip debe ser mayor o igual que 0", ge=0)], total: Annotated[int, Query(ge=0)]):
    return await futdata.get_partidos(skip, total)

@app.get("/todospartidos")
async def getPartidos():
    return await futdata.get_allIPartidos()

@app.get("/partidos/{partido_id}")
async def getPartidoByID(partido_id: Annotated[int, Path(description="El ID del partido debe ser mayor o igual que 0", ge=0)]):
    return await futdata.get_partido(partido_id)

@app.get("/partidosequipo/{partido_name}")
async def getPartidoByEquipoByParameter(partido_name):
    return await futdata.get_partidosEquipo(partido_name)

@app.get("/partidosequipo/")
async def getPartidoByEquipoByQuery(equipo: str):
    return await futdata.get_partidosEquipo(equipo)

@app.post("/partidos")
async def createPartido(partido: Annotated[Partido, Body(description="Datos del partido")]):
    return await futdata.write_partido(partido)

@app.put("/partidos/{partido_id}")
async def updatePartido(partido_id:int, partido:Partido, response:Response):
    partido_existe = await futdata.get_partido(partido_id)
    if partido_existe:
        return await futdata.update_partido(partido_id,partido)
    else:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"Partido con ID " + str(partido_id) + " no encontrado"}

@app.delete("/partidos/{partido_id}")
async def deletePartido(partido_id:int, response:Response):
    partido_existe = await futdata.get_partido(partido_id)
    if partido_existe:
        return await futdata.delete_partido(partido_id)
    else:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"Partido con ID " + str(partido_id) + " no encontrado"}