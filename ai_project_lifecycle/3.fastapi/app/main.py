# -*- coding:utf-8 -*-
from typing import Any, List, Union, Dict, Optional
from unittest import result
from uuid import UUID, uuid4
from datetime import datetime

from fastapi import FastAPI, UploadFile, File
from fastapi.param_functions import Depends

from pydantic import BaseModel, Field

from app.model import EfficientNet, get_config, get_model, predict_from_image_byte

app = FastAPI()

@app.get('/')
def hello_world():
    return {'hello': 'world'}

class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4) # 고유 식별자 
    name: str 
    price: float

class Order(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    products: List[Product] = Field(default_factory=list) # 빈 list 저장 
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @property 
    def bill(self):
        return sum([product.price for product in self.products])

    def add_product(self, product: Product):
        ''' 1) 이미 존재하는 상품인지 2) 업데이트하면 시간 갱신'''
        if product.id in [existing_product.id for existing_product in self.products]:
            return self
        
        self.products.append(product)
        self.updated_at = datetime.now()
        return self


orders = [] # 보통 데이터베이스로 하지만, 여기선 그냥 하는 거임    

@app.get('/orders/')
async def get_orders() -> List[Order]:
    return orders

def get_order_by_id(order_id: UUID) -> Optional[Order]:
    # 제너레이터로 메모리 절약
    return next((order for order in orders if order.id == order_id), None)

@app.get('/order/{order_id}', description='오더 정보 가져오기')
async def get_order(order_id: UUID) -> Union[Order, Dict]:
    order = get_order_by_id(order_id=order_id)
    if not order:
        return {'message':'주문정보없음'} 
    return order 

class InferenceImageProduct(Product):
    name: str= 'inference_image_product'
    price: float= 100.0
    result: Optional[List]

@app.post('/order', description='주문요청')
async def make_order(files: List[UploadFile] = File(...), 
                    model:EfficientNet = Depends(get_model), 
                    config: Dict[str, Optional[Any]] = Depends(get_config)):
    # Depends는 의존성 주입할때, 반복적이고 공통적인 로직이 필요할 때 사용 가능 
    products = []
    for file in files:
        image_bytes = await file.read()
        inferece_result = predict_from_image_byte(model=model, image_bytes=image_bytes, config=config)
        product = InferenceImageProduct(result=inferece_result)
        products.append(product)

    new_order = Order(products=products)
    orders.append(new_order)
    return new_order

class OrderUpdate(BaseModel):
    products: List[Product] = Field(default_factory=list)

def update_order_by_id(order_id: UUID, order_update: OrderUpdate) -> Optional[Order]:
    existing_order = get_order_by_id(order_id=order_id)
    if not existing_order: return 

    updated_order = existing_order.copy()
    for next_product in order_update.products:
        updated_order = existing_order.add_product(next_product)
    
    return updated_order

@app.patch('/order/{order_id}', description='주문을 수정')
async def update_order(order_id: UUID, order_update: OrderUpdate):
    updated_order = update_order_by_id(order_id=order_id, order_update=order_update)
    
    if not updated_order: return {'message': '주물정보없음'}
    return updated_order

@app.get('/bill/{order_id}', description='계산 요청')
async def get_bill(order_id: UUID):
    found_order = get_order_by_id(order_id=order_id)
    if not found_order: return {'message': '주문 정보 없음'}
    return found_order.bill
