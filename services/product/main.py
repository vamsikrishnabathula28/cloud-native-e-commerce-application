from fastapi import FastAPI, HTTPException, Depends
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Product Service", version="1.0.0")

# MongoDB connection
client = MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017"))
db = client.ecommerce
products = db.products

class Product(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    category: str
    image_url: Optional[str] = None

class ProductResponse(Product):
    id: str

    class Config:
        from_attributes = True

@app.post("/products/", response_model=ProductResponse)
async def create_product(product: Product):
    product_dict = product.dict()
    result = products.insert_one(product_dict)
    product_dict["id"] = str(result.inserted_id)
    return product_dict

@app.get("/products/", response_model=List[ProductResponse])
async def get_products():
    product_list = []
    for product in products.find():
        product["id"] = str(product["_id"])
        del product["_id"]
        product_list.append(product)
    return product_list

@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str):
    product = products.find_one({"_id": product_id})
    if product:
        product["id"] = str(product["_id"])
        del product["_id"]
        return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: str, product: Product):
    product_dict = product.dict()
    result = products.update_one({"_id": product_id}, {"$set": product_dict})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    product_dict["id"] = product_id
    return product_dict

@app.delete("/products/{product_id}")
async def delete_product(product_id: str):
    result = products.delete_one({"_id": product_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "product"} 