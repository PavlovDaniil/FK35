from fastapi import APIRouter
from .file import router as file

routers = APIRouter()
routers.include_router(file)
