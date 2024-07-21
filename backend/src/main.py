from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from backend.src.router import router as weather_router
app = FastAPI()

app.include_router(weather_router)
origins = [
    'http://127.0.0.1:5173',
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)