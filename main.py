from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola, FastAPI!"}




@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id <= 0:  # Simulació de que l'element no existeix
        return {"status": 404, "detail": "Item s'ha no trobat"}
    return {"item_id": item_id, "name": f"Item {item_id}"}


#### ES DE HTTPEXCEPTOIN
#@app.get("/items/{item_id}")
#def read_item(item_id: int):
#    if item_id <= 0:  # retorna un error 404
#        raise HTTPException(status_code=404, detail="Item no trobat")
#    return {"item_id": item_id, "name": f"Item {item_id}"}

#@app.get("/items/{item_id}")
#def read_item(item_id: int):
#    return {"item_id": item_id, "name": f"Item {item_id}"}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id, "username": f"user{user_id}"}


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float
    quantity: int
    optional_field: str | None = None

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item creat correctament", "item": item.dict()}
