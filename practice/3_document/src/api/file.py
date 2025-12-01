from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from src.utils import file
import os

router = APIRouter()
@router.get("/test")
def read_root():
    return {"Hello": "World"}

@router.get("/files")
def get_files():
    list_file = file.get_all_files()
    return {"files": list_file}

@router.get("/files/{filename}")
def read_file(filename: str):
    content = file.read_file(filename)
    return {"content": content}

@router.get("/files/placeholders/{filename}")
def read_file_placeholder(filename: str):
    placeholders = file.search(filename)
    return {"placeholders": placeholders}

@router.post("/files/{filename}")
def generate_pdf(filename: str, data: dict = None):
    pdf = file.generate_pdf_from_template(filename, data)
    return FileResponse(pdf, media_type="application/pdf", filename=filename)