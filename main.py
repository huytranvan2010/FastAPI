from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# # ko dùng asyns
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# # dùng async
# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


# dùng async, nâng cấp hơn chút với PUT request
# Khởi tạo body sử dụng Python types bằng `Pydantic`
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None 
    
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

"""
Chạy thử: nên dùng postman cho tiện
Nhập: http://127.0.0.1:8000/items/5?q=somequery  xem được gì
"""