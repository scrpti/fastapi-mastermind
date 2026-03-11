from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_read_laptopId():
    response = client.get("/laptops/35")
    assert response.status_code == 200

def test_read_laptopPrecioMaxNegativo():
    response = client.get("/laptops/preciomax?precioMax=-1")
    assert response.json()=={"detail":[{"type":"greater_than","loc":["query","precioMax"],"msg":"Input should be greater than 0","input":"-1","ctx":{"gt":0}}]}

def test_post_laptop():
    response = client.post("/laptops", json={"marca": "tecno",
                                            "modelo": "Tecno Megabook T1 Laptop (11th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
                                            "precio": 264,
                                            "OS": "dos",
                                            "anyosgarantia": "2"})
    assert response.status_code == 200

def test_delete_laptop():
    response = client.delete("/laptops/42")
    assert response.json() == {"info": "borrado portatil 42"}
    assert response.status_code == 200