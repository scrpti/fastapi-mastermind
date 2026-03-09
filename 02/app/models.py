from pydantic import BaseModel, Field

class Partido(BaseModel):
    anyo: int = Field(ge= 0, le= 2026)
    fase: str
    equipolocal: str
    goleslocales: int = Field(ge= 0)
    golesvisitante: int = Field(ge= 0)
    equipovisitante: str
    estaequipoanfitrion: bool
