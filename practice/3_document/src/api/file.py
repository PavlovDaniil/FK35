from fastapi import APIRouter
from src.utils import file

router = APIRouter()
@router.get("/test")
def read_root():
    return {"Hello": "World"}

@router.get("/files")
def get_files():
    list_file = file.get_all_files()
    return {"files": list_file}
