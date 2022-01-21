from fastapi import FastAPI
import random
app = FastAPI()


@app.get("/")
async def root():
    rand_num = random.randint(0,100)
    for x in range(1,100):
        if rand_num == 1 or rand_num == 100:
            return {"boom shocka locka": f'{rand_num}'}
        else:
            return {"message": f'{rand_num}'}
    

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id" : item_id}