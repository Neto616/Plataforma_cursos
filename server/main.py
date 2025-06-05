from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import controllers, views

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["*"] para permitir todos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(views.app)
app.include_router(controllers.app)

