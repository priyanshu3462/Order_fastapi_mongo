from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from bson import ObjectId
from database import products_collection, orders_collection
from models import Product, Order
from schemas import product_helper, order_helper

app = FastAPI()
@app.post("/products", status_code=201)
async def create_product(product: Product):
    result = await products_collection.insert_one(product.dict())
    new_product = await products_collection.find_one({"_id": result.inserted_id})
    return product_helper(new_product)


@app.get("/products", status_code=200)
async def list_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["size"] = size

    cursor = products_collection.find(query).skip(offset).limit(limit)
    products = [product_helper(p) async for p in cursor]
    return products


@app.post("/orders", status_code=201)
async def create_order(order: Order):
    result = await orders_collection.insert_one(order.dict())
    new_order = await orders_collection.find_one({"_id": result.inserted_id})
    return order_helper(new_order)


@app.get("/orders/{user_id}", status_code=200)
async def list_orders(user_id: str, limit: int = 10, offset: int = 0):
    cursor = orders_collection.find({"user_id": user_id}).skip(offset).limit(limit)
    orders = [order_helper(o) async for o in cursor]
    return orders
