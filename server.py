from fastapi import FastAPI
from enum import Enum

class AvaialbleCuisine(str, Enum):
    italian = "italian"
    mexican = "mexican"
    indian = "indian"

app = FastAPI()

@app.get("/hello/{name}")
async def hello(name: str):
    return "welcome to fastapi tutorial, " + name

food_items = {
    "italian": ["pizza", "pasta", "risotto"],
    "mexican": ["tacos", "salsa", "guacamole"],
    "indian": ["biryani", "samosa", "naan"]
}

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvaialbleCuisine):
    return food_items.get(cuisine, "Cuisine not found")

coupon_code = {
    1: "50% off",
    2: "30% off",
    3: "40% off"
}

@app.get("/get_coupon/{code}")
async def get_items(code: int):
    return {"dicount_amount": coupon_code.get(code)}