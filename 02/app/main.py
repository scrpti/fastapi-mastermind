from fastapi import FastAPI, Path, Query
from futboldata import FutbolData
from models import Partido


app = FastAPI()
futdata = FutbolData()

@app.get("/partidos")
async def getPartidos(skip: int=0, total: int=10):
    return await futdata.get_partidos(skip, total)


@app.get("/todospartidos")
async def getPartidos():
    return await futdata.get_allIPartidos()

@app.get("/partidos/{partido_id}")
async def getPartidoByID(partido_id: int):
    return await futdata.get_partido(partido_id)

@app.get("/partidosequipo/{partido_name}")
async def getPartidoByEquipoByParameter(partido_name):
    return await futdata.get_partidosEquipo(partido_name)

@app.get("/partidosequipo/")
async def getPartidoByEquipoByQuery(equipo: str):
    return await futdata.get_partidosEquipo(equipo)

@app.post("/partidos")
async def createPartido(partido: Partido):
    return await futdata.write_partido(partido)

@app.put("/partidos/{partido_id}")
async def updatePartido(partido_id:int, partido:Partido):
    return await futdata.update_partido(partido_id,partido)

@app.delete("/partidos/{partido_id}")
async def deletePartido(partido_id:int):
    return await futdata.delete_partido(partido_id)