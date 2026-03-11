#importamos desde fastAPI, la clases FastAPI y Response
from typing import Union
from enum import Enum
from pydantic import BaseModel, Field

class Sistema(str,Enum):
    mac = "mac",
    windows = "windows",
    dos = "dos",
    chrome = "chrome",
    android = "android",
    other = "other",
    ubuntu = "ubuntu"


# Modelo para un Laptop
class Portatil(BaseModel):
    marca: str
    modelo: str
    precio : int = 0
    OS : Sistema
    anyosgarantia : int