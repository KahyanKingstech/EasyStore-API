from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from customer import router as customer_router
from collection import router as collection_router
from product import router as product_router
from order import router as order_router
# from inventory import router as inventory_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customer_router)
app.include_router(collection_router)
app.include_router(product_router)
app.include_router(order_router)
# app.include_router(inventory_router)
