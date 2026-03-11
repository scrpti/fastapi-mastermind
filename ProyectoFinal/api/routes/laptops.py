from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from api import Portatil
from api import PortatilData

portatil = PortatilData()
router = APIRouter()

@router.get("", tags="get", summary="Obtener los portatiles mediante los filtros skip, total, modelo y all")
async def get_portatiles(skip: Annotated[int,Query(ge=0)],
                         total: Annotated[int,Query(gt=0)],
                         filtroNombre: str | None = Query(default=None, 
                                                          description="variable que filtra los portatiles por su modelo"),
                         all: bool = False
                         ):
                        #  modelo: Annotated[str,Query(min_length=2)],
                         
    if (all):
        return await portatil.get_allPortatiles()
    else:
        return await portatil.get_portatilesModelo(skip, total, filtroNombre)

@router.get("/preciomax", tags="getByPrecioMax", summary="Obtener los portatiles mediante el precio maximo")
async def get_portatilesByPrecioMax(precioMax:Annotated[int, Query(gt=0, 
                                                                   description="variable que marca el precio maximo " \
                                                                   "de los portatiles filtrados")]):
    return await portatil.get_portatilesPrecioMax(precioMax)

@router.get("/os", tags="getByOS", summary="Obtener los portatiles mediante el sistema operativo")
async def get_portatilesByOS(os:Annotated[str, Query(min_length=2,description="variable que marca el os a filtrar")]):
    return await portatil.get_portatilesOS(os)

@router.get("/{portatil_id}", tags="getByID", summary="Obtener un portatil mediante el ID")
async def get_portatilByID(portatil_id: Annotated[int, Path(gt=0)]):
    portatil_objeto = await portatil.get_portatil(portatil_id)
    if not portatil_objeto:
        raise HTTPException(status_code=404)
    return portatil_objeto

@router.post("", tags="POST", summary="Crear un portatil y guardarlo en el archivo")
async def post_portatil(portatilInput: Portatil):
    return await portatil.write_portatil(portatilInput)

@router.put("/{id}", tags="PUT", summary="Actualizar un portatil y guardarlo en el archivo")
async def put_portatil(id: int, portatilInput: Portatil):
    portatil_objeto = await portatil.get_portatil(id)
    if not portatil_objeto:
        raise HTTPException(status_code=404)
    return await portatil.update_portatil(id, portatilInput)

@router.delete("/{id}", tags="DELETE", summary="Borrar un portatil del archivo")
async def delete_portatil(id: int):
    portatil_objeto = await portatil.get_portatil(id)
    if not portatil_objeto:
        raise HTTPException(status_code=404)
    return await portatil.delete_portatil(id)