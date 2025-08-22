from app.config import settings
from fastapi import FastAPI


app = FastAPI(title=settings.APP_NAME)
