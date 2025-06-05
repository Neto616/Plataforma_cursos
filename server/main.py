from fastapi import FastAPI
from routes import controllers, views

app = FastAPI()


app.include_router(views.app)
app.include_router(controllers.app)

