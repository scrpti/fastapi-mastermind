from pydantic import BaseModel

class Partido(BaseModel):
    anyo: int
    fase: str
    equipolocal: str
    goleslocales: int
    golesvisitante: int
    equipovisitante: str
    estaequipoanfitrion: bool
