from fastapi import FastAPI
from api.routes.user import user_routes
from api.routes.task import task_routes
from api.routes.product import product_routes
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost:3000",
    "*"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(user_routes)
app.include_router(task_routes)
app.include_router(product_routes)