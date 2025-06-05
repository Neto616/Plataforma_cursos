#Servidor que actuara de Bot
from fastapi import FastAPI
from routes import views

app = FastAPI()
app.include_router(views.app)

