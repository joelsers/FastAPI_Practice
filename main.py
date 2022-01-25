from fastapi import FastAPI
import random
from models import Item
app = FastAPI()

db = []


@app.get("/")
async def root():
    rand_num = random.randint(0,100)
    for x in range(1,100):
        if rand_num <= 20 or rand_num >= 80:
            return {"boom shocka locka": f'{rand_num}'}
        else:
            return {"message": f'{rand_num}'}

@app.get("/items")
async def read_items():
     return db

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id" : item_id}

@app.post("/items")
async def post_item(item: Item):
    db.append(item.dict())
    return db[-1]

@app.patch("/items")
async def patch_item(item: Item):
    for db_item in db:
        if item.id == db_item['id']:
            db_item['name'] = item.name
            return db_item
        else:
            return ('no item with that id')

@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    for item in db:      
        if item_id == item['id']:
            db.pop(db.index(item))
            return db
        else:
            return ('no item with that id')