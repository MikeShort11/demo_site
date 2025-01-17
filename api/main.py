from fastapi import Body, FastAPI

app = FastAPI()

#glbal list of menu items
items = ["Classic Lemonade", "Strawberry Lemonade", "Mint Lemonade"]

@app.get("/menu")
async def get_menu():
    return {"items":items}

@app.put("/menu")
async def put_menu(input:str=Body(...)):
    items.append(input)
    return {"message": f"Item: {input} sucsessfuly added"}
