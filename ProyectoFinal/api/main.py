from fastapi.responses import JSONResponse
import uvicorn 
from fastapi import FastAPI, HTTPException, Request
from api.data.portatildata import PortatilData
from api import laptops

app = FastAPI( 
    title="LaptopAPI",
    description="ApiRestFul para la gestion de portatiles",
    version="0.0.1",
    contact={
        "name":"Pedro Scarpati"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
    )

portatil = PortatilData()

@app.exception_handler(HTTPException)
async def notFound_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code = exc.status_code,
        content = {"error":"Portatil no encontrado"}
    )

app.include_router(laptops,
                   tags=["laptops"],
                   prefix="/laptops")
